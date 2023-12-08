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

    def ConstructPostFromDBRecord(self,db_post_record) -> dict:


        respond_post = model_pb2.Post(title=db_post_record['title'],
                                        text=db_post_record['text'],
                                        author=model_pb2.User(user_id=db_post_record['author']),
                                        score= db_post_record['score'],
                                        state= model_pb2.Post.PostState.POST_STATE_NORMAL,
                                        publication_date= db_post_record['publication_date']
                                         )
        
        if(db_post_record['state'] == mockDB.PostState.POST_STATE_HIDDEN):
            respond_post.state = model_pb2.Post.PostState.POST_STATE_HIDDEN
        elif(db_post_record['state'] == mockDB.PostState.POST_STATE_LOCKED):
            respond_post.state = model_pb2.Post.PostState.POST_STATE_LOCKED

        if(db_post_record['url_type'] == mockDB.UrlType.VIDEO):
            respond_post.video_url = db_post_record['url']
        elif(db_post_record['url_type'] == mockDB.UrlType.IMAGE):
            respond_post.image_url = db_post_record['url']

        return respond_post
    
    def ConstructCommentFromDBRecord(self,db_comment_record) -> dict:
        respond_comment = model_pb2.Comment(text=db_comment_record['text'],
                                            author=model_pb2.User(user_id=db_comment_record['author']),
                                            score= db_comment_record['score'],
                                            state= model_pb2.Comment.CommetState.COMMENT_STATE_NORMAL,
                                            publication_date= db_comment_record['publication_date'],
                                            reply_type= model_pb2.Comment.ReplyType.REPLY_TYPE_POST,
                                            reply_to= db_comment_record['reply_to']
                                            )
        
        if(db_comment_record['state'] == mockDB.CommentState.COMMENT_STATE_HIDDEN):
            respond_comment.state =model_pb2.Comment.CommetState.COMMENT_STATE_HIDDEN

        if(db_comment_record['reply_type'] == mockDB.ReplyType.REPLY_TYPE_COMMENT):
            respond_comment.reply_type =model_pb2.Comment.ReplyType.REPLY_TYPE_COMMENT
        
        return respond_comment


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

        respond_post = self.ConstructPostFromDBRecord(new_post_record)

        return service_pb2.CreatePostRespond(post=respond_post)
            
    def VotePost(self, request, context):
        #filter the post record in the database
        post_record = next(filter(lambda record: record['id'] == request.post_id, self.mockDB.post))

        if(request.vote):
            #upvote
            post_record['score'] += 1 
        else:
            #downvote
            post_record['score'] -= 1


        respond_post = self.ConstructPostFromDBRecord(post_record)

        return service_pb2.VotePostRespond(post=respond_post)
    
    def GetPost(self, request, context):
        #filter the post record in the database
        post_record = next(filter(lambda record: record['id'] == request.post_id, self.mockDB.post))

        respond_post = self.ConstructPostFromDBRecord(post_record)

        return service_pb2.GetPostRespond(post=respond_post)
    
    def CreateComment(self, request, context):
        #discard wrapper 
        request_comment = request.comment
            
        # check one of field for url
        replyType = mockDB.ReplyType.REPLY_TYPE_POST
        if(request_comment.reply_type == model_pb2.Comment.REPLY_TYPE_COMMENT):
            replyType = mockDB.ReplyType.REPLY_TYPE_COMMENT

        #create new DB record
        new_comment_record = {
            "id": len(self.mockDB.comment),
            "text": request_comment.text,
            "author": request_comment.author.user_id,
            "score": 0,
            "state": mockDB.CommentState.COMMENT_STATE_NORMAL,
            "publication_date": datetime.date.today().strftime("%Y-%m-%d"),
            "reply_type": request_comment.reply_type,
            "reply_to": request_comment.reply_to,
        }
        #insert into DB
        self.mockDB.comment.append(new_comment_record)

        #DEBUG
        print(self.mockDB.comment[-1])

        respond_comment = self.ConstructCommentFromDBRecord(new_comment_record)

        return service_pb2.CreateCommentRespond(comment=respond_comment)
    
    def VoteComment(self, request, context):
        #filter the post record in the database
        comment_record = next(filter(lambda record: record['id'] == request.comment_id, self.mockDB.comment))

        if(request.vote):
            #upvote
            comment_record['score'] += 1 
        else:
            #downvote
            comment_record['score'] -= 1


        respond_comment = self.ConstructCommentFromDBRecord(comment_record)

        return service_pb2.VoteCommentRespond(comment=respond_comment)
    
    def GetMostUpvoteComment(self, request, context):
        #fetch comments that is reply to a given post
        comment_records = list(filter(lambda record: record['reply_type'] == mockDB.ReplyType.REPLY_TYPE_POST and
                                     record['reply_to'] == request.post_id, self.mockDB.comment))
        #sort the comments base on its score
        comment_records = sorted(comment_records, key=lambda record: record['score'], reverse=True)

        # comment_records can has less records than mostN
        return_len = min(request.mostN, len(comment_records))
        #return the list of comment
        for i in range(return_len):
            respond_comment = self.ConstructCommentFromDBRecord(comment_records[i])
            has_reply = False
            comments_reply_to_this = list(filter(lambda record: record['reply_type'] == mockDB.ReplyType.REPLY_TYPE_COMMENT and
                                     record['reply_to'] == comment_records[i]['id'], self.mockDB.comment))
            
            if(len(comments_reply_to_this) > 0):
                has_reply = True
            yield service_pb2.MostUpvoteCommentRespond(comment=respond_comment, has_replies=has_reply)

    def ExpandReply(self, request, context):
        #fetch comments that is reply to a comment post
        comment_records = list(filter(lambda record: record['reply_type'] == mockDB.ReplyType.REPLY_TYPE_COMMENT and
                                     record['reply_to'] == request.comment_id, self.mockDB.comment))
        
        #sort the comments base on its score
        comment_records = sorted(comment_records, key=lambda record: record['score'], reverse=True)

        # comment_records can has less records than mostN
        return_len = min(request.mostN, len(comment_records))

        for i in range(return_len):
            respond_comment = self.ConstructCommentFromDBRecord(comment_records[i])
            comments_reply_to_this = list(filter(lambda record: record['reply_type'] == mockDB.ReplyType.REPLY_TYPE_COMMENT and
                                     record['reply_to'] == comment_records[i]['id'], self.mockDB.comment))
            
            respond_reply = []
            if(len(comments_reply_to_this) > 0):
                repeat_reply_len =  min(request.mostN, len(comments_reply_to_this))
                for j in range(repeat_reply_len):
                    respond_reply.append(self.ConstructCommentFromDBRecord(comments_reply_to_this[j]))
            else:
                respond_reply = None

            yield service_pb2.ExpandReplyRespond(comment=respond_comment, reply=respond_reply)