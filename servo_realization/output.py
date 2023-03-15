import canalystii
from servo_realization.hardware_interface import USB_CAN
from servo_realization.protocol_interface.CanOpen301 import CanOpen301, ReceivedMessage
from servo_realization.robot.robot import Robot
from servo_realization.robot.servo_motor import ServoMotorAliexpress
from gui.calls.get_params_calls import *
from servo_realization.control_algorithms.controlAlgorithms import ControlAlgorithms


def on_usbcan_msg(msg: canalystii.protocol.Message):
    parsed = protocol.parse_recieve(msg)
    return parsed

def on_read_speed_global_call(receieved_message: ReceivedMessage):
    on_read_speed_gui_call(receieved_message)
    robot.update_speed_callback(servo_id=receieved_message.servo_id, value=receieved_message.decoded_data)

def on_read_accel_global_call(receieved_message: ReceivedMessage):
    on_read_accel_gui_call(receieved_message)
    robot.update_acceleration_callback(servo_id=receieved_message.servo_id, value=receieved_message.decoded_data)

def on_read_mode_global_call(receieved_message: ReceivedMessage):
    on_read_mode_gui_call(receieved_message)
    robot.update_mode_callback(servo_id=receieved_message.servo_id, value=receieved_message.decoded_data)

def on_read_pos_global_call(receieved_message: ReceivedMessage):
    on_read_pos_gui_call(receieved_message)
    robot.update_position_callback(servo_id=receieved_message.servo_id, value=receieved_message.decoded_data)

hardware_interface = USB_CAN.USB_CAN(0, 1000000, on_usbcan_msg)

protocol = CanOpen301(hardware_interface,
        on_read_speed_global_call,
        on_read_accel_global_call,
        on_read_mode_global_call,
        on_read_pos_global_call,
        on_read_target_pos_gui_call,
        on_read_error_check_gui_call,
        on_voltage_check_gui_call,
        on_temperature_check_gui_call,
        on_current_check_gui_call,
        )

axis_1 = ServoMotorAliexpress(id=1, pulses_per_revolution=32768, gearbox_value=50, protocol=protocol)
axis_2 = ServoMotorAliexpress(id=2, pulses_per_revolution=32768, gearbox_value=50, protocol=protocol)
axis_3 = ServoMotorAliexpress(id=3, pulses_per_revolution=32768, gearbox_value=50, protocol=protocol)
axis_4 = ServoMotorAliexpress(id=4, pulses_per_revolution=32768, gearbox_value=50, protocol=protocol)
axis_5 = ServoMotorAliexpress(id=5, pulses_per_revolution=32768, gearbox_value=50, protocol=protocol)
axis_6 = ServoMotorAliexpress(id=6, pulses_per_revolution=32768, gearbox_value=50, protocol=protocol)


robot = Robot(5, servos=[axis_1, axis_2, axis_3, axis_4, axis_6])

control_algorithms = ControlAlgorithms(robot_obj=robot)
