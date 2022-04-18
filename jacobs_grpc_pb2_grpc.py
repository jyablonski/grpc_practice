# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import jacobs_grpc_pb2 as jacobs__grpc__pb2


class jacobs_serviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.test_message = channel.unary_unary(
                '/jacobs_proto.jacobs_service/test_message',
                request_serializer=jacobs__grpc__pb2.message_request.SerializeToString,
                response_deserializer=jacobs__grpc__pb2.message_response.FromString,
                )


class jacobs_serviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def test_message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_jacobs_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'test_message': grpc.unary_unary_rpc_method_handler(
                    servicer.test_message,
                    request_deserializer=jacobs__grpc__pb2.message_request.FromString,
                    response_serializer=jacobs__grpc__pb2.message_response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jacobs_proto.jacobs_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class jacobs_service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def test_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jacobs_proto.jacobs_service/test_message',
            jacobs__grpc__pb2.message_request.SerializeToString,
            jacobs__grpc__pb2.message_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
