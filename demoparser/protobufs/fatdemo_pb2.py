# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demoparser/protobufs/fatdemo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from demoparser.protobufs import netmessages_pb2 as demoparser_dot_protobufs_dot_netmessages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='demoparser/protobufs/fatdemo.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\"demoparser/protobufs/fatdemo.proto\x1a&demoparser/protobufs/netmessages.proto\"M\n\x06MLDict\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nval_string\x18\x02 \x01(\t\x12\x0f\n\x07val_int\x18\x03 \x01(\x05\x12\x11\n\tval_float\x18\x04 \x01(\x02\"4\n\x07MLEvent\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x15\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x07.MLDict\"b\n\x0cMLMatchState\x12\x11\n\tgame_mode\x18\x01 \x01(\t\x12\r\n\x05phase\x18\x02 \x01(\t\x12\r\n\x05round\x18\x03 \x01(\x05\x12\x10\n\x08score_ct\x18\x04 \x01(\x05\x12\x0f\n\x07score_t\x18\x05 \x01(\x05\"W\n\x0cMLRoundState\x12\r\n\x05phase\x18\x01 \x01(\t\x12$\n\x08win_team\x18\x02 \x01(\x0e\x32\x06.ETeam:\nET_Unknown\x12\x12\n\nbomb_state\x18\x03 \x01(\t\"\xb8\x01\n\rMLWeaponState\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x0c.EWeaponType:\tEWT_Knife\x12\x11\n\tammo_clip\x18\x04 \x01(\x05\x12\x15\n\rammo_clip_max\x18\x05 \x01(\x05\x12\x14\n\x0c\x61mmo_reserve\x18\x06 \x01(\x05\x12\r\n\x05state\x18\x07 \x01(\t\x12\x14\n\x0crecoil_index\x18\x08 \x01(\x02\"\xb3\x03\n\rMLPlayerState\x12\x12\n\naccount_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x10\n\x08\x65ntindex\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04\x63lan\x18\x05 \x01(\t\x12 \n\x04team\x18\x06 \x01(\x0e\x32\x06.ETeam:\nET_Unknown\x12\x1b\n\x06\x61\x62spos\x18\x07 \x01(\x0b\x32\x0b.CMsgVector\x12\x1d\n\x08\x65yeangle\x18\x08 \x01(\x0b\x32\x0b.CMsgQAngle\x12!\n\x0c\x65yeangle_fwd\x18\t \x01(\x0b\x32\x0b.CMsgVector\x12\x0e\n\x06health\x18\n \x01(\x05\x12\r\n\x05\x61rmor\x18\x0b \x01(\x05\x12\x0f\n\x07\x66lashed\x18\x0c \x01(\x02\x12\x0e\n\x06smoked\x18\r \x01(\x02\x12\r\n\x05money\x18\x0e \x01(\x05\x12\x13\n\x0bround_kills\x18\x0f \x01(\x05\x12\x14\n\x0cround_killhs\x18\x10 \x01(\x05\x12\x0f\n\x07\x62urning\x18\x11 \x01(\x02\x12\x0e\n\x06helmet\x18\x12 \x01(\x08\x12\x12\n\ndefuse_kit\x18\x13 \x01(\x08\x12\x1f\n\x07weapons\x18\x14 \x03(\x0b\x32\x0e.MLWeaponState\"j\n\x0bMLGameState\x12\x1c\n\x05match\x18\x01 \x01(\x0b\x32\r.MLMatchState\x12\x1c\n\x05round\x18\x02 \x01(\x0b\x32\r.MLRoundState\x12\x1f\n\x07players\x18\x03 \x03(\x0b\x32\x0e.MLPlayerState\"\\\n\x0cMLDemoHeader\x12\x10\n\x08map_name\x18\x01 \x01(\t\x12\x11\n\ttick_rate\x18\x02 \x01(\x05\x12\x0f\n\x07version\x18\x03 \x01(\r\x12\x16\n\x0esteam_universe\x18\x04 \x01(\r\"S\n\x06MLTick\x12\x12\n\ntick_count\x18\x01 \x01(\x05\x12\x1b\n\x05state\x18\x02 \x01(\x0b\x32\x0c.MLGameState\x12\x18\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x08.MLEvent*\xac\x01\n\tEHitGroup\x12\x0f\n\x0b\x45HG_Generic\x10\x00\x12\x0c\n\x08\x45HG_Head\x10\x01\x12\r\n\tEHG_Chest\x10\x02\x12\x0f\n\x0b\x45HG_Stomach\x10\x03\x12\x0f\n\x0b\x45HG_LeftArm\x10\x04\x12\x10\n\x0c\x45HG_RightArm\x10\x05\x12\x0f\n\x0b\x45HG_LeftLeg\x10\x06\x12\x10\n\x0c\x45HG_RightLeg\x10\x07\x12\x0c\n\x08\x45HG_Gear\x10\x08\x12\x0c\n\x08\x45HG_Miss\x10\t*F\n\x05\x45Team\x12\x0e\n\nET_Unknown\x10\x00\x12\x10\n\x0c\x45T_Spectator\x10\x01\x12\x10\n\x0c\x45T_Terrorist\x10\x02\x12\t\n\x05\x45T_CT\x10\x03*\xe4\x01\n\x0b\x45WeaponType\x12\r\n\tEWT_Knife\x10\x00\x12\x0e\n\nEWT_Pistol\x10\x01\x12\x15\n\x11\x45WT_SubMachineGun\x10\x02\x12\r\n\tEWT_Rifle\x10\x03\x12\x0f\n\x0b\x45WT_Shotgun\x10\x04\x12\x13\n\x0f\x45WT_SniperRifle\x10\x05\x12\x12\n\x0e\x45WT_MachineGun\x10\x06\x12\n\n\x06\x45WT_C4\x10\x07\x12\x0f\n\x0b\x45WT_Grenade\x10\x08\x12\x11\n\rEWT_Equipment\x10\t\x12\x15\n\x11\x45WT_StackableItem\x10\n\x12\x0f\n\x0b\x45WT_Unknown\x10\x0b')
  ,
  dependencies=[demoparser_dot_protobufs_dot_netmessages__pb2.DESCRIPTOR,])

_EHITGROUP = _descriptor.EnumDescriptor(
  name='EHitGroup',
  full_name='EHitGroup',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EHG_Generic', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_Head', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_Chest', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_Stomach', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_LeftArm', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_RightArm', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_LeftLeg', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_RightLeg', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_Gear', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EHG_Miss', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1313,
  serialized_end=1485,
)
_sym_db.RegisterEnumDescriptor(_EHITGROUP)

EHitGroup = enum_type_wrapper.EnumTypeWrapper(_EHITGROUP)
_ETEAM = _descriptor.EnumDescriptor(
  name='ETeam',
  full_name='ETeam',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ET_Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ET_Spectator', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ET_Terrorist', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ET_CT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1487,
  serialized_end=1557,
)
_sym_db.RegisterEnumDescriptor(_ETEAM)

ETeam = enum_type_wrapper.EnumTypeWrapper(_ETEAM)
_EWEAPONTYPE = _descriptor.EnumDescriptor(
  name='EWeaponType',
  full_name='EWeaponType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EWT_Knife', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_Pistol', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_SubMachineGun', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_Rifle', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_Shotgun', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_SniperRifle', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_MachineGun', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_C4', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_Grenade', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_Equipment', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_StackableItem', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EWT_Unknown', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1560,
  serialized_end=1788,
)
_sym_db.RegisterEnumDescriptor(_EWEAPONTYPE)

EWeaponType = enum_type_wrapper.EnumTypeWrapper(_EWEAPONTYPE)
EHG_Generic = 0
EHG_Head = 1
EHG_Chest = 2
EHG_Stomach = 3
EHG_LeftArm = 4
EHG_RightArm = 5
EHG_LeftLeg = 6
EHG_RightLeg = 7
EHG_Gear = 8
EHG_Miss = 9
ET_Unknown = 0
ET_Spectator = 1
ET_Terrorist = 2
ET_CT = 3
EWT_Knife = 0
EWT_Pistol = 1
EWT_SubMachineGun = 2
EWT_Rifle = 3
EWT_Shotgun = 4
EWT_SniperRifle = 5
EWT_MachineGun = 6
EWT_C4 = 7
EWT_Grenade = 8
EWT_Equipment = 9
EWT_StackableItem = 10
EWT_Unknown = 11



_MLDICT = _descriptor.Descriptor(
  name='MLDict',
  full_name='MLDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MLDict.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val_string', full_name='MLDict.val_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val_int', full_name='MLDict.val_int', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val_float', full_name='MLDict.val_float', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=155,
)


_MLEVENT = _descriptor.Descriptor(
  name='MLEvent',
  full_name='MLEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_name', full_name='MLEvent.event_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='MLEvent.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=209,
)


_MLMATCHSTATE = _descriptor.Descriptor(
  name='MLMatchState',
  full_name='MLMatchState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_mode', full_name='MLMatchState.game_mode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='MLMatchState.phase', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='MLMatchState.round', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score_ct', full_name='MLMatchState.score_ct', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score_t', full_name='MLMatchState.score_t', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=309,
)


_MLROUNDSTATE = _descriptor.Descriptor(
  name='MLRoundState',
  full_name='MLRoundState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='MLRoundState.phase', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='win_team', full_name='MLRoundState.win_team', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bomb_state', full_name='MLRoundState.bomb_state', index=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=398,
)


_MLWEAPONSTATE = _descriptor.Descriptor(
  name='MLWeaponState',
  full_name='MLWeaponState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='MLWeaponState.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='MLWeaponState.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='MLWeaponState.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ammo_clip', full_name='MLWeaponState.ammo_clip', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ammo_clip_max', full_name='MLWeaponState.ammo_clip_max', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ammo_reserve', full_name='MLWeaponState.ammo_reserve', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='MLWeaponState.state', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recoil_index', full_name='MLWeaponState.recoil_index', index=7,
      number=8, type=2, cpp_type=6, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=585,
)


_MLPLAYERSTATE = _descriptor.Descriptor(
  name='MLPlayerState',
  full_name='MLPlayerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='MLPlayerState.account_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='MLPlayerState.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entindex', full_name='MLPlayerState.entindex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='MLPlayerState.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clan', full_name='MLPlayerState.clan', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team', full_name='MLPlayerState.team', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abspos', full_name='MLPlayerState.abspos', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eyeangle', full_name='MLPlayerState.eyeangle', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eyeangle_fwd', full_name='MLPlayerState.eyeangle_fwd', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='MLPlayerState.health', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='armor', full_name='MLPlayerState.armor', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flashed', full_name='MLPlayerState.flashed', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='smoked', full_name='MLPlayerState.smoked', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='MLPlayerState.money', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round_kills', full_name='MLPlayerState.round_kills', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round_killhs', full_name='MLPlayerState.round_killhs', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='burning', full_name='MLPlayerState.burning', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='helmet', full_name='MLPlayerState.helmet', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defuse_kit', full_name='MLPlayerState.defuse_kit', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weapons', full_name='MLPlayerState.weapons', index=19,
      number=20, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=1023,
)


_MLGAMESTATE = _descriptor.Descriptor(
  name='MLGameState',
  full_name='MLGameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='MLGameState.match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='MLGameState.round', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players', full_name='MLGameState.players', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1025,
  serialized_end=1131,
)


_MLDEMOHEADER = _descriptor.Descriptor(
  name='MLDemoHeader',
  full_name='MLDemoHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_name', full_name='MLDemoHeader.map_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_rate', full_name='MLDemoHeader.tick_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='MLDemoHeader.version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steam_universe', full_name='MLDemoHeader.steam_universe', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1133,
  serialized_end=1225,
)


_MLTICK = _descriptor.Descriptor(
  name='MLTick',
  full_name='MLTick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tick_count', full_name='MLTick.tick_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='MLTick.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='MLTick.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1227,
  serialized_end=1310,
)

_MLEVENT.fields_by_name['data'].message_type = _MLDICT
_MLROUNDSTATE.fields_by_name['win_team'].enum_type = _ETEAM
_MLWEAPONSTATE.fields_by_name['type'].enum_type = _EWEAPONTYPE
_MLPLAYERSTATE.fields_by_name['team'].enum_type = _ETEAM
_MLPLAYERSTATE.fields_by_name['abspos'].message_type = demoparser_dot_protobufs_dot_netmessages__pb2._CMSGVECTOR
_MLPLAYERSTATE.fields_by_name['eyeangle'].message_type = demoparser_dot_protobufs_dot_netmessages__pb2._CMSGQANGLE
_MLPLAYERSTATE.fields_by_name['eyeangle_fwd'].message_type = demoparser_dot_protobufs_dot_netmessages__pb2._CMSGVECTOR
_MLPLAYERSTATE.fields_by_name['weapons'].message_type = _MLWEAPONSTATE
_MLGAMESTATE.fields_by_name['match'].message_type = _MLMATCHSTATE
_MLGAMESTATE.fields_by_name['round'].message_type = _MLROUNDSTATE
_MLGAMESTATE.fields_by_name['players'].message_type = _MLPLAYERSTATE
_MLTICK.fields_by_name['state'].message_type = _MLGAMESTATE
_MLTICK.fields_by_name['events'].message_type = _MLEVENT
DESCRIPTOR.message_types_by_name['MLDict'] = _MLDICT
DESCRIPTOR.message_types_by_name['MLEvent'] = _MLEVENT
DESCRIPTOR.message_types_by_name['MLMatchState'] = _MLMATCHSTATE
DESCRIPTOR.message_types_by_name['MLRoundState'] = _MLROUNDSTATE
DESCRIPTOR.message_types_by_name['MLWeaponState'] = _MLWEAPONSTATE
DESCRIPTOR.message_types_by_name['MLPlayerState'] = _MLPLAYERSTATE
DESCRIPTOR.message_types_by_name['MLGameState'] = _MLGAMESTATE
DESCRIPTOR.message_types_by_name['MLDemoHeader'] = _MLDEMOHEADER
DESCRIPTOR.message_types_by_name['MLTick'] = _MLTICK
DESCRIPTOR.enum_types_by_name['EHitGroup'] = _EHITGROUP
DESCRIPTOR.enum_types_by_name['ETeam'] = _ETEAM
DESCRIPTOR.enum_types_by_name['EWeaponType'] = _EWEAPONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MLDict = _reflection.GeneratedProtocolMessageType('MLDict', (_message.Message,), dict(
  DESCRIPTOR = _MLDICT,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLDict)
  ))
_sym_db.RegisterMessage(MLDict)

MLEvent = _reflection.GeneratedProtocolMessageType('MLEvent', (_message.Message,), dict(
  DESCRIPTOR = _MLEVENT,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLEvent)
  ))
_sym_db.RegisterMessage(MLEvent)

MLMatchState = _reflection.GeneratedProtocolMessageType('MLMatchState', (_message.Message,), dict(
  DESCRIPTOR = _MLMATCHSTATE,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLMatchState)
  ))
_sym_db.RegisterMessage(MLMatchState)

MLRoundState = _reflection.GeneratedProtocolMessageType('MLRoundState', (_message.Message,), dict(
  DESCRIPTOR = _MLROUNDSTATE,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLRoundState)
  ))
_sym_db.RegisterMessage(MLRoundState)

MLWeaponState = _reflection.GeneratedProtocolMessageType('MLWeaponState', (_message.Message,), dict(
  DESCRIPTOR = _MLWEAPONSTATE,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLWeaponState)
  ))
_sym_db.RegisterMessage(MLWeaponState)

MLPlayerState = _reflection.GeneratedProtocolMessageType('MLPlayerState', (_message.Message,), dict(
  DESCRIPTOR = _MLPLAYERSTATE,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLPlayerState)
  ))
_sym_db.RegisterMessage(MLPlayerState)

MLGameState = _reflection.GeneratedProtocolMessageType('MLGameState', (_message.Message,), dict(
  DESCRIPTOR = _MLGAMESTATE,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLGameState)
  ))
_sym_db.RegisterMessage(MLGameState)

MLDemoHeader = _reflection.GeneratedProtocolMessageType('MLDemoHeader', (_message.Message,), dict(
  DESCRIPTOR = _MLDEMOHEADER,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLDemoHeader)
  ))
_sym_db.RegisterMessage(MLDemoHeader)

MLTick = _reflection.GeneratedProtocolMessageType('MLTick', (_message.Message,), dict(
  DESCRIPTOR = _MLTICK,
  __module__ = 'demoparser.protobufs.fatdemo_pb2'
  # @@protoc_insertion_point(class_scope:MLTick)
  ))
_sym_db.RegisterMessage(MLTick)


# @@protoc_insertion_point(module_scope)
