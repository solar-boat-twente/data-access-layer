from enum import Enum

from bridge.data_type import DataType
from util.util_tuple import Input


class ControlDataInputDef(Enum):

    timestamp = Input(index=0, type=DataType.string)
    xsens_raw_pitch = Input(index=1, type=DataType.float)
    xsens_raw_roll = Input(index=2, type=DataType.float)
    xsens_filtered_pitch = Input(index=3, type=DataType.float)
    xsens_filtered_roll = Input(index=4, type=DataType.float)
    xsens_raw_z_acceleration = Input(index=5, type=DataType.float)
    vlotters_angle_left = Input(index=6, type=DataType.float)
    vlotters_angle_right = Input(index=7, type=DataType.float)
    computed_force_roll = Input(index=8, type=DataType.float)
    computed_force_pitch = Input(index=9, type=DataType.float)
    computed_force_height = Input(index=10, type=DataType.float)
    computed_angle_left = Input(index=11, type=DataType.float)
    computed_angle_right = Input(index=12, type=DataType.float)
    computed_angle_back = Input(index=13, type=DataType.float)
