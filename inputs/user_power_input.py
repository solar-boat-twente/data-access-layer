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
    battery_state_of_charge = Input(index=13, type=DataType.float)
    battery_error_number = Input(index=14, type=DataType.string)
    battery_error_location = Input(index=15, type=DataType.string)
    battery_max_temp = Input(index=16, type=DataType.string)
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

    driver_motor_temp = Input(index=41, type=DataType.float)
    driver_driver_temp = Input(index=42, type=DataType.float)
    driver_motor_temp = Input(index=43, type=DataType.float)
    driver_driver_output_power = Input(index=44, type=DataType.float)
    driver_motor_speed = Input(index=45, type=DataType.float)
    driver_driver_voltage_input = Input(index=46, type=DataType.float)
    driver_driver_current_input = Input(index=47, type=DataType.float)
    driver_driver_state = Input(index=48, type=DataType.bit)

    solar_panel_state_0 = Input(index=49, type=DataType.bit)
    solar_panel_state_1 = Input(index=50, type=DataType.bit)
    solar_panel_state_2 = Input(index=51, type=DataType.bit)
    solar_panel_state_3 = Input(index=52, type=DataType.bit)
    solar_panel_state_4 = Input(index=53, type=DataType.bit)
    solar_panel_state_5 = Input(index=54, type=DataType.bit)
    solar_panel_state_6 = Input(index=55, type=DataType.bit)
    solar_panel_state_7 = Input(index=56, type=DataType.bit)
    solar_panel_state_8 = Input(index=57, type=DataType.bit)
    solar_panel_state_9 = Input(index=58, type=DataType.bit)

    throttle= Input(index=59, type=DataType.int)
    motor_state = Input(index=60, type=DataType.bit)
    contractor_control = Input(index=61, type=DataType.string)
    balancing_control = Input(index=62, type=DataType.string)
    error = Input(index=63, type=DataType.string)

    control_pid_state = Input(index=64, type=DataType.string)
    control_roll = Input(index=65, type=DataType.float)

    buttons_battery_on = Input(index=66, type=DataType.bit)
    buttons_force_battery = Input(index=67, type=DataType.bit)
    buttons_motor_on = Input(index=68, type=DataType.bit)
    buttons_deadmans_switch = Input(index=69, type=DataType.bit)
    buttons_solar_on = Input(index=70, type=DataType.bit)

    steer_raw_throttle = Input(index=71, type=DataType.string)
    steer_fly_mode = Input(index=72, type=DataType.string)
    steer_reverse = Input(index=73, type=DataType.bit)


class UserPowerInputInterpreter(DataInterpreter):

    def __init__(self, enum: Type[Enum]):
        super().__init__(enum)

        #self.on_change(UserPowerInputDef.baz, self.bla)

    def bla(self, c, v):
        pass
        #self.set(UserPowerInputDef.bar, v * 2)
