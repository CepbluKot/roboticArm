import canalystii
from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301
from servo_realisation.robot.robot import Robot
from gui.calls.get_params_calls import *


def on_msg(msg: canalystii.protocol.Message):
    parsed = protocol.parse_recieve(msg)
    return parsed

hardware_interface = USB_CAN.USB_CAN(0, 1000000, on_msg)

protocol = CanOpen301(hardware_interface,
        on_read_speed,
        on_read_accel,
        on_read_mode,
        on_read_pos,
        on_read_target_pos,
        on_read_error_check,
        on_voltage_check,
        on_temperature_check,
        on_current_check,
        on_pwm_check,
        on_saved_parameters_check,
        on_speed_loop_integration_time,)

robot = Robot(6, protocol, assigned_servos_ids=[1, 2, 3, 5 , 4, 6])
