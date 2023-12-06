import grpc
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
        

        # Make the gRPC call by invoking the service method with the request
        response = self.stub.CreatePost(service_pb2.CreatePostRequest(post=post))

        # Process the response received from the server
        print("Received response:", response)

if __name__ == '__main__':
    port = input("Enter the port bewteen 50000 - 50100 to connect to:")

    
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
    client.create_post("rush", "new meme", "lol", "www.meme.doogi",)