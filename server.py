import asyncio
import logging
import math
import time
from typing import AsyncIterable, Iterable

import grpc
import grpc_test_pb2
import grpc_test_pb2_grpc
import test_db_connect


def get_feature(feature_db: Iterable[grpc_test_pb2.Feature],
                point: grpc_test_pb2.Point) -> grpc_test_pb2.Feature:
    """Returns Feature at given location or None."""
    for feature in feature_db:
        if feature.location == point:
            return feature
    return None


def get_distance(start: grpc_test_pb2.Point,
                 end: grpc_test_pb2.Point) -> float:
    """Distance between two points."""
    coord_factor = 10000000.0
    lat_1 = start.latitude / coord_factor
    lat_2 = end.latitude / coord_factor
    lon_1 = start.longitude / coord_factor
    lon_2 = end.longitude / coord_factor
    lat_rad_1 = math.radians(lat_1)
    lat_rad_2 = math.radians(lat_2)
    delta_lat_rad = math.radians(lat_2 - lat_1)
    delta_lon_rad = math.radians(lon_2 - lon_1)

    # Formula is based on http://mathforum.org/library/drmath/view/51879.html
    a = (pow(math.sin(delta_lat_rad / 2), 2) +
         (math.cos(lat_rad_1) * math.cos(lat_rad_2) *
          pow(math.sin(delta_lon_rad / 2), 2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371000
    # metres
    return R * c


class Greeter(grpc_test_pb2_grpc.GreeterServicer):
    """pb2_grpc파일의 생성된 서비스 이름+Servicer 클래스를 상속받도록 작성"""

    # 스트리밍 테스트를 위한 임시 database 
    def __init__(self) -> None:
        self.db = test_db_connect.read_test_database()

    # 단방향 rpc 통신
    async def SayHello(self, request, context):
        return grpc_test_pb2.HelloReply(message=f"hello, {request.name}")
    
    # 단방향 rpc 통신
    def GetFeature(self, request: grpc_test_pb2.Point,
                   unused_context) -> grpc_test_pb2.Feature:
        feature = get_feature(self.db, request)
        if feature is None:
            return grpc_test_pb2.Feature(name="", location=request)
        else:
            return feature

    # 서버 스트리밍 rpc
    async def ListFeatures(
            self, request: grpc_test_pb2.Rectangle,
            unused_context) -> AsyncIterable[grpc_test_pb2.Feature]:
        """특정 범위의 위도, 경도를 request의 인자로 받으면 db에서 해당 범위 내의 지역을 반환하는 메소드"""
        left = min(request.lo.longitude, request.hi.longitude)
        right = max(request.lo.longitude, request.hi.longitude)
        top = max(request.lo.latitude, request.hi.latitude)
        bottom = min(request.lo.latitude, request.hi.latitude)
        for feature in self.db:
            if (feature.location.longitude >= left and
                    feature.location.longitude <= right and
                    feature.location.latitude >= bottom and
                    feature.location.latitude <= top):
                yield feature

    # 클리이언트 스트리밍 rpc
    async def RecordRoute(self, request_iterator: AsyncIterable[
        grpc_test_pb2.Point], unused_context) -> grpc_test_pb2.RouteSummary:
        point_count = 0
        feature_count = 0
        distance = 0.0
        prev_point = None

        start_time = time.time()
        async for point in request_iterator:
            point_count += 1
            if get_feature(self.db, point):
                feature_count += 1
            if prev_point:
                distance += get_distance(prev_point, point)
            prev_point = point

        elapsed_time = time.time() - start_time
        return grpc_test_pb2.RouteSummary(point_count=point_count,
                                            feature_count=feature_count,
                                            distance=int(distance),
                                            elapsed_time=int(elapsed_time))

    # 양방향 스트리밍 rpc
    async def RouteChat(
            self, request_iterator: AsyncIterable[grpc_test_pb2.RouteNote],
            unused_context) -> AsyncIterable[grpc_test_pb2.RouteNote]:
        prev_notes = []
        async for new_note in request_iterator:
            for prev_note in prev_notes:
                if prev_note.location == new_note.location:
                    yield prev_note
            prev_notes.append(new_note)


async def serve() -> None:
    server = grpc.aio.server()
    grpc_test_pb2_grpc.add_GreeterServicer_to_server(
        Greeter(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())