from bridge.data_bridge import DataBridge
from modbus import ModbusInstance

modbus_instance = ModbusInstance()


if __name__ == '__main__':

    bridge = DataBridge()
    bridge.open_pipes()

    modbus_instance.run(False)
