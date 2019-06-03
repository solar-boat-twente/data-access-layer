from datetime import time

import schedule

from bridge.data_bridge import DataBridge
from data_to_web_app.web_app_data import IntoQueue
from data_to_web_app.write_queue import SendData
from modbus import ModbusInstance

modbus_instance = ModbusInstance()


send_data = SendData()
into_queue = IntoQueue()

if __name__ == '__main__':

    #bridge = DataBridge()
    #bridge.open_pipes()
    send_data.start()
    into_queue.start()
    #modbus_instance.run(False)

