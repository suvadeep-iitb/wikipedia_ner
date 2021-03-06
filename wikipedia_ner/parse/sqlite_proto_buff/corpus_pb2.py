# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corpus.proto

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
  name='corpus.proto',
  package='',
  serialized_pb=_b('\n\x0c\x63orpus.proto\"c\n\x07\x45xample\x12\r\n\x05words\x18\x01 \x03(\t\x12!\n\x07trigger\x18\x02 \x03(\x0b\x32\x10.Example.Trigger\x1a&\n\x07Trigger\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07trigger\x18\x02 \x02(\t\"#\n\x06\x43orpus\x12\x19\n\x07\x65xample\x18\x01 \x03(\x0b\x32\x08.Example')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXAMPLE_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='Example.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Example.Trigger.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='Example.Trigger.trigger', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=77,
  serialized_end=115,
)

_EXAMPLE = _descriptor.Descriptor(
  name='Example',
  full_name='Example',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='Example.words', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='Example.trigger', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EXAMPLE_TRIGGER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=115,
)


_CORPUS = _descriptor.Descriptor(
  name='Corpus',
  full_name='Corpus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='example', full_name='Corpus.example', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=117,
  serialized_end=152,
)

_EXAMPLE_TRIGGER.containing_type = _EXAMPLE
_EXAMPLE.fields_by_name['trigger'].message_type = _EXAMPLE_TRIGGER
_CORPUS.fields_by_name['example'].message_type = _EXAMPLE
DESCRIPTOR.message_types_by_name['Example'] = _EXAMPLE
DESCRIPTOR.message_types_by_name['Corpus'] = _CORPUS

Example = _reflection.GeneratedProtocolMessageType('Example', (_message.Message,), dict(

  Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), dict(
    DESCRIPTOR = _EXAMPLE_TRIGGER,
    __module__ = 'corpus_pb2'
    # @@protoc_insertion_point(class_scope:Example.Trigger)
    ))
  ,
  DESCRIPTOR = _EXAMPLE,
  __module__ = 'corpus_pb2'
  # @@protoc_insertion_point(class_scope:Example)
  ))
_sym_db.RegisterMessage(Example)
_sym_db.RegisterMessage(Example.Trigger)

Corpus = _reflection.GeneratedProtocolMessageType('Corpus', (_message.Message,), dict(
  DESCRIPTOR = _CORPUS,
  __module__ = 'corpus_pb2'
  # @@protoc_insertion_point(class_scope:Corpus)
  ))
_sym_db.RegisterMessage(Corpus)


# @@protoc_insertion_point(module_scope)
