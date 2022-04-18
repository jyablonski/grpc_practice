import grpc
import jacobs_grpc_pb2_grpc
import jacobs_grpc_pb2

from faker import Faker

fake = Faker()


def run():
    channel = grpc.insecure_channel("localhost:50051")
    jacobs_proto = jacobs_grpc_pb2_grpc.jacobs_serviceStub(channel)
    message_response = jacobs_proto.test_message(
        jacobs_grpc_pb2.message_request(message=f"{fake.name()}", requester="jacob")
    )
    print(
        f"Client received from sender {message_response.sender} -- {message_response.message}"
    )
    # these message and sender attributes are defined in the proto file for message_response.


if __name__ == "__main__":
    run()
