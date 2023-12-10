import grpc
from gen import service_pb2_grpc
from gen import service_pb2
from gen import model_pb2
import mock_db
import datetime


class RedditServicer(service_pb2_grpc.RedditServicer):
    """Provides methods that implement functionality of route guide server."""
    def __init__(self) -> None:
        #start a new mock DB
        self.mock_db = mock_db.MockDB()

    @staticmethod
    def construct_post_from_dbrecord(db_post_record) -> dict:


        respond_post = model_pb2.Post(post_id=db_post_record['id'],
                                        title=db_post_record['title'],
                                        text=db_post_record['text'],
                                        author=model_pb2.User(user_id=db_post_record['author']),
                                        score= db_post_record['score'],
                                        state= model_pb2.Post.PostState.POST_STATE_NORMAL,
                                        publication_date= db_post_record['publication_date']
                                         )
        
        if(db_post_record['state'] == mock_db.PostState.POST_STATE_HIDDEN):
            respond_post.state = model_pb2.Post.PostState.POST_STATE_HIDDEN
        elif(db_post_record['state'] == mock_db.PostState.POST_STATE_LOCKED):
            respond_post.state = model_pb2.Post.PostState.POST_STATE_LOCKED

        if(db_post_record['url_type'] == mock_db.UrlType.VIDEO):
            respond_post.video_url = db_post_record['url']
        elif(db_post_record['url_type'] == mock_db.UrlType.IMAGE):
            respond_post.image_url = db_post_record['url']

        return respond_post
    
    @staticmethod
    def construct_comment_from_dbrecord(db_comment_record) -> dict:
        respond_comment = model_pb2.Comment(comment_id= db_comment_record['id'],
                                            text=db_comment_record['text'],
                                            author=model_pb2.User(user_id=db_comment_record['author']),
                                            score= db_comment_record['score'],
                                            state= model_pb2.Comment.CommetState.COMMENT_STATE_NORMAL,
                                            publication_date= db_comment_record['publication_date'],
                                            reply_type= model_pb2.Comment.ReplyType.REPLY_TYPE_POST,
                                            reply_to= db_comment_record['reply_to']
                                            )
        
        if(db_comment_record['state'] == mock_db.CommentState.COMMENT_STATE_HIDDEN):
            respond_comment.state =model_pb2.Comment.CommetState.COMMENT_STATE_HIDDEN

        if(db_comment_record['reply_type'] == mock_db.ReplyType.REPLY_TYPE_COMMENT):
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
            url_type = mock_db.UrlType.VIDEO
        elif(request_post.HasField("image_url")):
            url =  request_post.image_url
            url_type = mock_db.UrlType.IMAGE

        #create new DB record
        new_post_record = {
            "id": len(self.mock_db.post),
            "title": request_post.title,
            "text": request_post.text,
            "url_type": url_type,
            "url": url,
            "author": request_post.author.user_id, 
            "score": 0,
            "state": mock_db.PostState.POST_STATE_NORMAL,
            "publication_date": datetime.date.today().strftime("%Y-%m-%d")
        }
        #insert into DB
        self.mock_db.post.append(new_post_record)

        #DEBUG
        print(self.mock_db.post[-1])

        respond_post = self.construct_post_from_dbrecord(new_post_record)

        return service_pb2.CreatePostRespond(post=respond_post)
            
    def VotePost(self, request, context):
        #filter the post record in the database
        post_record = next(filter(lambda record: record['id'] == request.post_id, self.mock_db.post))

        if(request.vote):
            #upvote
            post_record['score'] += 1 
        else:
            #downvote
            post_record['score'] -= 1


        respond_post = self.construct_post_from_dbrecord(post_record)

        return service_pb2.VotePostRespond(post=respond_post)
    
    def GetPost(self, request, context):
        #filter the post record in the database
        post_record = next(filter(lambda record: record['id'] == request.post_id, self.mock_db.post))

        respond_post = self.construct_post_from_dbrecord(post_record)

        return service_pb2.GetPostRespond(post=respond_post)
    
    def CreateComment(self, request, context):
        #discard wrapper 
        request_comment = request.comment
            
        # check one of field for url
        replyType = mock_db.ReplyType.REPLY_TYPE_POST
        if(request_comment.reply_type == model_pb2.Comment.REPLY_TYPE_COMMENT):
            replyType = mock_db.ReplyType.REPLY_TYPE_COMMENT

        #create new DB record
        new_comment_record = {
            "id": len(self.mock_db.comment),
            "text": request_comment.text,
            "author": request_comment.author.user_id,
            "score": 0,
            "state": mock_db.CommentState.COMMENT_STATE_NORMAL,
            "publication_date": datetime.date.today().strftime("%Y-%m-%d"),
            "reply_type": request_comment.reply_type,
            "reply_to": request_comment.reply_to,
        }
        #insert into DB
        self.mock_db.comment.append(new_comment_record)

        #DEBUG
        print(self.mock_db.comment[-1])

        respond_comment = self.construct_comment_from_dbrecord(new_comment_record)

        return service_pb2.CreateCommentRespond(comment=respond_comment)
    
    def VoteComment(self, request, context):
        #filter the post record in the database
        comment_record = next(filter(lambda record: record['id'] == request.comment_id, self.mock_db.comment))

        if(request.vote):
            #upvote
            comment_record['score'] += 1 
        else:
            #downvote
            comment_record['score'] -= 1


        respond_comment = self.construct_comment_from_dbrecord(comment_record)

        return service_pb2.VoteCommentRespond(comment=respond_comment)
    
    def GetMostUpvoteComment(self, request, context):
        #fetch comments that is reply to a given post
        comment_records = list(filter(lambda record: record['reply_type'] == mock_db.ReplyType.REPLY_TYPE_POST and
                                     record['reply_to'] == request.post_id, self.mock_db.comment))
        #sort the comments base on its score
        comment_records = sorted(comment_records, key=lambda record: record['score'], reverse=True)

        # comment_records can has less records than mostN
        return_len = min(request.mostN, len(comment_records))
        #return the list of comment
        for i in range(return_len):
            respond_comment = self.construct_comment_from_dbrecord(comment_records[i])
            has_reply = False
            comments_reply_to_this = list(filter(lambda record: record['reply_type'] == mock_db.ReplyType.REPLY_TYPE_COMMENT and
                                     record['reply_to'] == comment_records[i]['id'], self.mock_db.comment))
            
            if(len(comments_reply_to_this) > 0):
                has_reply = True
            yield service_pb2.MostUpvoteCommentRespond(comment=respond_comment, has_replies=has_reply)

    def ExpandReply(self, request, context):
        #fetch comments that is reply to a comment post
        comment_records = list(filter(lambda record: record['reply_type'] == mock_db.ReplyType.REPLY_TYPE_COMMENT and
                                     record['reply_to'] == request.comment_id, self.mock_db.comment))
        
        #sort the comments base on its score
        comment_records = sorted(comment_records, key=lambda record: record['score'], reverse=True)

        # comment_records can has less records than mostN
        return_len = min(request.mostN, len(comment_records))

        for i in range(return_len):
            respond_comment = self.construct_comment_from_dbrecord(comment_records[i])
            comments_reply_to_this = list(filter(lambda record: record['reply_type'] == mock_db.ReplyType.REPLY_TYPE_COMMENT and
                                     record['reply_to'] == comment_records[i]['id'], self.mock_db.comment))
            
            respond_reply = []
            if(len(comments_reply_to_this) > 0):
                repeat_reply_len =  min(request.mostN, len(comments_reply_to_this))
                for j in range(repeat_reply_len):
                    respond_reply.append(self.construct_comment_from_dbrecord(comments_reply_to_this[j]))
            else:
                respond_reply = None

            yield service_pb2.ExpandReplyRespond(comment=respond_comment, reply=respond_reply)