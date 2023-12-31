# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import model_pb2 as model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x06reddit\x1a\x0bmodel.proto\"=\n\x11\x43reatePostRequest\x12\x1f\n\x04post\x18\x01 \x01(\x0b\x32\x0c.reddit.PostH\x00\x88\x01\x01\x42\x07\n\x05_post\"=\n\x11\x43reatePostRespond\x12\x1f\n\x04post\x18\x01 \x01(\x0b\x32\x0c.reddit.PostH\x00\x88\x01\x01\x42\x07\n\x05_post\"O\n\x0fVotePostRequest\x12\x14\n\x07post_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04vote\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\n\n\x08_post_idB\x07\n\x05_vote\";\n\x0fVotePostRespond\x12\x1f\n\x04post\x18\x01 \x01(\x0b\x32\x0c.reddit.PostH\x00\x88\x01\x01\x42\x07\n\x05_post\"2\n\x0eGetPostRequest\x12\x14\n\x07post_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\n\n\x08_post_id\":\n\x0eGetPostRespond\x12\x1f\n\x04post\x18\x01 \x01(\x0b\x32\x0c.reddit.PostH\x00\x88\x01\x01\x42\x07\n\x05_post\"I\n\x14\x43reateCommentRequest\x12%\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.CommentH\x00\x88\x01\x01\x42\n\n\x08_comment\"I\n\x14\x43reateCommentRespond\x12%\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.CommentH\x00\x88\x01\x01\x42\n\n\x08_comment\"X\n\x12VoteCommentRequest\x12\x17\n\ncomment_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04vote\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\r\n\x0b_comment_idB\x07\n\x05_vote\"G\n\x12VoteCommentRespond\x12%\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.CommentH\x00\x88\x01\x01\x42\n\n\x08_comment\"Z\n\x18MostUpvoteCommentRequest\x12\x12\n\x05mostN\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07post_id\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x08\n\x06_mostNB\n\n\x08_post_id\"w\n\x18MostUpvoteCommentRespond\x12%\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.CommentH\x00\x88\x01\x01\x12\x18\n\x0bhas_replies\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\n\n\x08_commentB\x0e\n\x0c_has_replies\"Z\n\x12\x45xpandReplyRequest\x12\x17\n\ncomment_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05mostN\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\r\n\x0b_comment_idB\x08\n\x06_mostN\"g\n\x12\x45xpandReplyRespond\x12%\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.CommentH\x00\x88\x01\x01\x12\x1e\n\x05reply\x18\x02 \x03(\x0b\x32\x0f.reddit.CommentB\n\n\x08_comment2\x8e\x04\n\x06Reddit\x12\x44\n\nCreatePost\x12\x19.reddit.CreatePostRequest\x1a\x19.reddit.CreatePostRespond\"\x00\x12>\n\x08VotePost\x12\x17.reddit.VotePostRequest\x1a\x17.reddit.VotePostRespond\"\x00\x12;\n\x07GetPost\x12\x16.reddit.GetPostRequest\x1a\x16.reddit.GetPostRespond\"\x00\x12M\n\rCreateComment\x12\x1c.reddit.CreateCommentRequest\x1a\x1c.reddit.CreateCommentRespond\"\x00\x12G\n\x0bVoteComment\x12\x1a.reddit.VoteCommentRequest\x1a\x1a.reddit.VoteCommentRespond\"\x00\x12^\n\x14GetMostUpvoteComment\x12 .reddit.MostUpvoteCommentRequest\x1a .reddit.MostUpvoteCommentRespond\"\x00\x30\x01\x12I\n\x0b\x45xpandReply\x12\x1a.reddit.ExpandReplyRequest\x1a\x1a.reddit.ExpandReplyRespond\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEPOSTREQUEST']._serialized_start=38
  _globals['_CREATEPOSTREQUEST']._serialized_end=99
  _globals['_CREATEPOSTRESPOND']._serialized_start=101
  _globals['_CREATEPOSTRESPOND']._serialized_end=162
  _globals['_VOTEPOSTREQUEST']._serialized_start=164
  _globals['_VOTEPOSTREQUEST']._serialized_end=243
  _globals['_VOTEPOSTRESPOND']._serialized_start=245
  _globals['_VOTEPOSTRESPOND']._serialized_end=304
  _globals['_GETPOSTREQUEST']._serialized_start=306
  _globals['_GETPOSTREQUEST']._serialized_end=356
  _globals['_GETPOSTRESPOND']._serialized_start=358
  _globals['_GETPOSTRESPOND']._serialized_end=416
  _globals['_CREATECOMMENTREQUEST']._serialized_start=418
  _globals['_CREATECOMMENTREQUEST']._serialized_end=491
  _globals['_CREATECOMMENTRESPOND']._serialized_start=493
  _globals['_CREATECOMMENTRESPOND']._serialized_end=566
  _globals['_VOTECOMMENTREQUEST']._serialized_start=568
  _globals['_VOTECOMMENTREQUEST']._serialized_end=656
  _globals['_VOTECOMMENTRESPOND']._serialized_start=658
  _globals['_VOTECOMMENTRESPOND']._serialized_end=729
  _globals['_MOSTUPVOTECOMMENTREQUEST']._serialized_start=731
  _globals['_MOSTUPVOTECOMMENTREQUEST']._serialized_end=821
  _globals['_MOSTUPVOTECOMMENTRESPOND']._serialized_start=823
  _globals['_MOSTUPVOTECOMMENTRESPOND']._serialized_end=942
  _globals['_EXPANDREPLYREQUEST']._serialized_start=944
  _globals['_EXPANDREPLYREQUEST']._serialized_end=1034
  _globals['_EXPANDREPLYRESPOND']._serialized_start=1036
  _globals['_EXPANDREPLYRESPOND']._serialized_end=1139
  _globals['_REDDIT']._serialized_start=1142
  _globals['_REDDIT']._serialized_end=1668
# @@protoc_insertion_point(module_scope)
