from enum import Enum
from typing import Type

from bridge.data_interpreter import DataInterpreter
from bridge.data_type import DataType
from util.util_tuple import Input, Output


class UserPowerInputDef(Enum):

    timestamp = Input(index=0, type=DataType.string)
    battery_cell_voltage_0 = Input(index=1, type=DataType.float)
    battery_cell_voltage_1 = Input(index=2, type=DataType.float)
    battery_cell_voltage_2 = Input(index=3, type=DataType.float)
    battery_cell_voltage_3 = Input(index=4, type=DataType.float)
    battery_cell_voltage_4 = Input(index=5, type=DataType.float)
    battery_cell_voltage_5 = Input(index=6, type=DataType.float)
    battery_cell_voltage_6 = Input(index=7, type=DataType.float)
    battery_cell_voltage_7 = Input(index=8, type=DataType.float)
    battery_cell_voltage_8 = Input(index=9, type=DataType.float)
    battery_cell_voltage_9 = Input(index=10, type=DataType.float)
    battery_cell_voltage_10 = Input(index=11, type=DataType.float)
    battery_cell_voltage_11 = Input(index=12, type=DataType.float)
    battery_state_of_charge = Input(index=13, type=DataType.float, out_type=DataType.int, modbus_ref=40002)
    battery_error_number = Input(index=14, type=DataType.string)
    battery_error_location = Input(index=15, type=DataType.string)
    battery_max_temp = Input(index=16, type=DataType.int, modbus_ref=40007)
    battery_min_temp = Input(index=17, type=DataType.string)
    battery_balance_state = Input(index=18, type=DataType.bit)
    battery_contactor_ready = Input(index=19, type=DataType.bit)
    battery_contactor_status = Input(index=20, type=DataType.bit)

    solar_panels_mttp_power_0 = Input(index=21, type=DataType.float)
    solar_panels_mttp_power_1 = Input(index=22, type=DataType.float)
    solar_panels_mttp_power_2 = Input(index=23, type=DataType.float)
    solar_panels_mttp_power_3 = Input(index=24, type=DataType.float)
    solar_panels_mttp_power_4 = Input(index=25, type=DataType.float)
    solar_panels_mttp_power_5 = Input(index=26, type=DataType.float)
    solar_panels_mttp_power_6 = Input(index=27, type=DataType.float)
    solar_panels_mttp_power_7 = Input(index=28, type=DataType.float)
    solar_panels_mttp_power_8 = Input(index=29, type=DataType.float)
    solar_panels_mttp_power_9 = Input(index=30, type=DataType.float)

    solar_panels_panel_power_0 = Input(index=31, type=DataType.float)
    solar_panels_panel_power_1 = Input(index=32, type=DataType.float)
    solar_panels_panel_power_2 = Input(index=33, type=DataType.float)
    solar_panels_panel_power_3 = Input(index=34, type=DataType.float)
    solar_panels_panel_power_4 = Input(index=35, type=DataType.float)
    solar_panels_panel_power_5 = Input(index=36, type=DataType.float)
    solar_panels_panel_power_6 = Input(index=37, type=DataType.float)
    solar_panels_panel_power_7 = Input(index=38, type=DataType.float)
    solar_panels_panel_power_8 = Input(index=39, type=DataType.float)
    solar_panels_panel_power_9 = Input(index=40, type=DataType.float)

    driver_motor_temp = Input(index=41, type=DataType.float, out_type=DataType.int, modbus_ref=40008)
    driver_driver_temp = Input(index=42, type=DataType.float, out_type=DataType.int, modbus_ref=40009)
    driver_driver_output_power = Input(index=43, type=DataType.float)
    driver_motor_speed = Input(index=43, type=DataType.float)
    driver_driver_voltage_input = Input(index=45, type=DataType.float)
    driver_driver_current_input = Input(index=46, type=DataType.float)
    driver_driver_state = Input(index=47, type=DataType.bit)

    solar_panel_state_0 = Input(index=48, type=DataType.bit)
    solar_panel_state_1 = Input(index=49, type=DataType.bit)
    solar_panel_state_2 = Input(index=50, type=DataType.bit)
    solar_panel_state_3 = Input(index=51, type=DataType.bit)
    solar_panel_state_4 = Input(index=52, type=DataType.bit)
    solar_panel_state_5 = Input(index=53, type=DataType.bit)
    solar_panel_state_6 = Input(index=54, type=DataType.bit)
    solar_panel_state_7 = Input(index=55, type=DataType.bit)
    solar_panel_state_8 = Input(index=56, type=DataType.bit)
    solar_panel_state_9 = Input(index=57, type=DataType.bit)

    throttle = Input(index=58, type=DataType.int)
    motor_state = Input(index=59, type=DataType.bit)
    contractor_control = Input(index=60, type=DataType.string)
    balancing_control = Input(index=61, type=DataType.string)
    #error = Input(index=63, type=DataType.string)


    control_pid_roll = Input(index=62, type=DataType.float, out_type=DataType.int, modbus_ref=40014)
    control_pid_pitch = Input(index=63, type=DataType.float)
    control_pid_height = Input(index=64, type=DataType.float)

    buttons_battery_on = Input(index=65, type=DataType.bit)
    buttons_force_battery = Input(index=66, type=DataType.bit)
    buttons_motor_on = Input(index=67, type=DataType.bit)
    buttons_debug_on = Input(index=68, type=DataType.bit)

    steer_raw_throttle = Input(index=69, type=DataType.string)
    steer_fly_mode = Input(index=70, type=DataType.string)
    steer_reverse = Input(index=71, type=DataType.bit)

    total_voltage = Input(index=72, type=DataType.float)
    total_current = Input(index=73, type=DataType.float)
    driver_on = Input(index=74, type=DataType.bit)
    error_word = Input(index=75, type=DataType.bit)
    low_priority_limiter = Input(index=76, type=DataType.bit)
    real_throttle = Input(index=77, type=DataType.float)


    fly_mode_1 = Output(type=DataType.bit, modbus_ref=0)
    fly_mode_2 = Output(type=DataType.bit, modbus_ref=1)
    fly_mode_3 = Output(type=DataType.bit, modbus_ref=2)
    fly_mode_4 = Output(type=DataType.bit, modbus_ref=3)
    direction_forward = Output(type=DataType.bit, modbus_ref=7)
    direction_backward = Output(type=DataType.bit, modbus_ref=8)
    battery_temperature_danger = Output(type=DataType.bit, modbus_ref=4)
    driver_temperature_danger = Output(type=DataType.bit, modbus_ref=5)
    motor_temperature_danger = Output(type=DataType.bit, modbus_ref=6)


class UserPowerInputInterpreter(DataInterpreter):

    def __init__(self, enum: Type[Enum]):
        super().__init__(enum)
        self.on_change(UserPowerInputDef.steer_fly_mode, self.on_fly_mode_change)
        self.on_change(UserPowerInputDef.steer_reverse, self.on_steer_reverse_change)
        self.on_change(UserPowerInputDef.driver_motor_temp, self.on_motor_temperature_change)
        self.on_change(UserPowerInputDef.driver_driver_temp, self.on_driver_temperature_change)
        self.on_change(UserPowerInputDef.battery_max_temp, self.on_battery_temperature_change)

    def on_fly_mode_change(self, value: str):
        mapping = {
            'FLY': UserPowerInputDef.fly_mode_4,
            'Bridge': UserPowerInputDef.fly_mode_3,
            'NO_FLY': UserPowerInputDef.fly_mode_2,
            'Slalom': UserPowerInputDef.fly_mode_1
        }

        def set_bit(definition: Enum, enum: Enum):
            self.set(enum, 1 if definition == enum else 0)

        mapped_def = mapping.get(value)
        if mapped_def:
            set_bit(mapped_def, UserPowerInputDef.fly_mode_1)
            set_bit(mapped_def, UserPowerInputDef.fly_mode_2)
            set_bit(mapped_def, UserPowerInputDef.fly_mode_3)
            set_bit(mapped_def, UserPowerInputDef.fly_mode_4)

    def on_steer_reverse_change(self, is_backwards: int):
        self.set(UserPowerInputDef.direction_forward, int(not is_backwards))
        self.set(UserPowerInputDef.direction_backward, is_backwards)

    def on_motor_temperature_change(self, temperature: float):
        min_temp = 10
        max_temp = 50

        is_safe = min_temp < temperature < max_temp
        self.set(UserPowerInputDef.motor_temperature_danger, int(is_safe))

    def on_driver_temperature_change(self, temperature: float):
        min_temp = 10
        max_temp = 50

        is_safe = min_temp < temperature < max_temp
        self.set(UserPowerInputDef.driver_temperature_danger, int(not is_safe))

    def on_battery_temperature_change(self, temperature: int):
        min_temp = 10
        max_temp = 50

        is_safe = min_temp < temperature < max_temp
        self.set(UserPowerInputDef.battery_temperature_danger, int(not is_safe))
