# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message_dict.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message_dict.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12message_dict.proto\"\x81\x03\n\x04\x44ict\x12\x0b\n\x03int\x18\x01 \x01(\x05\x12\r\n\x05\x66loat\x18\x02 \x01(\x02\x12\x0e\n\x06string\x18\x03 \x01(\t\x12\x11\n\tarray_int\x18\x04 \x03(\x05\x12\x13\n\x0b\x61rray_float\x18\x05 \x03(\x02\x12\x14\n\x0c\x61rray_string\x18\x06 \x03(\t\x12$\n\x08\x64ict_int\x18\x07 \x03(\x0b\x32\x12.Dict.DictIntEntry\x12(\n\ndict_float\x18\x08 \x03(\x0b\x32\x14.Dict.DictFloatEntry\x12*\n\x0b\x64ict_string\x18\t \x03(\x0b\x32\x15.Dict.DictStringEntry\x1a.\n\x0c\x44ictIntEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x30\n\x0e\x44ictFloatEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x31\n\x0f\x44ictStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')
)




_DICT_DICTINTENTRY = _descriptor.Descriptor(
  name='DictIntEntry',
  full_name='Dict.DictIntEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Dict.DictIntEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dict.DictIntEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=307,
)

_DICT_DICTFLOATENTRY = _descriptor.Descriptor(
  name='DictFloatEntry',
  full_name='Dict.DictFloatEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Dict.DictFloatEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dict.DictFloatEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=357,
)

_DICT_DICTSTRINGENTRY = _descriptor.Descriptor(
  name='DictStringEntry',
  full_name='Dict.DictStringEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Dict.DictStringEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dict.DictStringEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=408,
)

_DICT = _descriptor.Descriptor(
  name='Dict',
  full_name='Dict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int', full_name='Dict.int', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float', full_name='Dict.float', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='Dict.string', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array_int', full_name='Dict.array_int', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array_float', full_name='Dict.array_float', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array_string', full_name='Dict.array_string', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dict_int', full_name='Dict.dict_int', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dict_float', full_name='Dict.dict_float', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dict_string', full_name='Dict.dict_string', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DICT_DICTINTENTRY, _DICT_DICTFLOATENTRY, _DICT_DICTSTRINGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=408,
)

_DICT_DICTINTENTRY.containing_type = _DICT
_DICT_DICTFLOATENTRY.containing_type = _DICT
_DICT_DICTSTRINGENTRY.containing_type = _DICT
_DICT.fields_by_name['dict_int'].message_type = _DICT_DICTINTENTRY
_DICT.fields_by_name['dict_float'].message_type = _DICT_DICTFLOATENTRY
_DICT.fields_by_name['dict_string'].message_type = _DICT_DICTSTRINGENTRY
DESCRIPTOR.message_types_by_name['Dict'] = _DICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dict = _reflection.GeneratedProtocolMessageType('Dict', (_message.Message,), dict(

  DictIntEntry = _reflection.GeneratedProtocolMessageType('DictIntEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICT_DICTINTENTRY,
    __module__ = 'message_dict_pb2'
    # @@protoc_insertion_point(class_scope:Dict.DictIntEntry)
    ))
  ,

  DictFloatEntry = _reflection.GeneratedProtocolMessageType('DictFloatEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICT_DICTFLOATENTRY,
    __module__ = 'message_dict_pb2'
    # @@protoc_insertion_point(class_scope:Dict.DictFloatEntry)
    ))
  ,

  DictStringEntry = _reflection.GeneratedProtocolMessageType('DictStringEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICT_DICTSTRINGENTRY,
    __module__ = 'message_dict_pb2'
    # @@protoc_insertion_point(class_scope:Dict.DictStringEntry)
    ))
  ,
  DESCRIPTOR = _DICT,
  __module__ = 'message_dict_pb2'
  # @@protoc_insertion_point(class_scope:Dict)
  ))
_sym_db.RegisterMessage(Dict)
_sym_db.RegisterMessage(Dict.DictIntEntry)
_sym_db.RegisterMessage(Dict.DictFloatEntry)
_sym_db.RegisterMessage(Dict.DictStringEntry)


_DICT_DICTINTENTRY._options = None
_DICT_DICTFLOATENTRY._options = None
_DICT_DICTSTRINGENTRY._options = None
# @@protoc_insertion_point(module_scope)