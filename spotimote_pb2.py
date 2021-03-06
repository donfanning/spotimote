# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spotimote.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spotimote.proto',
  package='spotimote',
  serialized_pb=_b('\n\x0fspotimote.proto\x12\tspotimote\"\xcd\x01\n\tActionMsg\x12/\n\x08\x61\x63tionId\x18\x01 \x02(\x0e\x32\x1d.spotimote.ActionMsg.ActionId\"\x8e\x01\n\x08\x41\x63tionId\x12\x13\n\x0f\x41\x63tionPlayPause\x10\x01\x12\x0e\n\nActionNext\x10\x02\x12\x0e\n\nActionPrev\x10\x03\x12\x11\n\rActionShuffle\x10\x04\x12\x10\n\x0c\x41\x63tionRepeat\x10\x05\x12\x12\n\x0e\x41\x63tionVolumeUp\x10\x06\x12\x14\n\x10\x41\x63tionVolumeDown\x10\x07\"(\n\x0c\x42roadcastMsg\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x02(\x05\"D\n\x0e\x42roadcastReply\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\n\n\x02ip\x18\x03 \x02(\t\x12\x0c\n\x04port\x18\x04 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ACTIONMSG_ACTIONID = _descriptor.EnumDescriptor(
  name='ActionId',
  full_name='spotimote.ActionMsg.ActionId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ActionPlayPause', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionNext', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionPrev', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionShuffle', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionRepeat', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionVolumeUp', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActionVolumeDown', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=94,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_ACTIONMSG_ACTIONID)


_ACTIONMSG = _descriptor.Descriptor(
  name='ActionMsg',
  full_name='spotimote.ActionMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionId', full_name='spotimote.ActionMsg.actionId', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACTIONMSG_ACTIONID,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=236,
)


_BROADCASTMSG = _descriptor.Descriptor(
  name='BroadcastMsg',
  full_name='spotimote.BroadcastMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='spotimote.BroadcastMsg.ip', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='spotimote.BroadcastMsg.port', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=278,
)


_BROADCASTREPLY = _descriptor.Descriptor(
  name='BroadcastReply',
  full_name='spotimote.BroadcastReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='spotimote.BroadcastReply.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='spotimote.BroadcastReply.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='spotimote.BroadcastReply.ip', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='spotimote.BroadcastReply.port', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=348,
)

_ACTIONMSG.fields_by_name['actionId'].enum_type = _ACTIONMSG_ACTIONID
_ACTIONMSG_ACTIONID.containing_type = _ACTIONMSG
DESCRIPTOR.message_types_by_name['ActionMsg'] = _ACTIONMSG
DESCRIPTOR.message_types_by_name['BroadcastMsg'] = _BROADCASTMSG
DESCRIPTOR.message_types_by_name['BroadcastReply'] = _BROADCASTREPLY

ActionMsg = _reflection.GeneratedProtocolMessageType('ActionMsg', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONMSG,
  __module__ = 'spotimote_pb2'
  # @@protoc_insertion_point(class_scope:spotimote.ActionMsg)
  ))
_sym_db.RegisterMessage(ActionMsg)

BroadcastMsg = _reflection.GeneratedProtocolMessageType('BroadcastMsg', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTMSG,
  __module__ = 'spotimote_pb2'
  # @@protoc_insertion_point(class_scope:spotimote.BroadcastMsg)
  ))
_sym_db.RegisterMessage(BroadcastMsg)

BroadcastReply = _reflection.GeneratedProtocolMessageType('BroadcastReply', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTREPLY,
  __module__ = 'spotimote_pb2'
  # @@protoc_insertion_point(class_scope:spotimote.BroadcastReply)
  ))
_sym_db.RegisterMessage(BroadcastReply)


# @@protoc_insertion_point(module_scope)
