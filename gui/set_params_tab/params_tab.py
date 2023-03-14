import typing
from tkinter import *
from servo_realization.output import robot


def params_tab(frame):
    axis_input_fields: typing.Dict[int, Entry] = {}
    param_select = StringVar()

    params_calls = {
        'weak_magnet_angle': robot.send_weak_magnet_angle,
        'speed_loop_scale_coef': robot.send_speed_loop_scale_coefficient, 
        'position_loop_scale_coef': robot.send_position_loop_scale_coefficient,
        'speed_adjustment': robot.send_speed_loop_scale_coefficient,
        'dir_polarity': robot.send_polarity_dir,
        'electrical_gear_molecules': robot.send_electronic_gear_molecules,
        'electrical_transmission_denominator': robot.send_transfer_electronic_denominator, 
        'incremental_position': robot.send_incremental_position,
        'address': robot.send_servo_address,
        'max_stationaric_power': robot.send_stationary_max_power, 
        'target_position_cache': robot.send_target_location_cache,
        'max_current': robot.send_max_current,
    }

    def execute_call():
        for axis_id in axis_input_fields:
            data = axis_input_fields[axis_id].get()
            if data:
                data = int(data)
                params_calls[param_select.get()](servo_id=axis_id, value=data)

    def param_button(param_name: str,  frame, row: int, column: int, call: typing.Callable):
        name_field = Button(master=frame, text=param_name, command=call)
        name_field.grid(row=row, column=column, padx=10, pady=10)


    def input_field( frame, row: int, column: int):
        inp_field = Entry(master=frame, )
        inp_field.grid(row=row, column=column, padx=10, pady=10)
        return inp_field

    def axis_params(axis_name: str,  frame, axis_id: int):
        axis_name = Label(master=frame, text=axis_name, background='white')
        axis_name.grid(row=axis_id, column=0, padx=5, pady=5)
        axis_input_fields[axis_id] = input_field(row=axis_id, column=2, frame=frame)

    all_parameters = params_calls.keys()

    curr_row = 7
    curr_column = 1

    for param_name in all_parameters:
        btn = Radiobutton(master=frame, text=param_name, variable=param_select, anchor=W, value=param_name)
        btn.grid(column=curr_column, row=curr_row, sticky=W)

        curr_row += 1


    for axis_id in range(1,7):
        axis_params(f'axis {axis_id}', frame, axis_id)

    param_button(param_name='execute', frame=frame, row=5, column=5, call=execute_call)
