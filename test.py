import canalystii, ctypes, time

from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301
from servo_realisation.robot.robot import Robot


def on_msg(msg: canalystii.protocol.Message):
    return protoc.parse_recieve(msg)


def smth(a,):
    pass


interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301(interfec, smth, smth, smth, smth, smth)


robt = Robot(5, protoc, assigned_servos_ids=[1, 2, 3, 5, 6])


# robt.set_mode(1)
robt.set_speed(30)
# robt.set_acceleration(10)
# while  not protoc.check_is_buffer_empty():
#     pass
# print('done')

positions = {1: 0, 2: 0, 3: 32768*50/360*20, 5: 32768*30*0, 6: 0}

robt.set_target_pos(positions)

while  not protoc.check_is_buffer_empty():
    pass

robt.move()
