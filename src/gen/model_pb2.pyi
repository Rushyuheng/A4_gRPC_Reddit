from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ["post_id", "title", "text", "video_url", "image_url", "author", "score", "state", "publication_date"]
    class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        POST_STATE_NORMAL: _ClassVar[Post.PostState]
        POST_STATE_LOCKED: _ClassVar[Post.PostState]
        POST_STATE_HIDDEN: _ClassVar[Post.PostState]
    POST_STATE_NORMAL: Post.PostState
    POST_STATE_LOCKED: Post.PostState
    POST_STATE_HIDDEN: Post.PostState
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    title: str
    text: str
    video_url: str
    image_url: str
    author: User
    score: int
    state: Post.PostState
    publication_date: str
    def __init__(self, post_id: _Optional[int] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Post.PostState, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["comment_id", "text", "author", "score", "state", "publication_date", "reply_type", "reply_to"]
    class CommetState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        COMMENT_STATE_NORMAL: _ClassVar[Comment.CommetState]
        COMMENT_STATE_HIDDEN: _ClassVar[Comment.CommetState]
    COMMENT_STATE_NORMAL: Comment.CommetState
    COMMENT_STATE_HIDDEN: Comment.CommetState
    class ReplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        REPLY_TYPE_POST: _ClassVar[Comment.ReplyType]
        REPLY_TYPE_COMMENT: _ClassVar[Comment.ReplyType]
    REPLY_TYPE_POST: Comment.ReplyType
    REPLY_TYPE_COMMENT: Comment.ReplyType
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    text: str
    author: User
    score: int
    state: Comment.CommetState
    publication_date: str
    reply_type: Comment.ReplyType
    reply_to: int
    def __init__(self, comment_id: _Optional[int] = ..., text: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Comment.CommetState, str]] = ..., publication_date: _Optional[str] = ..., reply_type: _Optional[_Union[Comment.ReplyType, str]] = ..., reply_to: _Optional[int] = ...) -> None: ...
