# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_test_pb2 as grpc__test__pb2


class GreeterStub(object):
    """서비스 이름 위에 주석을 달면 생성된 grpc컴파일 파일에 docstring으로 들어가게 된다.
    서비스 이름 Greeter
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/Greeter/SayHello',
                request_serializer=grpc__test__pb2.HelloRequest.SerializeToString,
                response_deserializer=grpc__test__pb2.HelloReply.FromString,
                )
        self.GetFeature = channel.unary_unary(
                '/Greeter/GetFeature',
                request_serializer=grpc__test__pb2.Point.SerializeToString,
                response_deserializer=grpc__test__pb2.Feature.FromString,
                )
        self.ListFeatures = channel.unary_stream(
                '/Greeter/ListFeatures',
                request_serializer=grpc__test__pb2.Rectangle.SerializeToString,
                response_deserializer=grpc__test__pb2.Feature.FromString,
                )
        self.RecordRoute = channel.stream_unary(
                '/Greeter/RecordRoute',
                request_serializer=grpc__test__pb2.Point.SerializeToString,
                response_deserializer=grpc__test__pb2.RouteSummary.FromString,
                )
        self.RouteChat = channel.stream_stream(
                '/Greeter/RouteChat',
                request_serializer=grpc__test__pb2.RouteNote.SerializeToString,
                response_deserializer=grpc__test__pb2.RouteNote.FromString,
                )


class GreeterServicer(object):
    """서비스 이름 위에 주석을 달면 생성된 grpc컴파일 파일에 docstring으로 들어가게 된다.
    서비스 이름 Greeter
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeature(self, request, context):
        """A simple RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFeatures(self, request, context):
        """A server-to-client streaming RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordRoute(self, request_iterator, context):
        """A client-to-server streaming RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteChat(self, request_iterator, context):
        """A Bidirectional streaming RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=grpc__test__pb2.HelloRequest.FromString,
                    response_serializer=grpc__test__pb2.HelloReply.SerializeToString,
            ),
            'GetFeature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeature,
                    request_deserializer=grpc__test__pb2.Point.FromString,
                    response_serializer=grpc__test__pb2.Feature.SerializeToString,
            ),
            'ListFeatures': grpc.unary_stream_rpc_method_handler(
                    servicer.ListFeatures,
                    request_deserializer=grpc__test__pb2.Rectangle.FromString,
                    response_serializer=grpc__test__pb2.Feature.SerializeToString,
            ),
            'RecordRoute': grpc.stream_unary_rpc_method_handler(
                    servicer.RecordRoute,
                    request_deserializer=grpc__test__pb2.Point.FromString,
                    response_serializer=grpc__test__pb2.RouteSummary.SerializeToString,
            ),
            'RouteChat': grpc.stream_stream_rpc_method_handler(
                    servicer.RouteChat,
                    request_deserializer=grpc__test__pb2.RouteNote.FromString,
                    response_serializer=grpc__test__pb2.RouteNote.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """서비스 이름 위에 주석을 달면 생성된 grpc컴파일 파일에 docstring으로 들어가게 된다.
    서비스 이름 Greeter
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/SayHello',
            grpc__test__pb2.HelloRequest.SerializeToString,
            grpc__test__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFeature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/GetFeature',
            grpc__test__pb2.Point.SerializeToString,
            grpc__test__pb2.Feature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Greeter/ListFeatures',
            grpc__test__pb2.Rectangle.SerializeToString,
            grpc__test__pb2.Feature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordRoute(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Greeter/RecordRoute',
            grpc__test__pb2.Point.SerializeToString,
            grpc__test__pb2.RouteSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteChat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Greeter/RouteChat',
            grpc__test__pb2.RouteNote.SerializeToString,
            grpc__test__pb2.RouteNote.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
