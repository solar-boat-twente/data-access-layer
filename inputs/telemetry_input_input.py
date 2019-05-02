from enum import Enum

from bridge.data_type import DataType
from util.util_tuple import Input


class TelemetryInputInputDef(Enum):

    timestamp = Input(index=0, type=DataType.string)
    control_pid_telem_p = Input(index=1, type=DataType.float)
    control_pid_telem_i = Input(index=2, type=DataType.float)
    control_pid_telem_d = Input(index=3, type=DataType.float)
    control_pid_telem_n = Input(index=4, type=DataType.float)
    control_overwrite = Input(index=5, type=DataType.bit)
    solar_panel_state_0 = Input(index=6, type=DataType.bit)
    solar_panel_state_1 = Input(index=7, type=DataType.bit)
    solar_panel_state_2 = Input(index=8, type=DataType.bit)
    solar_panel_state_3 = Input(index=9, type=DataType.bit)
    solar_panel_state_4 = Input(index=10, type=DataType.bit)
    solar_panel_state_5 = Input(index=11, type=DataType.bit)
    solar_panel_state_6 = Input(index=12, type=DataType.bit)
    solar_panel_state_7 = Input(index=13, type=DataType.bit)
    solar_panel_state_8 = Input(index=14, type=DataType.bit)
    solar_panel_state_9 = Input(index=15, type=DataType.bit)
    advised_speed = Input(index=16, type=DataType.float)
