# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vlslam.proto

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
  name='vlslam.proto',
  package='vlslam_pb',
  serialized_pb=_b('\n\x0cvlslam.proto\x12\tvlslam_pb\"\xe7\x04\n\nCameraInfo\x12\x0c\n\x04rows\x18\x01 \x02(\x05\x12\x0c\n\x04\x63ols\x18\x02 \x02(\x05\x12\x30\n\x07pinhole\x18\x05 \x01(\x0b\x32\x1d.vlslam_pb.CameraInfo.PinholeH\x00\x12\x30\n\x03\x66ov\x18\x06 \x01(\x0b\x32!.vlslam_pb.CameraInfo.FieldOfViewH\x00\x12.\n\x06radtan\x18\x07 \x01(\x0b\x32\x1c.vlslam_pb.CameraInfo.RadTanH\x00\x12\x31\n\x04\x65qui\x18\x08 \x01(\x0b\x32!.vlslam_pb.CameraInfo.EquidistantH\x00\x1a\x39\n\x07Pinhole\x12\n\n\x02\x66x\x18\x01 \x02(\x01\x12\n\n\x02\x66y\x18\x02 \x02(\x01\x12\n\n\x02\x63x\x18\x03 \x02(\x01\x12\n\n\x02\x63y\x18\x04 \x02(\x01\x1aH\n\x0b\x46ieldOfView\x12\n\n\x02\x66x\x18\x01 \x02(\x01\x12\n\n\x02\x66y\x18\x02 \x02(\x01\x12\n\n\x02\x63x\x18\x03 \x02(\x01\x12\n\n\x02\x63y\x18\x04 \x02(\x01\x12\t\n\x01w\x18\x05 \x02(\x01\x1at\n\x06RadTan\x12\n\n\x02\x66x\x18\x01 \x02(\x01\x12\n\n\x02\x66y\x18\x02 \x02(\x01\x12\n\n\x02\x63x\x18\x03 \x02(\x01\x12\n\n\x02\x63y\x18\x04 \x02(\x01\x12\n\n\x02r0\x18\x05 \x02(\x01\x12\n\n\x02r1\x18\x06 \x02(\x01\x12\n\n\x02k0\x18\x07 \x02(\x01\x12\n\n\x02k1\x18\x08 \x02(\x01\x12\n\n\x02k2\x18\t \x02(\x01\x1am\n\x0b\x45quidistant\x12\n\n\x02\x66x\x18\x01 \x02(\x01\x12\n\n\x02\x66y\x18\x02 \x02(\x01\x12\n\n\x02\x63x\x18\x03 \x02(\x01\x12\n\n\x02\x63y\x18\x04 \x02(\x01\x12\n\n\x02k0\x18\x07 \x02(\x01\x12\n\n\x02k1\x18\x08 \x02(\x01\x12\n\n\x02k2\x18\t \x02(\x01\x12\n\n\x02k3\x18\n \x02(\x01\x42\x0c\n\ndistortion\"\xc6\x01\n\x07\x46\x65\x61ture\x12\n\n\x02id\x18\x01 \x02(\x03\x12)\n\x06status\x18\x02 \x02(\x0e\x32\x19.vlslam_pb.Feature.Status\x12\n\n\x02xp\x18\x03 \x03(\x01\x12\n\n\x02xw\x18\x04 \x03(\x01\x12\t\n\x01z\x18\x05 \x01(\x01\"a\n\x06Status\x12\t\n\x05\x45MPTY\x10\x00\x12\x0c\n\x08GOODDROP\x10\x01\x12\x08\n\x04KEEP\x10\x02\x12\n\n\x06REJECT\x10\x03\x12\x10\n\x0cINITIALIZING\x10\x04\x12\t\n\x05READY\x10\x05\x12\x0b\n\x07INSTATE\x10\x06\"S\n\x06Packet\x12\n\n\x02ts\x18\x01 \x02(\x01\x12\x0b\n\x03gwc\x18\x02 \x03(\x01\x12$\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32\x12.vlslam_pb.Feature\x12\n\n\x02wg\x18\x04 \x03(\x01\":\n\x05Track\x12\n\n\x02ts\x18\x01 \x02(\x01\x12%\n\ttracklets\x18\x02 \x03(\x0b\x32\x12.vlslam_pb.Feature\"\x8b\x01\n\x07\x44\x61taset\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12%\n\x06\x63\x61mera\x18\x02 \x02(\x0b\x32\x15.vlslam_pb.CameraInfo\x12\"\n\x07packets\x18\x03 \x03(\x0b\x32\x11.vlslam_pb.Packet\x12 \n\x06tracks\x18\x04 \x03(\x0b\x32\x10.vlslam_pb.Track\"H\n\x07\x45\x64geMap\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0c\n\x04rows\x18\x02 \x02(\x05\x12\x0c\n\x04\x63ols\x18\x03 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x02\"\xa9\x01\n\x0b\x42oundingBox\x12\x12\n\ntop_left_x\x18\x01 \x02(\x02\x12\x12\n\ntop_left_y\x18\x02 \x02(\x02\x12\x16\n\x0e\x62ottom_right_x\x18\x03 \x02(\x02\x12\x16\n\x0e\x62ottom_right_y\x18\x04 \x02(\x02\x12\x0e\n\x06scores\x18\x05 \x03(\x02\x12\x12\n\nclass_name\x18\x06 \x01(\t\x12\r\n\x05label\x18\x07 \x01(\x05\x12\x0f\n\x07\x61zimuth\x18\x08 \x01(\x02\"V\n\x0f\x42oundingBoxList\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12.\n\x0e\x62ounding_boxes\x18\x02 \x03(\x0b\x32\x16.vlslam_pb.BoundingBox')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FEATURE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='vlslam_pb.Feature.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOODDROP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEEP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTATE', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=747,
  serialized_end=844,
)
_sym_db.RegisterEnumDescriptor(_FEATURE_STATUS)


_CAMERAINFO_PINHOLE = _descriptor.Descriptor(
  name='Pinhole',
  full_name='vlslam_pb.CameraInfo.Pinhole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fx', full_name='vlslam_pb.CameraInfo.Pinhole.fx', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fy', full_name='vlslam_pb.CameraInfo.Pinhole.fy', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cx', full_name='vlslam_pb.CameraInfo.Pinhole.cx', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cy', full_name='vlslam_pb.CameraInfo.Pinhole.cy', index=3,
      number=4, type=1, cpp_type=5, label=2,
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
  serialized_start=269,
  serialized_end=326,
)

_CAMERAINFO_FIELDOFVIEW = _descriptor.Descriptor(
  name='FieldOfView',
  full_name='vlslam_pb.CameraInfo.FieldOfView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fx', full_name='vlslam_pb.CameraInfo.FieldOfView.fx', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fy', full_name='vlslam_pb.CameraInfo.FieldOfView.fy', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cx', full_name='vlslam_pb.CameraInfo.FieldOfView.cx', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cy', full_name='vlslam_pb.CameraInfo.FieldOfView.cy', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='vlslam_pb.CameraInfo.FieldOfView.w', index=4,
      number=5, type=1, cpp_type=5, label=2,
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
  serialized_start=328,
  serialized_end=400,
)

_CAMERAINFO_RADTAN = _descriptor.Descriptor(
  name='RadTan',
  full_name='vlslam_pb.CameraInfo.RadTan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fx', full_name='vlslam_pb.CameraInfo.RadTan.fx', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fy', full_name='vlslam_pb.CameraInfo.RadTan.fy', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cx', full_name='vlslam_pb.CameraInfo.RadTan.cx', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cy', full_name='vlslam_pb.CameraInfo.RadTan.cy', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r0', full_name='vlslam_pb.CameraInfo.RadTan.r0', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r1', full_name='vlslam_pb.CameraInfo.RadTan.r1', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k0', full_name='vlslam_pb.CameraInfo.RadTan.k0', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k1', full_name='vlslam_pb.CameraInfo.RadTan.k1', index=7,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k2', full_name='vlslam_pb.CameraInfo.RadTan.k2', index=8,
      number=9, type=1, cpp_type=5, label=2,
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
  serialized_start=402,
  serialized_end=518,
)

_CAMERAINFO_EQUIDISTANT = _descriptor.Descriptor(
  name='Equidistant',
  full_name='vlslam_pb.CameraInfo.Equidistant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fx', full_name='vlslam_pb.CameraInfo.Equidistant.fx', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fy', full_name='vlslam_pb.CameraInfo.Equidistant.fy', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cx', full_name='vlslam_pb.CameraInfo.Equidistant.cx', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cy', full_name='vlslam_pb.CameraInfo.Equidistant.cy', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k0', full_name='vlslam_pb.CameraInfo.Equidistant.k0', index=4,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k1', full_name='vlslam_pb.CameraInfo.Equidistant.k1', index=5,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k2', full_name='vlslam_pb.CameraInfo.Equidistant.k2', index=6,
      number=9, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k3', full_name='vlslam_pb.CameraInfo.Equidistant.k3', index=7,
      number=10, type=1, cpp_type=5, label=2,
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
  serialized_start=520,
  serialized_end=629,
)

_CAMERAINFO = _descriptor.Descriptor(
  name='CameraInfo',
  full_name='vlslam_pb.CameraInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='vlslam_pb.CameraInfo.rows', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cols', full_name='vlslam_pb.CameraInfo.cols', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pinhole', full_name='vlslam_pb.CameraInfo.pinhole', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fov', full_name='vlslam_pb.CameraInfo.fov', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radtan', full_name='vlslam_pb.CameraInfo.radtan', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equi', full_name='vlslam_pb.CameraInfo.equi', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CAMERAINFO_PINHOLE, _CAMERAINFO_FIELDOFVIEW, _CAMERAINFO_RADTAN, _CAMERAINFO_EQUIDISTANT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='distortion', full_name='vlslam_pb.CameraInfo.distortion',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=28,
  serialized_end=643,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='vlslam_pb.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='vlslam_pb.Feature.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='vlslam_pb.Feature.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xp', full_name='vlslam_pb.Feature.xp', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xw', full_name='vlslam_pb.Feature.xw', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='vlslam_pb.Feature.z', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEATURE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=646,
  serialized_end=844,
)


_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='vlslam_pb.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='vlslam_pb.Packet.ts', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gwc', full_name='vlslam_pb.Packet.gwc', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='features', full_name='vlslam_pb.Packet.features', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wg', full_name='vlslam_pb.Packet.wg', index=3,
      number=4, type=1, cpp_type=5, label=3,
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
  serialized_start=846,
  serialized_end=929,
)


_TRACK = _descriptor.Descriptor(
  name='Track',
  full_name='vlslam_pb.Track',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='vlslam_pb.Track.ts', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracklets', full_name='vlslam_pb.Track.tracklets', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=931,
  serialized_end=989,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='vlslam_pb.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='vlslam_pb.Dataset.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera', full_name='vlslam_pb.Dataset.camera', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packets', full_name='vlslam_pb.Dataset.packets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracks', full_name='vlslam_pb.Dataset.tracks', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=992,
  serialized_end=1131,
)


_EDGEMAP = _descriptor.Descriptor(
  name='EdgeMap',
  full_name='vlslam_pb.EdgeMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='vlslam_pb.EdgeMap.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='vlslam_pb.EdgeMap.rows', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cols', full_name='vlslam_pb.EdgeMap.cols', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='vlslam_pb.EdgeMap.data', index=3,
      number=4, type=2, cpp_type=6, label=3,
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
  serialized_start=1133,
  serialized_end=1205,
)


_BOUNDINGBOX = _descriptor.Descriptor(
  name='BoundingBox',
  full_name='vlslam_pb.BoundingBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='top_left_x', full_name='vlslam_pb.BoundingBox.top_left_x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top_left_y', full_name='vlslam_pb.BoundingBox.top_left_y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom_right_x', full_name='vlslam_pb.BoundingBox.bottom_right_x', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bottom_right_y', full_name='vlslam_pb.BoundingBox.bottom_right_y', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scores', full_name='vlslam_pb.BoundingBox.scores', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='vlslam_pb.BoundingBox.class_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='vlslam_pb.BoundingBox.label', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='azimuth', full_name='vlslam_pb.BoundingBox.azimuth', index=7,
      number=8, type=2, cpp_type=6, label=1,
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
  serialized_start=1208,
  serialized_end=1377,
)


_BOUNDINGBOXLIST = _descriptor.Descriptor(
  name='BoundingBoxList',
  full_name='vlslam_pb.BoundingBoxList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='vlslam_pb.BoundingBoxList.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bounding_boxes', full_name='vlslam_pb.BoundingBoxList.bounding_boxes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1379,
  serialized_end=1465,
)

_CAMERAINFO_PINHOLE.containing_type = _CAMERAINFO
_CAMERAINFO_FIELDOFVIEW.containing_type = _CAMERAINFO
_CAMERAINFO_RADTAN.containing_type = _CAMERAINFO
_CAMERAINFO_EQUIDISTANT.containing_type = _CAMERAINFO
_CAMERAINFO.fields_by_name['pinhole'].message_type = _CAMERAINFO_PINHOLE
_CAMERAINFO.fields_by_name['fov'].message_type = _CAMERAINFO_FIELDOFVIEW
_CAMERAINFO.fields_by_name['radtan'].message_type = _CAMERAINFO_RADTAN
_CAMERAINFO.fields_by_name['equi'].message_type = _CAMERAINFO_EQUIDISTANT
_CAMERAINFO.oneofs_by_name['distortion'].fields.append(
  _CAMERAINFO.fields_by_name['pinhole'])
_CAMERAINFO.fields_by_name['pinhole'].containing_oneof = _CAMERAINFO.oneofs_by_name['distortion']
_CAMERAINFO.oneofs_by_name['distortion'].fields.append(
  _CAMERAINFO.fields_by_name['fov'])
_CAMERAINFO.fields_by_name['fov'].containing_oneof = _CAMERAINFO.oneofs_by_name['distortion']
_CAMERAINFO.oneofs_by_name['distortion'].fields.append(
  _CAMERAINFO.fields_by_name['radtan'])
_CAMERAINFO.fields_by_name['radtan'].containing_oneof = _CAMERAINFO.oneofs_by_name['distortion']
_CAMERAINFO.oneofs_by_name['distortion'].fields.append(
  _CAMERAINFO.fields_by_name['equi'])
_CAMERAINFO.fields_by_name['equi'].containing_oneof = _CAMERAINFO.oneofs_by_name['distortion']
_FEATURE.fields_by_name['status'].enum_type = _FEATURE_STATUS
_FEATURE_STATUS.containing_type = _FEATURE
_PACKET.fields_by_name['features'].message_type = _FEATURE
_TRACK.fields_by_name['tracklets'].message_type = _FEATURE
_DATASET.fields_by_name['camera'].message_type = _CAMERAINFO
_DATASET.fields_by_name['packets'].message_type = _PACKET
_DATASET.fields_by_name['tracks'].message_type = _TRACK
_BOUNDINGBOXLIST.fields_by_name['bounding_boxes'].message_type = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['CameraInfo'] = _CAMERAINFO
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET
DESCRIPTOR.message_types_by_name['Track'] = _TRACK
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['EdgeMap'] = _EDGEMAP
DESCRIPTOR.message_types_by_name['BoundingBox'] = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['BoundingBoxList'] = _BOUNDINGBOXLIST

CameraInfo = _reflection.GeneratedProtocolMessageType('CameraInfo', (_message.Message,), dict(

  Pinhole = _reflection.GeneratedProtocolMessageType('Pinhole', (_message.Message,), dict(
    DESCRIPTOR = _CAMERAINFO_PINHOLE,
    __module__ = 'vlslam_pb2'
    # @@protoc_insertion_point(class_scope:vlslam_pb.CameraInfo.Pinhole)
    ))
  ,

  FieldOfView = _reflection.GeneratedProtocolMessageType('FieldOfView', (_message.Message,), dict(
    DESCRIPTOR = _CAMERAINFO_FIELDOFVIEW,
    __module__ = 'vlslam_pb2'
    # @@protoc_insertion_point(class_scope:vlslam_pb.CameraInfo.FieldOfView)
    ))
  ,

  RadTan = _reflection.GeneratedProtocolMessageType('RadTan', (_message.Message,), dict(
    DESCRIPTOR = _CAMERAINFO_RADTAN,
    __module__ = 'vlslam_pb2'
    # @@protoc_insertion_point(class_scope:vlslam_pb.CameraInfo.RadTan)
    ))
  ,

  Equidistant = _reflection.GeneratedProtocolMessageType('Equidistant', (_message.Message,), dict(
    DESCRIPTOR = _CAMERAINFO_EQUIDISTANT,
    __module__ = 'vlslam_pb2'
    # @@protoc_insertion_point(class_scope:vlslam_pb.CameraInfo.Equidistant)
    ))
  ,
  DESCRIPTOR = _CAMERAINFO,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.CameraInfo)
  ))
_sym_db.RegisterMessage(CameraInfo)
_sym_db.RegisterMessage(CameraInfo.Pinhole)
_sym_db.RegisterMessage(CameraInfo.FieldOfView)
_sym_db.RegisterMessage(CameraInfo.RadTan)
_sym_db.RegisterMessage(CameraInfo.Equidistant)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.Feature)
  ))
_sym_db.RegisterMessage(Feature)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), dict(
  DESCRIPTOR = _PACKET,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.Packet)
  ))
_sym_db.RegisterMessage(Packet)

Track = _reflection.GeneratedProtocolMessageType('Track', (_message.Message,), dict(
  DESCRIPTOR = _TRACK,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.Track)
  ))
_sym_db.RegisterMessage(Track)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), dict(
  DESCRIPTOR = _DATASET,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.Dataset)
  ))
_sym_db.RegisterMessage(Dataset)

EdgeMap = _reflection.GeneratedProtocolMessageType('EdgeMap', (_message.Message,), dict(
  DESCRIPTOR = _EDGEMAP,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.EdgeMap)
  ))
_sym_db.RegisterMessage(EdgeMap)

BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.BoundingBox)
  ))
_sym_db.RegisterMessage(BoundingBox)

BoundingBoxList = _reflection.GeneratedProtocolMessageType('BoundingBoxList', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOXLIST,
  __module__ = 'vlslam_pb2'
  # @@protoc_insertion_point(class_scope:vlslam_pb.BoundingBoxList)
  ))
_sym_db.RegisterMessage(BoundingBoxList)


# @@protoc_insertion_point(module_scope)