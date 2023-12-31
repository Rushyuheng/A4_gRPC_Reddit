from concurrent import futures
import sys
import grpc
import logging
import reddit_service
from gen import service_pb2_grpc

def serve(port:str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_RedditServicer_to_server(
        reddit_service.RedditServicer(), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("server listening on port:" + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if(len(sys.argv) <= 1):
        # if no CMD argument provided, use the default 50051 port
        print("Empty Port argument, using default port 50051")
        port = "50051"
    else:
        # use the CMD argument as the port number 
        port = str(sys.argv[1])

    try:
        port_value = int(port)
        if port_value < 50000 or port_value > 50100:
            print("Invalid Port, please use port between 50000-50100, using default port 50051 now")
            port = "50051"
    except ValueError:
        print("Invalid Port, please use port between 50000-50100, using default port 50051 now")
        port = "50051"


    serve(port)