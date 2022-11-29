import canalystii, time
from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301, ReceievedMessage
from servo_realisation.robot.robot import Robot


def on_msg(msg: canalystii.protocol.Message):
    parsed = protoc.parse_recieve(msg)
    return parsed


def on_read_speed(receieved_message: ReceievedMessage):
    print('asgdrzsgdrg')

def on_read_accel(receieved_message: ReceievedMessage):
    print('zzzz')

def on_read_mode(receieved_message: ReceievedMessage):
    pass

def on_read_pos(receieved_message: ReceievedMessage):
    pass

def on_read_target_pos(receieved_message: ReceievedMessage):
    pass
        
def on_read_error_check(receieved_message: ReceievedMessage):
    pass
        
def on_voltage_check(receieved_message: ReceievedMessage):
    print('watagfak')
        
def on_temperature_check(receieved_message: ReceievedMessage):
    pass

def on_current_check(receieved_message: ReceievedMessage):
    pass
        
def on_pwm_check(receieved_message: ReceievedMessage):
    pass

def on_saved_parameters_check(receieved_message: ReceievedMessage):
    pass

def on_speed_loop_integration_time(receieved_message: ReceievedMessage):
    pass


interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301(interfec,
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




robt = Robot(5, protoc, assigned_servos_ids=[1, 2, 3, 5 , 6])

positions = {1: 32768*50/360*12, 
                2: 32768*50/360*12, 
                3: 32768*50/360*13, 
                5: 32768*50/360*43, 
                6: 32768*50/360*12,
                # 4: 32768*50/360*fourth_ser
                }

robt.set_target_pos(positions)
