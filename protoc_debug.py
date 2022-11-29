import canalystii, time
from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301, ReceievedMessage


def on_msg(msg: canalystii.protocol.Message):
    parsed = protoc.parse_recieve(msg)
    return parsed


def on_accel(receieved_message):
    pass

def on_mode(receieved_message):
    pass


def on_pos(receieved_message):
    pass


def on_speed(receieved_message: ReceievedMessage):
    pass


def on_target_pos(receieved_message: ReceievedMessage):
    print('woah', receieved_message.decoded_data)


def on_error_check(receieved_message):
    pass

def on_voltage(receieved_message: ReceievedMessage):
    print('voltage', receieved_message.decoded_data/327)

interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301(interfec, on_speed, on_accel, on_mode, on_pos, on_target_pos,on_error_check, on_voltage)


protoc.read_voltage(1)
