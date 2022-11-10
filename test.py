import canalystii, ctypes, time

from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface import CanOpen301


def on_msg(msg: canalystii.protocol.Message):

    z = protoc.parse_recieve(msg)
    # print("decod", z.decoded_data, msg)
    return protoc.parse_recieve(msg)


def smth(a,):
    pass


interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301.CanOpen301(interfec, smth, smth, smth, smth, smth)


# while 1:
#     print("BEGIN SEND")
#     protoc.read_speed(6)
#     protoc.read_speed(5)
#     protoc.read_accelearation(6)
#     protoc.read_accelearation(5)
#     time.sleep(5)


protoc.send_speed(5, 10)
protoc.read_speed(5)
while not protoc.check_is_buffer_empty():
    pass

print('done')

