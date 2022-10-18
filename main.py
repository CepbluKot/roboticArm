from time import sleep
import threading
import canalystii
import time
import servo_realisation.servo
import servo_realisation.commands_constructor.commands_constructor_abstraction
import servo_realisation.commands_constructor.commands_constructor
from servo_realisation.servo import (
    # Servo,
    ServoPdoControlTheProcessOfFindingTheOrigin,
    ServoPdoPositionInterpolationMode,
    ServoSdoAbsolutePositionMode,
    ServoPdoSpeedMode,
    ServoSdoAbsolutePositionMode,
    ServoSdoRelativePositionMode,
    ServoSdoSpeedMode,
)
from servo_realisation.servo_abstraction import (
    ServoPdoControlTheProcessOfFindingTheOriginAbstraction,
    ServoPdoPositionInterpolationModeAbstraction,
    ServoPdoAbsolutePositionModeAbstraction,
    ServoPdoSpeedModeAbstraction,
    ServoSdoAbsolutePositionModeAbstraction,
    ServoSdoRelativePositionModeAbstraction,
    ServoSdoSpeedModeAbstraction,
)

import servo_realisation.commands_constructor.commands_constructor
import servo_realisation.commands_constructor.commands_constructor_abstraction
import servo_realisation.servo_commands.commands

srv = servo_realisation.servo.Servo(device_id=0)
servo_sdo_speed_mode = ServoSdoSpeedMode(servo_interface=srv)
servo_sdo_speed_mode_abs = ServoSdoSpeedModeAbstraction(
    servo_interface=srv, servo_sdo_speed_mode_interface=servo_sdo_speed_mode
)

servo_pdo_speed_mode = ServoPdoSpeedMode(servo_interface=srv)
servo_pdo_speed_mode_abs = ServoPdoSpeedModeAbstraction(
    servo_interface=srv, servo_pdo_speed_mode_interface=servo_pdo_speed_mode
)


constructr = (
    servo_realisation.commands_constructor.commands_constructor.CommandConstructor(
        servo_object=srv
    )
)
constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(
    interface=constructr
)

# # servo_sdo_speed_mode_abs.speed_mode()
# # sleep(5)

# set_zero_1_1 = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=6,
#     data=(0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA),
# )

# set_zero_2_1 = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=6,
#     data=(0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA),
# )



# set_zero_1_2 = canalystii.Message(
#     can_id=0x602,
#     remote=False,
#     extended=False,
#     data_len=6,
#     data=(0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA),
# )

# set_zero_2_2 = canalystii.Message(
#     can_id=0x602,
#     remote=False,
#     extended=False,
#     data_len=6,
#     data=(0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA),
# )

# # set_abs_mode = canalystii.Message(
# #     can_id=0x601,
# #     remote=False,
# #     extended=False,
# #     data_len=5,
# #     data=(0x2F, 0x60, 0x60, 0x00, 0x01),
# # )

# set_pos_msg_ob = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=8,
#     data=(0x23, 0x7A, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00),
# )

# set_pos_msg_zero = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=8,
#     data=(0x23, 0x7A, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00),
# )

# read_pos_msg = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=4,
#     data=(0x40, 0x64, 0x60, 0x00),
# )

# activate = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=6,
#     data=(0x2B, 0x40, 0x60, 0x00, 0x2F, 0x00),
# )

# msg_80 = canalystii.Message(
#     can_id=0x00, remote=False, extended=False, data_len=1, data=(0x80,)
# )


# read_voltage = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=4,
#     data=(0x40, 0x79, 0x60, 0x00),
# )

# read_acc = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=4,
#     data=(0x40, 0x83, 0x60, 0x00),
# )

# set_acc = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=8,
#     data=(0x23, 0x83, 0x60, 0x00, 0xB8, 0x0B, 0x00, 0x00),
# )

# set_speed = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=8,
#     data=(0x23, 0x81, 0x60, 0x00, 0x2C, 0x01, 0x00, 0x00),
# )

# # set_target_pos = canalystii.Message(
# #     can_id=0x502,
# #     remote=False,
# #     extended=False,
# #     data_len=4,
# #     data=(0x00, 0x00 , 0x00, 0x00),
# # )

# start_move_to_target_pos = canalystii.Message(
#     can_id=0x80,
#     remote=False,
#     extended=False,
#     data_len=0,
#     data=(0x80,),
# )


# set_speed = constructor_abs.create_command(
#     command_from_documentation="60810020", is_write=1, address=0x601, write_value=500
# )


# # speed_mode = constructor_abs.create_command(
# #     command_from_documentation="60600008", is_write=1, address=0x601, write_value=1
# # )


# abs_mode = constructor_abs.create_command(
#     command_from_documentation='60400010',
#     is_write=True,
#     write_value=47,
#     address=0x601
# )

# print(abs_mode)


# position = constructor_abs.create_command(
#     command_from_documentation="607A0020", is_write=1, address=0x601, write_value=32000*30
# )



# servo1 = servo_realisation.servo_commands.commands.ControlServo(servo_object=srv)



# # servo1.set_movements_speed(700)
# # servo1.simple_move_to_position(position=32000*50)


ser = servo_realisation.commands_constructor.commands_constructor.CommandConstructor(servo_object=srv)
ser_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(ser)


# # change_mode = ser_abs.create_command(
# #                 command_from_documentation="60600008", is_write=1, address=0x601, write_value=1
# #             )

# # com_b = ser_abs.create_command(
# #                 command_from_documentation="607A0020", is_write=1, address=0x601, write_value=32000*50
# #             )

# # srv.send(channel=0, messages=read_pos_msg)

# # reciv = srv.receive(channel=0)
# # while not reciv:
# #     reciv = srv.receive(channel=0)
# # print(reciv)

# # -------------------------



# # sleep(0.1)
# # srv.send(channel=0, messages=set_zero_1_2)
# # sleep(0.1)
# # srv.send(channel=0, messages=set_zero_2_2)
# # sleep(0.1)


# # sleep(0.1)
# # srv.send(channel=0, messages=set_zero_1_1)
# # sleep(0.1)
# # srv.send(channel=0, messages=set_zero_2_1)
# # sleep(0.1)



# change_mode = ser_abs.create_command(
#                 command_from_documentation="60600008", is_write=1, address=0x601, write_value=1
#             )



# set_target_pos_2 = canalystii.Message(
#     can_id=0x502,
#     remote=False,
#     extended=False,
#     data_len=4,
#     data=(0x00, 0x00 , 0x00, 0x00),
# )


# set_target_pos_1 = canalystii.Message(
#     can_id=0x501,
#     remote=False,
#     extended=False,
#     data_len=4,
#     data=(0x00, 0x0E , 0x38, 0x16),
# )


# write_speed_1 = ser_abs.create_command(
#                 command_from_documentation="60810020", is_write=1, address=0x601, write_value=5
#             )


# write_speed_2 = ser_abs.create_command(
#                 command_from_documentation="60810020", is_write=1, address=0x602, write_value=5
#             )



# srv.send(channel=0, messages=write_speed_1)
# sleep(0.1)


# print('changen sped')
# begin = time.time()

# while time.time() - begin < 2:
#     rec = srv.receive(0)
#     while not rec:

#         rec = srv.receive(0)

#     print('print in loop -> ', rec)

# # srv.send(channel=0, messages=write_speed_2)
# # sleep(0.1)


# smth = ser_abs.create_command(command_from_documentation='60FD0010', is_read=1, address=0x601)
# get_pos = ser_abs.create_command(command_from_documentation='26190010', is_read=1, address=0x601)
# get_signalisation = ser_abs.create_command(command_from_documentation='260E0010', is_read=1, address=0x601)




# set_pos_msg_zero = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=8,
#     data=(0x23, 0x7A, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00),
# )


# set_pos_msg_zero = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=8,
#     data=(0x23, 0x7A, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00),
# )


# change_mode_1 = ser_abs.create_command(
#                 command_from_documentation="60600008", is_write=1, address=0x601, write_value=1
#             )
# change_mode_2 = ser_abs.create_command(
#                 command_from_documentation="60600008", is_write=1, address=0x602, write_value=1
#             )

# sleep(0.1)
# srv.send(channel=0, messages=change_mode_1)
# sleep(0.1)


# print('moode')
# begin = time.time()

# while time.time() - begin < 2:
#     rec = srv.receive(0)
#     while not rec:

#         rec = srv.receive(0)

#     print('print in loop -> ', rec)

# # sleep(0.1)
# # srv.send(channel=0, messages=change_mode_2)
# # sleep(0.1)




# # srv.send(channel=0, messages=get_pos)
# sleep(0.1)
# srv.send(channel=0, messages=set_target_pos_1)
# sleep(0.1)

# print('torget pos ')
# begin = time.time()

# while time.time() - begin <2:
#     rec = srv.receive(0)
#     while not rec:
#         # sleep(0.1)
#         # srv.send(channel=0, messages=get_pos)
#         # sleep(0.1)
#         rec = srv.receive(0)

#     print('print in loop -> ', rec)

# # srv.send(channel=0, messages=set_target_pos_2)
# # sleep(0.1)
# srv.send(channel=0, messages=start_move_to_target_pos)

# print('MOOVE')
# begin = time.time()

# while time.time() - begin < 2:
#     rec = srv.receive(0)
#     while not rec:

#         rec = srv.receive(0)

#     print('print in loop -> ', rec)

# # sleep(0.1)

# # --------------------------


# change_id = ser_abs.create_command(
#                 command_from_documentation="26150010", is_write=1, address=0x601, write_value=2
#             )


# save = ser_abs.create_command(
#                 command_from_documentation="26140010", is_write=1, address=0x601, write_value=1
#             )

# read_speed = ser_abs.create_command(
#                 command_from_documentation="60810020", is_read=1, address=0x602
#             )




# srv.send(channel=0, messages=change_id)

# srv.send(channel=0, messages=read_speed)


# srv.send(channel=0, messages=get_pos)


signalization = ser_abs.create_command(command_from_documentation='260E0010', is_read=1, address=0x602)
# ^^^ check errors 
# check page 7


srv.send(channel=0, messages=signalization)

begin = time.time()

while time.time() - begin < 5:
    rec = srv.receive(0)
    while not rec:

        rec = srv.receive(0)

    print('print in loop -> ', rec)

srv.stop(0)
srv.stop(1)
