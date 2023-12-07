import grpc
import sys
from gen import service_pb2_grpc
from gen import service_pb2
from gen import model_pb2

class RedditClient:
    def __init__(self):
        self.channel = None
        self.stub = None

    def start_connection(self,port):
        # Create a gRPC channel to the server (assuming server running at localhost:50051)
        self.channel = grpc.insecure_channel('localhost:' + port)

        # Create a stub (client) to interact with the server
        self.stub = service_pb2_grpc.RedditStub(self.channel)


    def create_post(self, user_id:str, title:str, text:str, url:str):
        # Create a request message
        author = model_pb2.User(user_id=user_id)
        post = model_pb2.Post(title=title,text=text,image_url=url,author=author)
        # wrap post
        request = service_pb2.CreatePostRequest(post=post)

        # Make the gRPC call by invoking the service method with the request
        response = self.stub.CreatePost(request)

        # Process the response received from the server
        print("Received response:", response)
    
    def vote_post(self, post_id:int, vote:bool):
        # Create a request message
        request = service_pb2.VotePostRequest(post_id=post_id,vote=vote)

        # Make the gRPC call by invoking the service method with the request
        response = self.stub.VotePost(request)

        # Process the response received from the server
        print("Received response:", response)
    
    def get_post(self, post_id:int):
        # Create a request message
        request = service_pb2.GetPostRequest(post_id=post_id)

        # Make the gRPC call by invoking the service method with the request
        response = self.stub.VotePost(request)

        # Process the response received from the server
        print("Received response:", response)

if __name__ == '__main__':
    if(len(sys.argv) <= 1):
        print("Empty Port argument, using default port 50051")
        port = "50051"
    else:
        port = str(sys.argv[1])

    try:
        port_value = int(port)
        if port_value < 50000 or port_value > 50100:
            print("Invalid Port, using default port 50051")
            port = "50051"
    except ValueError:
        print("Invalid Port, using default port 50051")
        port = "50051"


    client = RedditClient()
    client.start_connection(port)
    #client.create_post("rush", "new meme", "lol", "www.meme.doogi")
    #client.vote_post(0,True)
    client.get_post(2)