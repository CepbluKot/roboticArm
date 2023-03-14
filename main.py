from gui.output import init_gui, axis_set_angle_slider_data
from gui.calls.set_params_calls import *
from gui.calls.move_to_point_calls import *


init_gui(move_to_point_call=move_to_point_call, get_axis_target_pos_value_funcs_dict=axis_set_angle_slider_data, set_speed_call=set_speed_call, points_ride_call=move_multiple_points)
