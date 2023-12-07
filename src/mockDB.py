
from enum import Enum

# Define an enum for PostState
class PostState(Enum):
    POST_STATE_NORMAL = 0
    POST_STATE_LOCKED = 1
    POST_STATE_HIDDEN = 2

# Define an enum for CommentState
class CommentState(Enum):
    COMMENT_STATE_NORMAL = 0
    COMMENT_STATE_HIDDEN = 1

# Define an enum for UrlType
class UrlType(Enum):
    VIDEO = 0
    IMAGE = 1

# Define an enum for ReplyType
class ReplyType(Enum):
    REPLY_TYPE_POST = 0
    REPLY_TYPE_COMMENT = 1

class mockDB:
    def __init__(self) -> None:
        self.users = [
            {
                "user_id":"rush"
            },
            {
                "user_id":"james"
            },
            {
                "user_id":"coco"
            },
        ]

        self.post = [
            {
                "id":0,
                "title": "Title 1",
                "text": "Text for post 1",
                "url_type": UrlType.VIDEO,
                "url": "https://example.com/video/1",
                "author": "rush", 
                "score": 0,
                "state": PostState.POST_STATE_NORMAL,
                "publication_date": "2003-02-11"
            },
            {
                "id":1,
                "title": "Title 2",
                "text": "Text for post 2",
                "url_type": UrlType.IMAGE,
                "url": "https://example.com/image/2",
                "author": "james", 
                "score": -10,
                "state": PostState.POST_STATE_NORMAL,
                "publication_date": "2023-12-06"
            },
            {
                "id":2,
                "title": "Title 3",
                "text": "Text for post 3",
                "url_type": UrlType.VIDEO,
                "url": "https://example.com/video/3",
                "author": "james", 
                "score": 25,
                "state": PostState.POST_STATE_HIDDEN,
                "publication_date": "2023-11-25"
            },
            {
                "id":3,
                "title": "Title 4",
                "text": "Text for post 4",
                "url_type": UrlType.IMAGE,
                "url": "https://example.com/image/4",
                "author": "coco", 
                "score": -9,
                "state": PostState.POST_STATE_LOCKED,
                "publication_date": "2022-03-16"
            },
            {
                "id":4,
                "title": "Title 5",
                "text": "Text for post 5",
                "url_type": UrlType.VIDEO,
                "url": "https://example.com/video/5",
                "author": "rush", 
                "score": 30,
                "state": PostState.POST_STATE_NORMAL,
                "publication_date": "2005-07-08"
            }
        ]
        
        self.commet = [
            {
                "id":0,
                "text": "what the heck is this",
                "author": "rush", 
                "score": 12,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2014-08-01",
                "replyType": ReplyType.REPLY_TYPE_POST,
                "replyTo": 0,
            },
            {
                "id":1,
                "text": "not fun",
                "author": "james", 
                "score": -3,
                "state": CommentState.COMMENT_STATE_HIDDEN,
                "publication_date": "1999-07-09",
                "replyType": ReplyType.REPLY_TYPE_POST,
                "replyTo": 0,
            },
            {
                "id":2,
                "text": "love the post",
                "author": "coco", 
                "score": 32,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2012-03-25",
                "replyType": ReplyType.REPLY_TYPE_POST,
                "replyTo": 1,
            },
            {
                "id": 3,
                "text": "Great content!",
                "author": "rush",
                "score": 25,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2020-05-12",
                "replyType": ReplyType.REPLY_TYPE_POST,
                "replyTo": 0,
            },
            {
                "id": 4,
                "text": "Disagree strongly.",
                "author": "james",
                "score": -10,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2018-11-30",
                "replyType": ReplyType.REPLY_TYPE_POST,
                "replyTo": 0,
            },
            {
                "id": 5,
                "text": "Interesting perspective!",
                "author": "coco",
                "score": 18,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2021-09-28",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 3,
            },
            {
                "id": 6,
                "text": "I've seen better.",
                "author": "rush",
                "score": -5,
                "state": CommentState.COMMENT_STATE_HIDDEN,
                "publication_date": "2017-06-20",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 4,
            },
            {
                "id": 7,
                "text": "This needs improvement.",
                "author": "james",
                "score": 7,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2019-04-15",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 4,
            },
            {
                "id": 8,
                "text": "Fantastic job!",
                "author": "coco",
                "score": 40,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2022-11-05",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 4,
            },
            {
                "id": 9,
                "text": "Hilarious!",
                "author": "rush",
                "score": 15,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2023-01-18",
                "replyType": ReplyType.POST,
                "replyTo": 2,
            },
            {
                "id": 10,
                "text": "not fun",
                "author": "james",
                "score": -3,
                "state": CommentState.COMMENT_STATE_HIDDEN,
                "publication_date": "1999-07-09",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 0,
            },
            {
                "id": 11,
                "text": "love the post",
                "author": "coco",
                "score": 32,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2012-03-25",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 1,
            },
            {
                "id": 12,
                "text": "what the heck is this",
                "author": "rush",
                "score": 12,
                "state": CommentState.COMMENT_STATE_NORMAL,
                "publication_date": "2014-08-01",
                "replyType": ReplyType.REPLY_TYPE_COMMENT,
                "replyTo": 0,
            },
        ]


        