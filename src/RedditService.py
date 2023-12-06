import grpc
from gen import service_pb2_grpc
from gen import service_pb2
from gen import model_pb2


class RedditServicer(service_pb2_grpc.RedditServicer):
    """Provides methods that implement functionality of route guide server."""

    def CreatePost(self, request, context):
            post = model_pb2.Post(title="hello world")
            return service_pb2.CreatePostRespond(post=post)
