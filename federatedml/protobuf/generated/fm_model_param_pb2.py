# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fm-model-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fm-model-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer.fm',
  syntax='proto3',
  serialized_options=_b('B\021FMModelParamProto'),
  serialized_pb=_b('\n\x14\x66m-model-param.proto\x12)com.webank.ai.fate.core.mlmodel.buffer.fm\"\x1b\n\tEmbedding\x12\x0e\n\x06weight\x18\x01 \x03(\x01\"\xb9\x04\n\x0c\x46MModelParam\x12\r\n\x05iters\x18\x01 \x01(\x05\x12\x14\n\x0closs_history\x18\x02 \x03(\x01\x12\x14\n\x0cis_converged\x18\x03 \x01(\x08\x12S\n\x06weight\x18\x04 \x03(\x0b\x32\x43.com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.WeightEntry\x12Y\n\tembedding\x18\x05 \x03(\x0b\x32\x46.com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.EmbeddingEntry\x12\x12\n\nembed_size\x18\x06 \x01(\x05\x12\x11\n\tintercept\x18\x07 \x01(\x01\x12\x0e\n\x06header\x18\x08 \x03(\t\x12V\n\x12one_vs_rest_result\x18\t \x01(\x0b\x32:.com.webank.ai.fate.core.mlmodel.buffer.fm.OneVsRestResult\x12\x18\n\x10need_one_vs_rest\x18\n \x01(\x08\x1a-\n\x0bWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x66\n\x0e\x45mbeddingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32\x34.com.webank.ai.fate.core.mlmodel.buffer.fm.Embedding:\x02\x38\x01\"\xb0\x03\n\x0bSingleModel\x12\r\n\x05iters\x18\x01 \x01(\x05\x12\x14\n\x0closs_history\x18\x02 \x03(\x01\x12\x14\n\x0cis_converged\x18\x03 \x01(\x08\x12R\n\x06weight\x18\x04 \x03(\x0b\x32\x42.com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.WeightEntry\x12X\n\tembedding\x18\x05 \x03(\x0b\x32\x45.com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.EmbeddingEntry\x12\x11\n\tintercept\x18\x06 \x01(\x01\x12\x0e\n\x06header\x18\x07 \x03(\t\x1a-\n\x0bWeightEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x66\n\x0e\x45mbeddingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32\x34.com.webank.ai.fate.core.mlmodel.buffer.fm.Embedding:\x02\x38\x01\"\x80\x01\n\x0fOneVsRestResult\x12P\n\x10\x63ompleted_models\x18\x01 \x03(\x0b\x32\x36.com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel\x12\x1b\n\x13one_vs_rest_classes\x18\x02 \x03(\tB\x13\x42\x11\x46MModelParamProtob\x06proto3')
)




_EMBEDDING = _descriptor.Descriptor(
  name='Embedding',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.Embedding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.Embedding.weight', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=67,
  serialized_end=94,
)


_FMMODELPARAM_WEIGHTENTRY = _descriptor.Descriptor(
  name='WeightEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.WeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.WeightEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.WeightEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=517,
  serialized_end=562,
)

_FMMODELPARAM_EMBEDDINGENTRY = _descriptor.Descriptor(
  name='EmbeddingEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.EmbeddingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.EmbeddingEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.EmbeddingEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=666,
)

_FMMODELPARAM = _descriptor.Descriptor(
  name='FMModelParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iters', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.iters', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_history', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.loss_history', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.is_converged', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.weight', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='embedding', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.embedding', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='embed_size', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.embed_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intercept', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.intercept', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.header', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_vs_rest_result', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.one_vs_rest_result', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_one_vs_rest', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.need_one_vs_rest', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FMMODELPARAM_WEIGHTENTRY, _FMMODELPARAM_EMBEDDINGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=666,
)


_SINGLEMODEL_WEIGHTENTRY = _descriptor.Descriptor(
  name='WeightEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.WeightEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.WeightEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.WeightEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=517,
  serialized_end=562,
)

_SINGLEMODEL_EMBEDDINGENTRY = _descriptor.Descriptor(
  name='EmbeddingEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.EmbeddingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.EmbeddingEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.EmbeddingEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=666,
)

_SINGLEMODEL = _descriptor.Descriptor(
  name='SingleModel',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iters', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.iters', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_history', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.loss_history', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.is_converged', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.weight', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='embedding', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.embedding', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intercept', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.intercept', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.header', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SINGLEMODEL_WEIGHTENTRY, _SINGLEMODEL_EMBEDDINGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=669,
  serialized_end=1101,
)


_ONEVSRESTRESULT = _descriptor.Descriptor(
  name='OneVsRestResult',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.OneVsRestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='completed_models', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.OneVsRestResult.completed_models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='one_vs_rest_classes', full_name='com.webank.ai.fate.core.mlmodel.buffer.fm.OneVsRestResult.one_vs_rest_classes', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=1104,
  serialized_end=1232,
)

_FMMODELPARAM_WEIGHTENTRY.containing_type = _FMMODELPARAM
_FMMODELPARAM_EMBEDDINGENTRY.fields_by_name['value'].message_type = _EMBEDDING
_FMMODELPARAM_EMBEDDINGENTRY.containing_type = _FMMODELPARAM
_FMMODELPARAM.fields_by_name['weight'].message_type = _FMMODELPARAM_WEIGHTENTRY
_FMMODELPARAM.fields_by_name['embedding'].message_type = _FMMODELPARAM_EMBEDDINGENTRY
_FMMODELPARAM.fields_by_name['one_vs_rest_result'].message_type = _ONEVSRESTRESULT
_SINGLEMODEL_WEIGHTENTRY.containing_type = _SINGLEMODEL
_SINGLEMODEL_EMBEDDINGENTRY.fields_by_name['value'].message_type = _EMBEDDING
_SINGLEMODEL_EMBEDDINGENTRY.containing_type = _SINGLEMODEL
_SINGLEMODEL.fields_by_name['weight'].message_type = _SINGLEMODEL_WEIGHTENTRY
_SINGLEMODEL.fields_by_name['embedding'].message_type = _SINGLEMODEL_EMBEDDINGENTRY
_ONEVSRESTRESULT.fields_by_name['completed_models'].message_type = _SINGLEMODEL
DESCRIPTOR.message_types_by_name['Embedding'] = _EMBEDDING
DESCRIPTOR.message_types_by_name['FMModelParam'] = _FMMODELPARAM
DESCRIPTOR.message_types_by_name['SingleModel'] = _SINGLEMODEL
DESCRIPTOR.message_types_by_name['OneVsRestResult'] = _ONEVSRESTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Embedding = _reflection.GeneratedProtocolMessageType('Embedding', (_message.Message,), dict(
  DESCRIPTOR = _EMBEDDING,
  __module__ = 'fm_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.Embedding)
  ))
_sym_db.RegisterMessage(Embedding)

FMModelParam = _reflection.GeneratedProtocolMessageType('FMModelParam', (_message.Message,), dict(

  WeightEntry = _reflection.GeneratedProtocolMessageType('WeightEntry', (_message.Message,), dict(
    DESCRIPTOR = _FMMODELPARAM_WEIGHTENTRY,
    __module__ = 'fm_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.WeightEntry)
    ))
  ,

  EmbeddingEntry = _reflection.GeneratedProtocolMessageType('EmbeddingEntry', (_message.Message,), dict(
    DESCRIPTOR = _FMMODELPARAM_EMBEDDINGENTRY,
    __module__ = 'fm_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam.EmbeddingEntry)
    ))
  ,
  DESCRIPTOR = _FMMODELPARAM,
  __module__ = 'fm_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.FMModelParam)
  ))
_sym_db.RegisterMessage(FMModelParam)
_sym_db.RegisterMessage(FMModelParam.WeightEntry)
_sym_db.RegisterMessage(FMModelParam.EmbeddingEntry)

SingleModel = _reflection.GeneratedProtocolMessageType('SingleModel', (_message.Message,), dict(

  WeightEntry = _reflection.GeneratedProtocolMessageType('WeightEntry', (_message.Message,), dict(
    DESCRIPTOR = _SINGLEMODEL_WEIGHTENTRY,
    __module__ = 'fm_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.WeightEntry)
    ))
  ,

  EmbeddingEntry = _reflection.GeneratedProtocolMessageType('EmbeddingEntry', (_message.Message,), dict(
    DESCRIPTOR = _SINGLEMODEL_EMBEDDINGENTRY,
    __module__ = 'fm_model_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel.EmbeddingEntry)
    ))
  ,
  DESCRIPTOR = _SINGLEMODEL,
  __module__ = 'fm_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.SingleModel)
  ))
_sym_db.RegisterMessage(SingleModel)
_sym_db.RegisterMessage(SingleModel.WeightEntry)
_sym_db.RegisterMessage(SingleModel.EmbeddingEntry)

OneVsRestResult = _reflection.GeneratedProtocolMessageType('OneVsRestResult', (_message.Message,), dict(
  DESCRIPTOR = _ONEVSRESTRESULT,
  __module__ = 'fm_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.fm.OneVsRestResult)
  ))
_sym_db.RegisterMessage(OneVsRestResult)


DESCRIPTOR._options = None
_FMMODELPARAM_WEIGHTENTRY._options = None
_FMMODELPARAM_EMBEDDINGENTRY._options = None
_SINGLEMODEL_WEIGHTENTRY._options = None
_SINGLEMODEL_EMBEDDINGENTRY._options = None
# @@protoc_insertion_point(module_scope)
