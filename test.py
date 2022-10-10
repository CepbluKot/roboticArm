from time import sleep
import canalystii
import time
from servo_realisation.servo import Servo, ServoPdoControlTheProcessOfFindingTheOrigin, ServoPdoPositionInterpolationMode, ServoSdoAbsolutePositionMode, ServoPdoSpeedMode, ServoSdoAbsolutePositionMode, ServoSdoRelativePositionMode, ServoSdoSpeedMode
from servo_realisation.servo_abstraction import ServoPdoControlTheProcessOfFindingTheOriginAbstraction, ServoPdoPositionInterpolationModeAbstraction, ServoPdoAbsolutePositionModeAbstraction, ServoPdoSpeedModeAbstraction, ServoSdoAbsolutePositionModeAbstraction, ServoSdoRelativePositionModeAbstraction, ServoSdoSpeedModeAbstraction


# dev = canalystii.CanalystDevice(bitrate=1000000, device_index=0)



# new_message = canalystii.Message(
#     can_id=0x401,
#     remote=False,
#     extended=False,
#     data_len=7,
#     data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
# )

# new_message = canalystii.Message(
#     can_id=0x141,
#     remote=False,
#     extended=False,
#     # data_len=0,
#     # data=(0x00, )
# )

# dev.send(0, new_message)


# print(dev.receive(1))
srv = Servo(device_id=0)
servo_sdo_speed_mode = ServoSdoSpeedMode(servo_interface=srv)
servo_sdo_speed_mode_abs = ServoSdoSpeedModeAbstraction(servo_interface=srv, servo_sdo_speed_mode_interface=servo_sdo_speed_mode)

servo_pdo_speed_mode = ServoPdoSpeedMode(servo_interface=srv)
servo_pdo_speed_mode_abs = ServoPdoSpeedModeAbstraction(servo_interface=srv, servo_pdo_speed_mode_interface=servo_pdo_speed_mode)



# print(servo_sdo_speed_mode_abs.speed_mode())
# sleep(5)


# new_message = canalystii.Message(
#     can_id=0x601,
#     remote=False,
#     extended=False,
#     data_len=5,
#     data=(0x2F, 0x60, 0x60, 0x00, 0x01 )
# )

new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=8,
    data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00  )
)

srv.send(channel=0, messages=new_message)

begin = time.time()


while time.time() - begin < 2:
    
    rec = srv.receive(0)
    while not rec:
        rec = srv.receive(0)

    print(rec)

# servo_pdo_speed_mode_abs.control_word_working_mode_target_speed_current_position_status_word(speed=0)

srv.stop(0)
srv.stop(1)
