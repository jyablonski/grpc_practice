import jacobs_grpc_pb2_grpc
import jacobs_grpc_pb2
import random
import grpc
from concurrent import futures


class jacobs_serviceServicer(jacobs_grpc_pb2_grpc.jacobs_serviceServicer):
    def __init__(self):
        self.choices = ["yes", "no", "maybe"]

    def test_message(self, request, context):

        # these attributes below are just put here to make the message + sender look cleaner
        classification_response = random.choice(self.choices).upper()
        name = request.message
        requester = request.requester
        message_sender = f"grpc_robot_{random.randrange(10)}"

        # Below is where the variables go that we defined for the message_response message in the proto file.
        return jacobs_grpc_pb2.message_response(
            message=f"Hello {requester}! The name you requested is {name} - is this name in our database ... {classification_response}!",
            sender=message_sender,
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jacobs_grpc_pb2_grpc.add_jacobs_serviceServicer_to_server(
        jacobs_serviceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
