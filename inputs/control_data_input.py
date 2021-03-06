from enum import Enum
from typing import Type

from bridge.data_interpreter import DataInterpreter
from bridge.data_type import DataType
from util.util_tuple import Input, Output


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
    speed = Input(index=14, type=DataType.float, out_type=DataType.int, modbus_ref=40003)
    real_height = Input(index=15, type=DataType.float, out_type=DataType.int, modbus_ref=40011)
    real_roll = Input(index=16, type=DataType.float, out_type=DataType.int, modbus_ref=40013)

    display_height = Output(DataType.int, modbus_ref=40015)


class ControlDataInputInterpreter(DataInterpreter):

    def __init__(self, enum: Type[Enum]):
        super().__init__(enum)
        self.on_change(ControlDataInputDef.real_height, self.on_real_height_change)

    def on_real_height_change(self, value: float):
        hmi_offset = 20  # The lowest number in the height scale on the HMI
        self.set(ControlDataInputDef.display_height, value + hmi_offset)

