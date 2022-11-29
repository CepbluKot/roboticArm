import canalystii, time
from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301


def on_msg(msg: canalystii.protocol.Message):
    parsed = protoc.parse_recieve(msg)
    return parsed


def modify_accel(axis_id, value):
    pass

def modify_mode(axis_id, value):
    pass


def modify_pos(axis_id, value):
    pass


def modify_speed(axis_id, value):
    pass


def modify_target_pos(axis_id, value):
    pass


interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301(interfec, modify_speed, modify_accel, modify_mode, modify_pos, modify_target_pos)

protoc.read_error_checker(5)
