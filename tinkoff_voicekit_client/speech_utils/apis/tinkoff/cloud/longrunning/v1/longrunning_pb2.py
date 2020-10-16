# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/cloud/longrunning/v1/longrunning.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tinkoff/cloud/longrunning/v1/longrunning.proto',
  package='tinkoff.cloud.longrunning.v1',
  syntax='proto3',
  serialized_options=_b('ZHstash.tcsbank.ru/stt/tinkoff_cloud_apis/pkg/tinkoff/cloud/longrunning/v1'),
  serialized_pb=_b('\n.tinkoff/cloud/longrunning/v1/longrunning.proto\x12\x1ctinkoff.cloud.longrunning.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\"\xe4\x01\n\tOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12&\n\x08metadata\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12;\n\x05state\x18\x04 \x01(\x0e\x32,.tinkoff.cloud.longrunning.v1.OperationState\x12#\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06result\"\xbb\x02\n\x0fOperationFilter\x12\x1a\n\x10\x65xact_service_id\x18\x01 \x01(\tH\x00\x12\x30\n\x0e\x61ny_service_id\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x12\n\x08\x65xact_id\x18\x03 \x01(\tH\x01\x12(\n\x06\x61ny_id\x18\x04 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x01\x12\x15\n\x0b\x65xact_group\x18\x05 \x01(\tH\x02\x12+\n\tany_group\x18\x06 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x02\x12;\n\x05state\x18\x07 \x03(\x0e\x32,.tinkoff.cloud.longrunning.v1.OperationStateB\x0c\n\nservice_idB\x04\n\x02idB\x07\n\x05group\"!\n\x13GetOperationRequest\x12\n\n\x02id\x18\x01 \x01(\t\"N\n\x14WaitOperationRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"}\n\x15ListOperationsRequest\x12=\n\x06\x66ilter\x18\x01 \x01(\x0b\x32-.tinkoff.cloud.longrunning.v1.OperationFilter\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"n\n\x16ListOperationsResponse\x12;\n\noperations\x18\x01 \x03(\x0b\x32\'.tinkoff.cloud.longrunning.v1.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"W\n\x16\x44\x65leteOperationRequest\x12=\n\x06\x66ilter\x18\x01 \x01(\x0b\x32-.tinkoff.cloud.longrunning.v1.OperationFilter\"W\n\x16\x43\x61ncelOperationRequest\x12=\n\x06\x66ilter\x18\x01 \x01(\x0b\x32-.tinkoff.cloud.longrunning.v1.OperationFilter\"s\n\x16WatchOperationsRequest\x12=\n\x06\x66ilter\x18\x01 \x01(\x0b\x32-.tinkoff.cloud.longrunning.v1.OperationFilter\x12\x1a\n\x12listen_for_updates\x18\x02 \x01(\x08\"U\n\x16OperationsInitialState\x12;\n\noperations\x18\x01 \x03(\x0b\x32\'.tinkoff.cloud.longrunning.v1.Operation\"O\n\x10OperationsUpdate\x12;\n\noperations\x18\x01 \x03(\x0b\x32\'.tinkoff.cloud.longrunning.v1.Operation\"\xe9\x01\n\x17WatchOperationsResponse\x12M\n\rinitial_state\x18\x01 \x01(\x0b\x32\x34.tinkoff.cloud.longrunning.v1.OperationsInitialStateH\x00\x12/\n\rinit_finished\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12@\n\x06update\x18\x03 \x01(\x0b\x32..tinkoff.cloud.longrunning.v1.OperationsUpdateH\x00\x42\x0c\n\noperations*D\n\x0eOperationState\x12\x0c\n\x08\x45NQUEUED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\x08\n\x04\x44ONE\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x32\xbf\x06\n\nOperations\x12\x87\x01\n\x0cGetOperation\x12\x31.tinkoff.cloud.longrunning.v1.GetOperationRequest\x1a\'.tinkoff.cloud.longrunning.v1.Operation\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/operations/{id}\x12l\n\rWaitOperation\x12\x32.tinkoff.cloud.longrunning.v1.WaitOperationRequest\x1a\'.tinkoff.cloud.longrunning.v1.Operation\x12\x93\x01\n\x0eListOperations\x12\x33.tinkoff.cloud.longrunning.v1.ListOperationsRequest\x1a\x34.tinkoff.cloud.longrunning.v1.ListOperationsResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/operations\x12\x80\x01\n\x0fWatchOperations\x12\x34.tinkoff.cloud.longrunning.v1.WatchOperationsRequest\x1a\x35.tinkoff.cloud.longrunning.v1.WatchOperationsResponse0\x01\x12\x89\x01\n\x0f\x44\x65leteOperation\x12\x34.tinkoff.cloud.longrunning.v1.DeleteOperationRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"* /v1/operations/{filter.exact_id}\x12\x93\x01\n\x0f\x43\x61ncelOperation\x12\x34.tinkoff.cloud.longrunning.v1.CancelOperationRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\"\'/v1/operations/{filter.exact_id}:cancel:\x01*BJZHstash.tcsbank.ru/stt/tinkoff_cloud_apis/pkg/tinkoff/cloud/longrunning/v1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])

_OPERATIONSTATE = _descriptor.EnumDescriptor(
  name='OperationState',
  full_name='tinkoff.cloud.longrunning.v1.OperationState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENQUEUED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1825,
  serialized_end=1893,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONSTATE)

OperationState = enum_type_wrapper.EnumTypeWrapper(_OPERATIONSTATE)
ENQUEUED = 0
PROCESSING = 1
DONE = 2
FAILED = 3



_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='tinkoff.cloud.longrunning.v1.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tinkoff.cloud.longrunning.v1.Operation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='tinkoff.cloud.longrunning.v1.Operation.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tinkoff.cloud.longrunning.v1.Operation.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='tinkoff.cloud.longrunning.v1.Operation.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='tinkoff.cloud.longrunning.v1.Operation.error', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='tinkoff.cloud.longrunning.v1.Operation.response', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='result', full_name='tinkoff.cloud.longrunning.v1.Operation.result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=224,
  serialized_end=452,
)


_OPERATIONFILTER = _descriptor.Descriptor(
  name='OperationFilter',
  full_name='tinkoff.cloud.longrunning.v1.OperationFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exact_service_id', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.exact_service_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='any_service_id', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.any_service_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exact_id', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.exact_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='any_id', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.any_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exact_group', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.exact_group', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='any_group', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.any_group', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.state', index=6,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='service_id', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.service_id',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='id', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.id',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='group', full_name='tinkoff.cloud.longrunning.v1.OperationFilter.group',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=455,
  serialized_end=770,
)


_GETOPERATIONREQUEST = _descriptor.Descriptor(
  name='GetOperationRequest',
  full_name='tinkoff.cloud.longrunning.v1.GetOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tinkoff.cloud.longrunning.v1.GetOperationRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=805,
)


_WAITOPERATIONREQUEST = _descriptor.Descriptor(
  name='WaitOperationRequest',
  full_name='tinkoff.cloud.longrunning.v1.WaitOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tinkoff.cloud.longrunning.v1.WaitOperationRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='tinkoff.cloud.longrunning.v1.WaitOperationRequest.timeout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=807,
  serialized_end=885,
)


_LISTOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListOperationsRequest',
  full_name='tinkoff.cloud.longrunning.v1.ListOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='tinkoff.cloud.longrunning.v1.ListOperationsRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='tinkoff.cloud.longrunning.v1.ListOperationsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='tinkoff.cloud.longrunning.v1.ListOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=1012,
)


_LISTOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListOperationsResponse',
  full_name='tinkoff.cloud.longrunning.v1.ListOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='tinkoff.cloud.longrunning.v1.ListOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='tinkoff.cloud.longrunning.v1.ListOperationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1124,
)


_DELETEOPERATIONREQUEST = _descriptor.Descriptor(
  name='DeleteOperationRequest',
  full_name='tinkoff.cloud.longrunning.v1.DeleteOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='tinkoff.cloud.longrunning.v1.DeleteOperationRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1126,
  serialized_end=1213,
)


_CANCELOPERATIONREQUEST = _descriptor.Descriptor(
  name='CancelOperationRequest',
  full_name='tinkoff.cloud.longrunning.v1.CancelOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='tinkoff.cloud.longrunning.v1.CancelOperationRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1215,
  serialized_end=1302,
)


_WATCHOPERATIONSREQUEST = _descriptor.Descriptor(
  name='WatchOperationsRequest',
  full_name='tinkoff.cloud.longrunning.v1.WatchOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='tinkoff.cloud.longrunning.v1.WatchOperationsRequest.filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listen_for_updates', full_name='tinkoff.cloud.longrunning.v1.WatchOperationsRequest.listen_for_updates', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1304,
  serialized_end=1419,
)


_OPERATIONSINITIALSTATE = _descriptor.Descriptor(
  name='OperationsInitialState',
  full_name='tinkoff.cloud.longrunning.v1.OperationsInitialState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='tinkoff.cloud.longrunning.v1.OperationsInitialState.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1421,
  serialized_end=1506,
)


_OPERATIONSUPDATE = _descriptor.Descriptor(
  name='OperationsUpdate',
  full_name='tinkoff.cloud.longrunning.v1.OperationsUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='tinkoff.cloud.longrunning.v1.OperationsUpdate.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1508,
  serialized_end=1587,
)


_WATCHOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='WatchOperationsResponse',
  full_name='tinkoff.cloud.longrunning.v1.WatchOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_state', full_name='tinkoff.cloud.longrunning.v1.WatchOperationsResponse.initial_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_finished', full_name='tinkoff.cloud.longrunning.v1.WatchOperationsResponse.init_finished', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='tinkoff.cloud.longrunning.v1.WatchOperationsResponse.update', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operations', full_name='tinkoff.cloud.longrunning.v1.WatchOperationsResponse.operations',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1590,
  serialized_end=1823,
)

_OPERATION.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_OPERATION.fields_by_name['state'].enum_type = _OPERATIONSTATE
_OPERATION.fields_by_name['error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_OPERATION.fields_by_name['response'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_OPERATION.oneofs_by_name['result'].fields.append(
  _OPERATION.fields_by_name['error'])
_OPERATION.fields_by_name['error'].containing_oneof = _OPERATION.oneofs_by_name['result']
_OPERATION.oneofs_by_name['result'].fields.append(
  _OPERATION.fields_by_name['response'])
_OPERATION.fields_by_name['response'].containing_oneof = _OPERATION.oneofs_by_name['result']
_OPERATIONFILTER.fields_by_name['any_service_id'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_OPERATIONFILTER.fields_by_name['any_id'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_OPERATIONFILTER.fields_by_name['any_group'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_OPERATIONFILTER.fields_by_name['state'].enum_type = _OPERATIONSTATE
_OPERATIONFILTER.oneofs_by_name['service_id'].fields.append(
  _OPERATIONFILTER.fields_by_name['exact_service_id'])
_OPERATIONFILTER.fields_by_name['exact_service_id'].containing_oneof = _OPERATIONFILTER.oneofs_by_name['service_id']
_OPERATIONFILTER.oneofs_by_name['service_id'].fields.append(
  _OPERATIONFILTER.fields_by_name['any_service_id'])
_OPERATIONFILTER.fields_by_name['any_service_id'].containing_oneof = _OPERATIONFILTER.oneofs_by_name['service_id']
_OPERATIONFILTER.oneofs_by_name['id'].fields.append(
  _OPERATIONFILTER.fields_by_name['exact_id'])
_OPERATIONFILTER.fields_by_name['exact_id'].containing_oneof = _OPERATIONFILTER.oneofs_by_name['id']
_OPERATIONFILTER.oneofs_by_name['id'].fields.append(
  _OPERATIONFILTER.fields_by_name['any_id'])
_OPERATIONFILTER.fields_by_name['any_id'].containing_oneof = _OPERATIONFILTER.oneofs_by_name['id']
_OPERATIONFILTER.oneofs_by_name['group'].fields.append(
  _OPERATIONFILTER.fields_by_name['exact_group'])
_OPERATIONFILTER.fields_by_name['exact_group'].containing_oneof = _OPERATIONFILTER.oneofs_by_name['group']
_OPERATIONFILTER.oneofs_by_name['group'].fields.append(
  _OPERATIONFILTER.fields_by_name['any_group'])
_OPERATIONFILTER.fields_by_name['any_group'].containing_oneof = _OPERATIONFILTER.oneofs_by_name['group']
_WAITOPERATIONREQUEST.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_LISTOPERATIONSREQUEST.fields_by_name['filter'].message_type = _OPERATIONFILTER
_LISTOPERATIONSRESPONSE.fields_by_name['operations'].message_type = _OPERATION
_DELETEOPERATIONREQUEST.fields_by_name['filter'].message_type = _OPERATIONFILTER
_CANCELOPERATIONREQUEST.fields_by_name['filter'].message_type = _OPERATIONFILTER
_WATCHOPERATIONSREQUEST.fields_by_name['filter'].message_type = _OPERATIONFILTER
_OPERATIONSINITIALSTATE.fields_by_name['operations'].message_type = _OPERATION
_OPERATIONSUPDATE.fields_by_name['operations'].message_type = _OPERATION
_WATCHOPERATIONSRESPONSE.fields_by_name['initial_state'].message_type = _OPERATIONSINITIALSTATE
_WATCHOPERATIONSRESPONSE.fields_by_name['init_finished'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_WATCHOPERATIONSRESPONSE.fields_by_name['update'].message_type = _OPERATIONSUPDATE
_WATCHOPERATIONSRESPONSE.oneofs_by_name['operations'].fields.append(
  _WATCHOPERATIONSRESPONSE.fields_by_name['initial_state'])
_WATCHOPERATIONSRESPONSE.fields_by_name['initial_state'].containing_oneof = _WATCHOPERATIONSRESPONSE.oneofs_by_name['operations']
_WATCHOPERATIONSRESPONSE.oneofs_by_name['operations'].fields.append(
  _WATCHOPERATIONSRESPONSE.fields_by_name['init_finished'])
_WATCHOPERATIONSRESPONSE.fields_by_name['init_finished'].containing_oneof = _WATCHOPERATIONSRESPONSE.oneofs_by_name['operations']
_WATCHOPERATIONSRESPONSE.oneofs_by_name['operations'].fields.append(
  _WATCHOPERATIONSRESPONSE.fields_by_name['update'])
_WATCHOPERATIONSRESPONSE.fields_by_name['update'].containing_oneof = _WATCHOPERATIONSRESPONSE.oneofs_by_name['operations']
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['OperationFilter'] = _OPERATIONFILTER
DESCRIPTOR.message_types_by_name['GetOperationRequest'] = _GETOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['WaitOperationRequest'] = _WAITOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['ListOperationsRequest'] = _LISTOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListOperationsResponse'] = _LISTOPERATIONSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteOperationRequest'] = _DELETEOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['CancelOperationRequest'] = _CANCELOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['WatchOperationsRequest'] = _WATCHOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['OperationsInitialState'] = _OPERATIONSINITIALSTATE
DESCRIPTOR.message_types_by_name['OperationsUpdate'] = _OPERATIONSUPDATE
DESCRIPTOR.message_types_by_name['WatchOperationsResponse'] = _WATCHOPERATIONSRESPONSE
DESCRIPTOR.enum_types_by_name['OperationState'] = _OPERATIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.Operation)
  })
_sym_db.RegisterMessage(Operation)

OperationFilter = _reflection.GeneratedProtocolMessageType('OperationFilter', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONFILTER,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.OperationFilter)
  })
_sym_db.RegisterMessage(OperationFilter)

GetOperationRequest = _reflection.GeneratedProtocolMessageType('GetOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONREQUEST,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.GetOperationRequest)
  })
_sym_db.RegisterMessage(GetOperationRequest)

WaitOperationRequest = _reflection.GeneratedProtocolMessageType('WaitOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _WAITOPERATIONREQUEST,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.WaitOperationRequest)
  })
_sym_db.RegisterMessage(WaitOperationRequest)

ListOperationsRequest = _reflection.GeneratedProtocolMessageType('ListOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSREQUEST,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.ListOperationsRequest)
  })
_sym_db.RegisterMessage(ListOperationsRequest)

ListOperationsResponse = _reflection.GeneratedProtocolMessageType('ListOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSRESPONSE,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.ListOperationsResponse)
  })
_sym_db.RegisterMessage(ListOperationsResponse)

DeleteOperationRequest = _reflection.GeneratedProtocolMessageType('DeleteOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOPERATIONREQUEST,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.DeleteOperationRequest)
  })
_sym_db.RegisterMessage(DeleteOperationRequest)

CancelOperationRequest = _reflection.GeneratedProtocolMessageType('CancelOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELOPERATIONREQUEST,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.CancelOperationRequest)
  })
_sym_db.RegisterMessage(CancelOperationRequest)

WatchOperationsRequest = _reflection.GeneratedProtocolMessageType('WatchOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHOPERATIONSREQUEST,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.WatchOperationsRequest)
  })
_sym_db.RegisterMessage(WatchOperationsRequest)

OperationsInitialState = _reflection.GeneratedProtocolMessageType('OperationsInitialState', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONSINITIALSTATE,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.OperationsInitialState)
  })
_sym_db.RegisterMessage(OperationsInitialState)

OperationsUpdate = _reflection.GeneratedProtocolMessageType('OperationsUpdate', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONSUPDATE,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.OperationsUpdate)
  })
_sym_db.RegisterMessage(OperationsUpdate)

WatchOperationsResponse = _reflection.GeneratedProtocolMessageType('WatchOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _WATCHOPERATIONSRESPONSE,
  '__module__' : 'tinkoff.cloud.longrunning.v1.longrunning_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.cloud.longrunning.v1.WatchOperationsResponse)
  })
_sym_db.RegisterMessage(WatchOperationsResponse)


DESCRIPTOR._options = None

_OPERATIONS = _descriptor.ServiceDescriptor(
  name='Operations',
  full_name='tinkoff.cloud.longrunning.v1.Operations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1896,
  serialized_end=2727,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOperation',
    full_name='tinkoff.cloud.longrunning.v1.Operations.GetOperation',
    index=0,
    containing_service=None,
    input_type=_GETOPERATIONREQUEST,
    output_type=_OPERATION,
    serialized_options=_b('\202\323\344\223\002\025\022\023/v1/operations/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='WaitOperation',
    full_name='tinkoff.cloud.longrunning.v1.Operations.WaitOperation',
    index=1,
    containing_service=None,
    input_type=_WAITOPERATIONREQUEST,
    output_type=_OPERATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='tinkoff.cloud.longrunning.v1.Operations.ListOperations',
    index=2,
    containing_service=None,
    input_type=_LISTOPERATIONSREQUEST,
    output_type=_LISTOPERATIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/operations'),
  ),
  _descriptor.MethodDescriptor(
    name='WatchOperations',
    full_name='tinkoff.cloud.longrunning.v1.Operations.WatchOperations',
    index=3,
    containing_service=None,
    input_type=_WATCHOPERATIONSREQUEST,
    output_type=_WATCHOPERATIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteOperation',
    full_name='tinkoff.cloud.longrunning.v1.Operations.DeleteOperation',
    index=4,
    containing_service=None,
    input_type=_DELETEOPERATIONREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002\"* /v1/operations/{filter.exact_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='CancelOperation',
    full_name='tinkoff.cloud.longrunning.v1.Operations.CancelOperation',
    index=5,
    containing_service=None,
    input_type=_CANCELOPERATIONREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\202\323\344\223\002,\"\'/v1/operations/{filter.exact_id}:cancel:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_OPERATIONS)

DESCRIPTOR.services_by_name['Operations'] = _OPERATIONS

# @@protoc_insertion_point(module_scope)
