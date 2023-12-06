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
    __slots__ = ["title", "text", "video_url", "image_url", "author", "score", "state", "publication_date"]
    class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        POST_STATE_NORMAL: _ClassVar[Post.PostState]
        POST_STATE_LOCKED: _ClassVar[Post.PostState]
        POST_STATE_HIDDEN: _ClassVar[Post.PostState]
    POST_STATE_NORMAL: Post.PostState
    POST_STATE_LOCKED: Post.PostState
    POST_STATE_HIDDEN: Post.PostState
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author: User
    score: int
    state: Post.PostState
    publication_date: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Post.PostState, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["text", "author", "score", "state", "publication_date"]
    class CommetState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        POST_STATE_NORMAL: _ClassVar[Comment.CommetState]
        POST_STATE_HIDDEN: _ClassVar[Comment.CommetState]
    POST_STATE_NORMAL: Comment.CommetState
    POST_STATE_HIDDEN: Comment.CommetState
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    text: str
    author: User
    score: int
    state: Comment.CommetState
    publication_date: str
    def __init__(self, text: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Comment.CommetState, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...
