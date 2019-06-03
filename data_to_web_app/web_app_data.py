import json
import time
from threading import Thread
from data_to_web_app import data_queue


class WebAppData:
    """
    Class containing all data that needs to go to the webapp on the brim.
    """
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.speed = None
        self.real_height = None
        self.real_roll = None
        self.computed_force_roll = None
        self.computed_force_pitch = None
        self.computed_force_height = None
        self.solar_input_panel_powers = None
        self.battery_max_temp = None
        self.battery_state_of_charge = None
        self.total_voltage = None
        self.total_current = None
        self.steer_raw_throttle = None
        self.steer_fly_mode = None
        self.driver_motor_temp = None
        self.driver_driver_temp = None
        self.driver_driver_output_power = None
        self.driver_driver_voltage_input = None
        self.driver_driver_current_input = None
        self.driver_on = None
        self.driver_driver_state = None
        self.driver_motor_speed = None


class IntoQueue(Thread):
    def __init__(self):
        super().__init__()
        #self.data = data

    def to_json(self, object):
        #print("Object is ", object)
        return json.dumps(object.__dict__)

    def run(self):
        while True:
            print("Into queue")
            json_data = self.to_json(web_app_data)
            data_queue.data_queue.put(json_data)
            time.sleep(1)


web_app_data = WebAppData()

