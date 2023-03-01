from gui.output import init_gui, axis_set_angle_slider_data
from gui.calls.move_to_point import interpolation_call, interpol_call_for_thread
from gui.calls.set_params_calls import *
from gui.calls.save_settings_calls import *
from gui.calls.set_zero_pos_calls import *
from gui.calls.points_ride_calls import *


init_gui(interpolation_call= interpolation_call, get_axis_target_pos_value_funcs_dict=axis_set_angle_slider_data, set_speed_call=set_speed_call, set_accel_call=set_accel_call, set_sync_call=set_sync_call, set_zero_pos_calls=set_zero_pos_calls_output, save_settings_calls=save_settings_calls_output, points_ride_call=start_ride_call)
