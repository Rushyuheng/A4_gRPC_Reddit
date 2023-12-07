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

    def ConstrunctPostFromDB(self,db__post_record) -> dict:
        respond_post = model_pb2.Post(title=db__post_record['title'],
                                        text=db__post_record['text'],
                                        author=model_pb2.User(user_id=db__post_record['author']),
                                        score= db__post_record['score'],
                                        state= model_pb2.Post.PostState.POST_STATE_NORMAL,
                                        publication_date= db__post_record['publication_date']
                                         )
            
        if(db__post_record['url_type'] == mockDB.UrlType.VIDEO):
            respond_post.video_url = db__post_record['url']
        elif(db__post_record['url_type'] == mockDB.UrlType.IMAGE):
            respond_post.image_url = db__post_record['url']
        return respond_post


    def CreatePost(self, request, context):
        #discard wrapper 
        request_post = request.post
            
        # check one of field for url
        url = None
        url_type = None
        if(request_post.HasField("video_url")):
            url =  request_post.video_url
            url_type = mockDB.UrlType.VIDEO
        elif(request_post.HasField("image_url")):
            url =  request_post.image_url
            url_type = mockDB.UrlType.IMAGE

        #create new DB record
        new_post_record = {
            "id": len(self.mockDB.post),
            "title": request_post.title,
            "text": request_post.text,
            "url_type": url_type,
            "url": url,
            "author": request_post.author.user_id, 
            "score": 0,
            "state": mockDB.PostState.POST_STATE_NORMAL,
            "publication_date": datetime.date.today().strftime("%Y-%m-%d")
        }
        #insert into DB
        self.mockDB.post.append(new_post_record)

        #DEBUG
        print(self.mockDB.post[-1])

        respond_post = self.ConstrunctPostFromDB(new_post_record)

        return service_pb2.CreatePostRespond(post=respond_post)
            
    def VotePost(self, request, context):
        #filter the post record in the database
        post_record = next(filter(lambda record: record['id'] == request.post_id, self.mockDB.post))
        print(type(post_record))

        if(request.vote):
            #upvote
            post_record['score'] += 1 
        else:
            #downvote
            post_record['score'] -= 1

        #DEBUG
        print(self.mockDB.post[-1])

        respond_post = self.ConstrunctPostFromDB(post_record)

        return service_pb2.CreatePostRespond(post=respond_post)
