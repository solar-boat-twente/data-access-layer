from enum import Enum
from typing import Type, Callable

from util.util_logging import log
from util.util_tuple import Input


class DataInterpreter:

    def __init__(self, enum: Type[Enum]):
        self.__inputs = dict()
        self.__data = dict()
        self.__enum = enum
        self.__change_events = {}
        self.__map_inputs()

    def __map_inputs(self):
        for constant in self.__enum:
            def_value = constant.value
            if not def_value:
                continue

            if isinstance(def_value, Input):
                def_index = def_value.index

                if not def_value.type:
                    raise AttributeError('Missing required attribute "%s"' % 'type')

                if def_index is not None:
                    self.__inputs[def_index] = constant

        log('Mapped all input attributes and linked them to indexes')

    def interpret(self, string: str):
        data = string.split(',')
        for index, constant in self.__inputs.items():
            try:
                data_value = data[index]
                data_type = constant.value.type
                data_parser = data_type.value[0]

                if data_parser:
                    data_value = data_parser(data_value)
                self.set(constant, data_value)

            except IndexError:
                default = constant.value.default
                if default is not None:
                    self.set(constant, default)

                continue

    def set(self, constant: Enum, value: object, call_event: bool = True):
        self.__data[constant] = value

        if isinstance(constant.value, Input):
            data_type = constant.value.out_type or constant.value.type
        else:
            data_type = constant.value.type

        modbus_ref = constant.value.modbus_ref
        modbus_write = data_type.value[1]
        event_handler = self.__change_events.get(constant)

        if call_event and event_handler:
            event_handler(constant, value)

        if modbus_ref is not None and modbus_write:
            from app import modbus_instance
            getattr(modbus_instance, modbus_write)(modbus_ref, value)

        log('Updated attribute %s with value %s' % (constant.name, value))

    def get(self, constant: Enum) -> object:
        return self.__data.get(constant)

    def on_change(self, constant: Enum, callback: Callable[[object], None]):
        self.__change_events[constant] = callback

    def __flush(self):
        pass






