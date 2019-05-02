from enum import Enum
from typing import Type

from bridge.data_interpreter import DataInterpreter
from bridge.data_type import DataType
from util.util_tuple import Input, Output


class TelemetryInputInputDef(Enum):

    timestamp = Input(index=0, type=DataType.string)
    control_pid_height_p = Input(index=1, type=DataType.float)
    control_pid_height_i = Input(index=2, type=DataType.float)
    control_pid_height_d = Input(index=3, type=DataType.float)
    control_pid_height_n = Input(index=4, type=DataType.float)
    control_pid_roll_p = Input(index=5, type=DataType.float)
    control_pid_roll_i = Input(index=6, type=DataType.float)
    control_pid_roll_d = Input(index=7, type=DataType.float)
    control_pid_roll_n = Input(index=8, type=DataType.float)
    control_pid_pitch_p = Input(index=9, type=DataType.float)
    control_pid_pitch_i = Input(index=10, type=DataType.float)
    control_pid_pitch_d = Input(index=11, type=DataType.float)
    control_pid_pitch_n = Input(index=12, type=DataType.float)
    control_overwrite = Input(index=13, type=DataType.bit)
    solar_panel_state_0 = Input(index=14, type=DataType.bit)
    solar_panel_state_1 = Input(index=15, type=DataType.bit)
    solar_panel_state_2 = Input(index=16, type=DataType.bit)
    solar_panel_state_3 = Input(index=17, type=DataType.bit)
    solar_panel_state_4 = Input(index=18, type=DataType.bit)
    solar_panel_state_5 = Input(index=19, type=DataType.bit)
    solar_panel_state_6 = Input(index=20, type=DataType.bit)
    solar_panel_state_7 = Input(index=21, type=DataType.bit)
    solar_panel_state_8 = Input(index=22, type=DataType.bit)
    solar_panel_state_9 = Input(index=23, type=DataType.bit)
    advised_speed = Input(index=24, type=DataType.float, out_type=DataType.int, modbus_ref=40006)

    advised_speed_min = Output(type=DataType.int, modbus_ref=40004)
    advised_speed_max = Output(type=DataType.int, modbus_ref=40005)
    connection_status = Output(type=DataType.int, modbus_ref=40012)


class TelemetryInputInterpreter(DataInterpreter):

    def __init__(self, enum: Type[Enum]):
        super().__init__(enum)
        self.on_change(TelemetryInputInputDef.advised_speed, self.on_advised_speed_change)
        self.set(TelemetryInputInputDef.connection_status, 3)

    def on_advised_speed_change(self, new_value: int):
        advised_speed_offset = 4

        min_speed = new_value - advised_speed_offset if new_value >= advised_speed_offset else 0
        max_speed = new_value + advised_speed_offset if new_value + advised_speed_offset <= 50 else 50

        self.set(TelemetryInputInputDef.advised_speed_min, min_speed)
        self.set(TelemetryInputInputDef.advised_speed_max, max_speed)
