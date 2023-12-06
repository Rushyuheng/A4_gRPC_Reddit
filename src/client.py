import grpc
from gen import service_pb2_grpc
from gen import service_pb2
from gen import model_pb2

def run_grpc_client():
    # Create a gRPC channel to the server (assuming server running at localhost:50051)
    channel = grpc.insecure_channel('localhost:50051')

    # Create a stub (client) to interact with the server
    stub = service_pb2_grpc.RedditStub(channel)

    # Create a request message
    request = model_pb2.Post()
    # Set fields in the request message, if needed

    # Make the gRPC call by invoking the service method with the request
    response = stub.CreatePost(request)

    # Process the response received from the server
    print("Received response:", response)

if __name__ == '__main__':
    run_grpc_client()