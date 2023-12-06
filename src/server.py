from concurrent import futures

import grpc
import RedditService
from gen import service_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_RedditServicer_to_server(
        RedditService.RedditServicer(), server
    )
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("server listening on port:" + "50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()