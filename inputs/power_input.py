from enum import Enum
from typing import Type

from bridge.data_interpreter import DataInterpreter
from bridge.data_type import DataType
from util.util_tuple import Input, Output


class PowerInputDef(Enum):

    battery_level = Input(index=0, type=DataType.int, modbus_ref=40002)
    speed = Input(index=1, type=DataType.int, modbus_ref=40003)
    min_speed = Input(index=2, type=DataType.int, modbus_ref=40004)
    max_speed = Input(index=3, type=DataType.int, modbus_ref=40005)
    advice_speed = Input(index=4, type=DataType.int, modbus_ref=40006)
    battery_temp = Input(index=5, type=DataType.int, modbus_ref=40007)
    motor_temp = Input(index=6, type=DataType.int, modbus_ref=40008)
    driver_temp = Input(index=7, type=DataType.int, modbus_ref=40009)
    height = Input(index=8, type=DataType.int, modbus_ref=40011)
    direction_forward = Input(index=9, type=DataType.bit, modbus_ref=7)
    direction_backward = Input(index=10, type=DataType.bit, modbus_ref=8)

    # mode_text = Output(type=DataType.string, modbus_ref=40010)  # Text currently hardcoded in HMI
    mode_1_active = Output(type=DataType.bit, modbus_ref=0)     # TODO CHANGE THIS WHEN MODE NUMBER CHANGES
    mode_2_active = Output(type=DataType.bit, modbus_ref=1)     # TODO CHANGE THIS WHEN MODE NUMBER CHANGES
    mode_3_active = Output(type=DataType.bit, modbus_ref=2)     # TODO CHANGE THIS WHEN MODE NUMBER CHANGES
    mode_4_active = Output(type=DataType.bit, modbus_ref=3)     # TODO CHANGE THIS WHEN MODE NUMBER CHANGES

    battery_danger = Output(type=DataType.bit, modbus_ref=4)    # TODO CHANGE THIS WHEN BATTERY TEMP. CHANGES
    driver_danger = Output(type=DataType.bit, modbus_ref=5)     # TODO CHANGE THIS WHEN DRIVER TEMP. CHANGES
    motor_danger = Output(type=DataType.bit, modbus_ref=6)      # TODO CHANGE THIS WHEN MOTOR TEMP. CHANGES
    connection_status = Output(type=DataType.int, modbus_ref=40012)


class PowerInputInterpreter(DataInterpreter):

    def __init__(self, enum: Type[Enum]):
        super().__init__(enum)
        self.set(PowerInputDef.mode_1_active, 1)
        self.set(PowerInputDef.mode_2_active, 0)
        self.set(PowerInputDef.mode_3_active, 0)
        self.set(PowerInputDef.mode_4_active, 0)
        self.set(PowerInputDef.battery_danger, 0)
        self.set(PowerInputDef.driver_danger, 0)
        self.set(PowerInputDef.motor_danger, 0)
        self.set(PowerInputDef.connection_status, 2)
