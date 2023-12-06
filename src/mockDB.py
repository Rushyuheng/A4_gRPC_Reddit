
from enum import Enum

# Define an enum for PostState
class PostState(Enum):
    POST_STATE_NORMAL = 0
    POST_STATE_LOCKED = 1
    POST_STATE_HIDDEN = 2

# Define an enum for CommentState
class CommentState(Enum):
    POST_STATE_NORMAL = 0
    POST_STATE_HIDDEN = 1

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
                "url": "https://example.com/video/5",
                "author": "rush", 
                "score": 30,
                "state": PostState.POST_STATE_NORMAL,
                "publication_date": "2005-07-08"
            }
        ]
        