import canalystii, time
from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301
from servo_realisation.robot.robot import Robot
from gui.output import init_gui


axis_data = {}

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
robt = Robot(5, protoc, assigned_servos_ids=[1, 2, 3, 5, 6])

robt.set_mode(1)
robt.set_speed(60)
robt.set_acceleration(20)

time.sleep(2)

# protoc.read_error_checker(1)

# protoc.read_error_checker(4)

def interpolation_call():
    data = {}
    for axis_id in axis_data:
        data[axis_id] = axis_data[axis_id]()


    first_ser = int(float(data[1]))
    sec_ser =int(float(data[2]))
    thir_ser = int(float(data[3]))
    # fourth_ser =int(float(data[4]))
    fifth_ser =int(float(data[5]))
    sixth_ser =int(float(data[6]))


    positions = {1: 32768*50/360*first_ser, 
                2: 32768*50/360*sec_ser, 
                3: 32768*50/360*thir_ser, 
                5: 32768*50/360*fifth_ser, 
                6: 32768*50/360*sixth_ser,
                # 4: 32768*50/360*fourth_ser
                }

    robt.set_target_pos(positions)

    while not protoc.check_is_buffer_empty():
        print('waitin for buff!')
    robt.move()


def get_speed_call():
    return robt.read_speed(1)

def get_accel_call():
    print('accel',robt.read_acceleration(1))
    return robt.read_acceleration(1)

def get_sync_call():
    # robt.set_speed(60)
    return -1


def set_speed_call(value):
    robt.set_speed(float(value))

def set_accel_call(value):
    robt.set_acceleration(float(value))

def set_sync_call(value):
    # robt.set_speed(60)
    pass


save_settings_call = protoc.send_save

def set_zero_pos_first_axis_call():
    robt.set_zero_pos(1)

def set_zero_pos_sec_axis_call():
    robt.set_zero_pos(2)

def set_zero_pos_third_axis_call():
    robt.set_zero_pos(3)

def set_zero_pos_fourth_axis_call():
    robt.set_zero_pos(4)

def set_zero_pos_fifth_axis_call():
    robt.set_zero_pos(5)

def set_zero_pos_sixth_axis_call():
    robt.set_zero_pos(6)


# -------------


def save_settings_first_axis_call():
    robt.save_settings(1)

def save_settings_sec_axis_call():
    robt.save_settings(2)

def save_settings_third_axis_call():
    robt.save_settings(3)

def save_settings_fourth_axis_call():
    robt.save_settings(4)

def save_settings_fifth_axis_call():
    robt.save_settings(5)

def save_settings_sixth_axis_call():
    robt.save_settings(6)


set_zero_pos_calls = {1:set_zero_pos_first_axis_call, 2:set_zero_pos_sec_axis_call, 3:set_zero_pos_third_axis_call, 4:set_zero_pos_fourth_axis_call, 5:set_zero_pos_fifth_axis_call, 6:set_zero_pos_sixth_axis_call} 
save_settings_calls = {1:save_settings_first_axis_call, 2:save_settings_sec_axis_call, 3:save_settings_third_axis_call, 4:save_settings_fourth_axis_call, 5:save_settings_fifth_axis_call, 6:save_settings_sixth_axis_call}

init_gui(interpolation_call=interpolation_call, get_axis_value_funcs_dict=axis_data, set_speed_call=set_speed_call, set_accel_call=set_accel_call, set_sync_call=set_sync_call, get_speed_call=get_speed_call, get_accel_call=get_accel_call, get_sync_call=get_sync_call, set_zero_pos_calls=set_zero_pos_calls, save_settings_calls=save_settings_calls)
