import canalystii, ctypes, time

from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface import CanOpen301


def on_msg(msg: canalystii.protocol.Message):

    z = protoc.parse_recieve(msg)
    print("decod", z.decoded_data, msg)
    return protoc.parse_recieve(msg)


def smth(a,):
    pass


interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301.CanOpen301(interfec, smth, smth, smth, smth, smth)
# interfec.open_connection()


def prp(id):
    protoc.send_speed(id, 1)
    protoc.send_acceleration(id, 1)
    protoc.send_mode(id, 1)
    protoc.send_target_pos(id, 0)


# for i in range(1, 3):
#     prp(i)
# prp(5)
prp(6)

protoc.send_general_move_command()
