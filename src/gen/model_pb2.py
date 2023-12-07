# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmodel.proto\x12\x06reddit\"(\n\x04User\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_user_id\"\xf9\x02\n\x04Post\x12\x12\n\x05title\x18\x01 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04text\x18\x02 \x01(\tH\x02\x88\x01\x01\x12\x13\n\tvideo_url\x18\x03 \x01(\tH\x00\x12\x13\n\timage_url\x18\x04 \x01(\tH\x00\x12!\n\x06\x61uthor\x18\x05 \x01(\x0b\x32\x0c.reddit.UserH\x03\x88\x01\x01\x12\x12\n\x05score\x18\x06 \x01(\x05H\x04\x88\x01\x01\x12*\n\x05state\x18\x07 \x01(\x0e\x32\x16.reddit.Post.PostStateH\x05\x88\x01\x01\x12\x1d\n\x10publication_date\x18\x08 \x01(\tH\x06\x88\x01\x01\"P\n\tPostState\x12\x15\n\x11POST_STATE_NORMAL\x10\x00\x12\x15\n\x11POST_STATE_LOCKED\x10\x01\x12\x15\n\x11POST_STATE_HIDDEN\x10\x02\x42\x05\n\x03urlB\x08\n\x06_titleB\x07\n\x05_textB\t\n\x07_authorB\x08\n\x06_scoreB\x08\n\x06_stateB\x13\n\x11_publication_date\"\xff\x02\n\x07\x43omment\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12!\n\x06\x61uthor\x18\x02 \x01(\x0b\x32\x0c.reddit.UserH\x01\x88\x01\x01\x12\x12\n\x05score\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12/\n\x05state\x18\x04 \x01(\x0e\x32\x1b.reddit.Comment.CommetStateH\x03\x88\x01\x01\x12\x1d\n\x10publication_date\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07replyTo\x18\x06 \x01(\x05H\x05\x88\x01\x01\"A\n\x0b\x43ommetState\x12\x18\n\x14\x43OMMENT_STATE_NORMAL\x10\x00\x12\x18\n\x14\x43OMMENT_STATE_HIDDEN\x10\x01\"8\n\tReplyType\x12\x13\n\x0fREPLY_TYPE_POST\x10\x00\x12\x16\n\x12REPLY_TYPE_COMMENT\x10\x01\x42\x07\n\x05_textB\t\n\x07_authorB\x08\n\x06_scoreB\x08\n\x06_stateB\x13\n\x11_publication_dateB\n\n\x08_replyTob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=23
  _globals['_USER']._serialized_end=63
  _globals['_POST']._serialized_start=66
  _globals['_POST']._serialized_end=443
  _globals['_POST_POSTSTATE']._serialized_start=285
  _globals['_POST_POSTSTATE']._serialized_end=365
  _globals['_COMMENT']._serialized_start=446
  _globals['_COMMENT']._serialized_end=829
  _globals['_COMMENT_COMMETSTATE']._serialized_start=633
  _globals['_COMMENT_COMMETSTATE']._serialized_end=698
  _globals['_COMMENT_REPLYTYPE']._serialized_start=700
  _globals['_COMMENT_REPLYTYPE']._serialized_end=756
# @@protoc_insertion_point(module_scope)
