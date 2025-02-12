# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/input_reader.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*object_detection/protos/input_reader.proto\x12\x17object_detection.protos\"\xb5\t\n\x0bInputReader\x12\x0e\n\x04name\x18\x17 \x01(\t:\x00\x12\x18\n\x0elabel_map_path\x18\x01 \x01(\t:\x00\x12\x15\n\x07shuffle\x18\x02 \x01(\x08:\x04true\x12!\n\x13shuffle_buffer_size\x18\x0b \x01(\r:\x04\x32\x30\x34\x38\x12*\n\x1d\x66ilenames_shuffle_buffer_size\x18\x0c \x01(\r:\x03\x31\x30\x30\x12\x15\n\nnum_epochs\x18\x05 \x01(\r:\x01\x30\x12!\n\x16sample_1_of_n_examples\x18\x16 \x01(\r:\x01\x31\x12\x17\n\x0bnum_readers\x18\x06 \x01(\r:\x02\x36\x34\x12\x1f\n\x14num_parallel_batches\x18\x13 \x01(\r:\x01\x38\x12\x1f\n\x14num_prefetch_batches\x18\x14 \x01(\x05:\x01\x32\x12 \n\x0equeue_capacity\x18\x03 \x01(\r:\x04\x32\x30\x30\x30\x42\x02\x18\x01\x12#\n\x11min_after_dequeue\x18\x04 \x01(\r:\x04\x31\x30\x30\x30\x42\x02\x18\x01\x12\x1d\n\x11read_block_length\x18\x0f \x01(\r:\x02\x33\x32\x12\x1e\n\rprefetch_size\x18\r \x01(\r:\x03\x35\x31\x32\x42\x02\x18\x01\x12&\n\x16num_parallel_map_calls\x18\x0e \x01(\r:\x02\x36\x34\x42\x02\x18\x01\x12\"\n\x17num_additional_channels\x18\x12 \x01(\x05:\x01\x30\x12\x18\n\rnum_keypoints\x18\x10 \x01(\r:\x01\x30\x12\x1c\n\x14keypoint_type_weight\x18\x1a \x03(\x02\x12 \n\x13max_number_of_boxes\x18\x15 \x01(\x05:\x03\x31\x30\x30\x12%\n\x16load_multiclass_scores\x18\x18 \x01(\x08:\x05\x66\x61lse\x12$\n\x15load_context_features\x18\x19 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13load_instance_masks\x18\x07 \x01(\x08:\x05\x66\x61lse\x12M\n\tmask_type\x18\n \x01(\x0e\x32).object_detection.protos.InstanceMaskType:\x0fNUMERICAL_MASKS\x12\x1e\n\x0fload_dense_pose\x18\x1f \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10use_display_name\x18\x11 \x01(\x08:\x05\x66\x61lse\x12 \n\x11include_source_id\x18\x1b \x01(\x08:\x05\x66\x61lse\x12\x42\n\ninput_type\x18\x1e \x01(\x0e\x32\".object_detection.protos.InputType:\nTF_EXAMPLE\x12\x17\n\x0b\x66rame_index\x18  \x01(\x05:\x02-1\x12N\n\x16tf_record_input_reader\x18\x08 \x01(\x0b\x32,.object_detection.protos.TFRecordInputReaderH\x00\x12M\n\x15\x65xternal_input_reader\x18\t \x01(\x0b\x32,.object_detection.protos.ExternalInputReaderH\x00\x12&\n\x17\x65xpand_labels_hierarchy\x18\x1d \x01(\x08:\x05\x66\x61lseB\x0e\n\x0cinput_reader\")\n\x13TFRecordInputReader\x12\x12\n\ninput_path\x18\x01 \x03(\t\"\x1c\n\x13\x45xternalInputReader*\x05\x08\x01\x10\xe8\x07*C\n\x10InstanceMaskType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x13\n\x0fNUMERICAL_MASKS\x10\x01\x12\r\n\tPNG_MASKS\x10\x02*G\n\tInputType\x12\x11\n\rINPUT_DEFAULT\x10\x00\x12\x0e\n\nTF_EXAMPLE\x10\x01\x12\x17\n\x13TF_SEQUENCE_EXAMPLE\x10\x02')

_INSTANCEMASKTYPE = DESCRIPTOR.enum_types_by_name['InstanceMaskType']
InstanceMaskType = enum_type_wrapper.EnumTypeWrapper(_INSTANCEMASKTYPE)
_INPUTTYPE = DESCRIPTOR.enum_types_by_name['InputType']
InputType = enum_type_wrapper.EnumTypeWrapper(_INPUTTYPE)
DEFAULT = 0
NUMERICAL_MASKS = 1
PNG_MASKS = 2
INPUT_DEFAULT = 0
TF_EXAMPLE = 1
TF_SEQUENCE_EXAMPLE = 2


_INPUTREADER = DESCRIPTOR.message_types_by_name['InputReader']
_TFRECORDINPUTREADER = DESCRIPTOR.message_types_by_name['TFRecordInputReader']
_EXTERNALINPUTREADER = DESCRIPTOR.message_types_by_name['ExternalInputReader']
InputReader = _reflection.GeneratedProtocolMessageType('InputReader', (_message.Message,), {
  'DESCRIPTOR' : _INPUTREADER,
  '__module__' : 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.InputReader)
  })
_sym_db.RegisterMessage(InputReader)

TFRecordInputReader = _reflection.GeneratedProtocolMessageType('TFRecordInputReader', (_message.Message,), {
  'DESCRIPTOR' : _TFRECORDINPUTREADER,
  '__module__' : 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.TFRecordInputReader)
  })
_sym_db.RegisterMessage(TFRecordInputReader)

ExternalInputReader = _reflection.GeneratedProtocolMessageType('ExternalInputReader', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALINPUTREADER,
  '__module__' : 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ExternalInputReader)
  })
_sym_db.RegisterMessage(ExternalInputReader)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INPUTREADER.fields_by_name['queue_capacity']._options = None
  _INPUTREADER.fields_by_name['queue_capacity']._serialized_options = b'\030\001'
  _INPUTREADER.fields_by_name['min_after_dequeue']._options = None
  _INPUTREADER.fields_by_name['min_after_dequeue']._serialized_options = b'\030\001'
  _INPUTREADER.fields_by_name['prefetch_size']._options = None
  _INPUTREADER.fields_by_name['prefetch_size']._serialized_options = b'\030\001'
  _INPUTREADER.fields_by_name['num_parallel_map_calls']._options = None
  _INPUTREADER.fields_by_name['num_parallel_map_calls']._serialized_options = b'\030\001'
  _INSTANCEMASKTYPE._serialized_start=1352
  _INSTANCEMASKTYPE._serialized_end=1419
  _INPUTTYPE._serialized_start=1421
  _INPUTTYPE._serialized_end=1492
  _INPUTREADER._serialized_start=72
  _INPUTREADER._serialized_end=1277
  _TFRECORDINPUTREADER._serialized_start=1279
  _TFRECORDINPUTREADER._serialized_end=1320
  _EXTERNALINPUTREADER._serialized_start=1322
  _EXTERNALINPUTREADER._serialized_end=1350
# @@protoc_insertion_point(module_scope)
