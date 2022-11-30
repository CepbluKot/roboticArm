import canalystii, time, threading
from tkinter.ttk import  Treeview

from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301, ReceievedMessage
from servo_realisation.robot.robot import Robot
from gui.output import init_gui
from gui.general_params_tab.storages.output import general_params_repo


axis_data = {}

def on_msg(msg: canalystii.protocol.Message):
    parsed = protoc.parse_recieve(msg)
    return parsed

def on_read_speed(receieved_message: ReceievedMessage):
    widget = general_params_repo.get(receieved_message.servo_id, 'speed')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_accel(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'accel')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_mode(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'mode')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_pos(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'positon')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_target_pos(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'target position')
    if widget:
        widget.config(text=receieved_message.decoded_data)
        
def on_read_error_check(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'error code')
    if widget:
        widget.config(text=receieved_message.decoded_data)
        
def on_voltage_check(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'voltage')
    if widget:
        widget.config(text=receieved_message.decoded_data/327)
        
def on_temperature_check(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'temperature')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_current_check(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'current')
    if widget:
        widget.config(text=receieved_message.decoded_data)
        
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

robt.set_mode(1)
robt.set_speed(60)
robt.set_acceleration(20)



def interpol_call_for_thread():
    data = {}
    for axis_id in axis_data:
        data[axis_id] = axis_data[axis_id]()


    first_ser = round(float(data[1]))
    sec_ser =round(float(data[2]))
    thir_ser = round(float(data[3]))
    # fourth_ser =round(float(data[4]))
    fifth_ser =round(float(data[5]))
    sixth_ser =round(float(data[6]))


    positions = {1: 32768*50/360*first_ser, 
                2: 32768*50/360*sec_ser, 
                3: 32768*50/360*thir_ser, 
                5: 32768*50/360*fifth_ser, 
                6: 32768*50/360*sixth_ser,
                # 4: 32768*50/360*fourth_ser
                }

    robt.set_target_pos(positions)

    # print('wait buffer')
    # while not protoc.check_is_buffer_empty():
    #     pass

    print('done')
    robt.move()


def interpolation_call():
    interp_thr = threading.Thread(target=interpol_call_for_thread)
    interp_thr.start()


def get_speed_call():
    return robt.read_speed(1)

def get_accel_call():
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


def start_ride_call(tree: Treeview):
    def smth():
        prev_row = None

        for itm in tree.get_children():
            curr_row = tree.item(itm)
            if prev_row:
                prev_row_tag = prev_row['tags'][0]
                tree.tag_configure(prev_row_tag, background='white')

            curr_row_tag = curr_row['tags'][0]
            tree.tag_configure(curr_row_tag, background='blue')
            
            curr_row_vals = curr_row['values']

            positions = {}

            axis_id = 1
            for axis_val in curr_row_vals:
                if axis_val == 'None':
                    positions[axis_id] = -1
                else:
                    positions[axis_id] = 32768*50/360*float(axis_val)
                axis_id += 1

            print(positions)
            robt.set_target_pos(positions)
            robt.move()
            time.sleep(6)

            prev_row = curr_row
            

        if prev_row:
            prev_row_tag = prev_row['tags'][0]
            tree.tag_configure(prev_row_tag, background='white')


    test_thr = threading.Thread(target=smth)
    test_thr.start()


def checker():
    while 1:
        time.sleep(2)
        for axis_id in range(1,7):
            protoc.read_speed(axis_id)
            protoc.read_accelearation(axis_id)
            protoc.read_current(axis_id)
            protoc.read_position(axis_id)
            protoc.read_mode(axis_id)
            protoc.read_error_checker(axis_id)
            protoc.read_temperature(axis_id)
            protoc.read_voltage(axis_id)


# checkthr = threading.Thread(target=checker)

# checkthr.start()

init_gui(interpolation_call=interpolation_call, get_axis_value_funcs_dict=axis_data, set_speed_call=set_speed_call, set_accel_call=set_accel_call, set_sync_call=set_sync_call, get_speed_call=get_speed_call, get_accel_call=get_accel_call, get_sync_call=get_sync_call, set_zero_pos_calls=set_zero_pos_calls, save_settings_calls=save_settings_calls, points_ride_call=start_ride_call)
