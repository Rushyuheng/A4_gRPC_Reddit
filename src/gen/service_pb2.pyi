import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePostRequest(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _model_pb2.Post
    def __init__(self, post: _Optional[_Union[_model_pb2.Post, _Mapping]] = ...) -> None: ...

class CreatePostRespond(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _model_pb2.Post
    def __init__(self, post: _Optional[_Union[_model_pb2.Post, _Mapping]] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ["post_id", "vote"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    vote: bool
    def __init__(self, post_id: _Optional[int] = ..., vote: bool = ...) -> None: ...

class VotePostRespond(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _model_pb2.Post
    def __init__(self, post: _Optional[_Union[_model_pb2.Post, _Mapping]] = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class GetPostRespond(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _model_pb2.Post
    def __init__(self, post: _Optional[_Union[_model_pb2.Post, _Mapping]] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _model_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_model_pb2.Comment, _Mapping]] = ...) -> None: ...

class CreateCommentRespond(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _model_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_model_pb2.Comment, _Mapping]] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ["comment_id", "vote"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    vote: bool
    def __init__(self, comment_id: _Optional[int] = ..., vote: bool = ...) -> None: ...

class VoteCommentRespond(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _model_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_model_pb2.Comment, _Mapping]] = ...) -> None: ...

class MostUpvoteCommentRequest(_message.Message):
    __slots__ = ["mostN", "post_id"]
    MOSTN_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    mostN: int
    post_id: int
    def __init__(self, mostN: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class MostUpvoteCommentRespond(_message.Message):
    __slots__ = ["comment", "has_replies"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
    comment: _model_pb2.Comment
    has_replies: bool
    def __init__(self, comment: _Optional[_Union[_model_pb2.Comment, _Mapping]] = ..., has_replies: bool = ...) -> None: ...

class ExpandReplyRequest(_message.Message):
    __slots__ = ["comment_id", "mostN"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MOSTN_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    mostN: int
    def __init__(self, comment_id: _Optional[int] = ..., mostN: _Optional[int] = ...) -> None: ...

class ExpandReplyRespond(_message.Message):
    __slots__ = ["comment", "reply"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    comment: _model_pb2.Comment
    reply: _containers.RepeatedCompositeFieldContainer[_model_pb2.Comment]
    def __init__(self, comment: _Optional[_Union[_model_pb2.Comment, _Mapping]] = ..., reply: _Optional[_Iterable[_Union[_model_pb2.Comment, _Mapping]]] = ...) -> None: ...
