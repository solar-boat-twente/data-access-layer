from enum import Enum
from typing import Type

from bridge.data_interpreter import DataInterpreter
from bridge.data_type import DataType
from util.util_tuple import Input, Output

""" 
class ControlDataInputDef(Enum):

    foo = Input(index=0, type=DataType.int)
    baz = Input(index=1, type=DataType.float, modbus_ref=40001)
    bar = Output(type=DataType.int, modbus_ref=40001)
"""
class UserPowerInputDef(Enum):

    foo = Input(index=0, type=DataType.int)
    baz = Input(index=1, type=DataType.float, modbus_ref=40001)
    bar = Output(type=DataType.int, modbus_ref=40001)


class UserPowerInputInterpreter(DataInterpreter):

    def __init__(self, enum: Type[Enum]):
        super().__init__(enum)

        self.on_change(UserPowerInputDef.baz, self.bla)

    def bla(self, c, v):
        self.set(UserPowerInputDef.bar, v * 2)
