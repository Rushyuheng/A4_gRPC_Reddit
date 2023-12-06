import grpc
from google.protobuf.timestamp_pb2 import Timestamp
from gen import service_pb2_grpc
from gen import service_pb2
from gen import model_pb2
import mockDB
import datetime


class RedditServicer(service_pb2_grpc.RedditServicer):
    """Provides methods that implement functionality of route guide server."""
    def __init__(self) -> None:
        #start a new mock DB
        self.mockDB = mockDB.mockDB()

    def CreatePost(self, request, context):
            #discard wrapper 
            request_post = request.post
            
            # check one of field for url
            url = None
            if(request_post.HasField("video_url")):
                url =  request_post.video_url
            elif(request_post.HasField("image_url")):
                url =  request_post.image_url

            #create new DB record
            newPost = {
                "id": len(self.mockDB.post),
                "title": request_post.title,
                "text": request_post.text,
                "url": url,
                "author": request_post.author.user_id, 
                "score": 00,
                "state": mockDB.PostState.POST_STATE_NORMAL,
                "publication_date": datetime.date.today().strftime("%Y-%m-%d")
            }
            #insert into DB
            self.mockDB.post.append(newPost)

            #DEBUG
            print(self.mockDB.post[-1])

            respond_post = model_pb2.Post(title=newPost['title'],
                                         text=newPost['text'],
                                         author=model_pb2.User(user_id=newPost['author']),
                                         score= newPost['score'],
                                         state= model_pb2.Post.PostState.POST_STATE_NORMAL,
                                         publication_date= newPost['publication_date']
                                         )
            
            if(request_post.HasField("video_url")):
                respond_post.video_url = newPost['url']
            elif(request_post.HasField("image_url")):
                respond_post.image_url = newPost['url']

            return service_pb2.CreatePostRespond(post=respond_post)
            
