# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jacobs_grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11jacobs_grpc.proto\x12\x0cjacobs_proto\"5\n\x0fmessage_request\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\trequester\x18\x02 \x01(\t\"3\n\x10message_response\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t2a\n\x0ejacobs_service\x12O\n\x0ctest_message\x12\x1d.jacobs_proto.message_request\x1a\x1e.jacobs_proto.message_response\"\x00\x62\x06proto3')



_MESSAGE_REQUEST = DESCRIPTOR.message_types_by_name['message_request']
_MESSAGE_RESPONSE = DESCRIPTOR.message_types_by_name['message_response']
message_request = _reflection.GeneratedProtocolMessageType('message_request', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE_REQUEST,
  '__module__' : 'jacobs_grpc_pb2'
  # @@protoc_insertion_point(class_scope:jacobs_proto.message_request)
  })
_sym_db.RegisterMessage(message_request)

message_response = _reflection.GeneratedProtocolMessageType('message_response', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE_RESPONSE,
  '__module__' : 'jacobs_grpc_pb2'
  # @@protoc_insertion_point(class_scope:jacobs_proto.message_response)
  })
_sym_db.RegisterMessage(message_response)

_JACOBS_SERVICE = DESCRIPTOR.services_by_name['jacobs_service']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE_REQUEST._serialized_start=35
  _MESSAGE_REQUEST._serialized_end=88
  _MESSAGE_RESPONSE._serialized_start=90
  _MESSAGE_RESPONSE._serialized_end=141
  _JACOBS_SERVICE._serialized_start=143
  _JACOBS_SERVICE._serialized_end=240
# @@protoc_insertion_point(module_scope)
