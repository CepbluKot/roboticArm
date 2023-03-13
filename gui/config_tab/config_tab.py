import typing
from tkinter import *
from gui.config_tab.storages.output import config_calls_repo
from servo_realisation.output import robot


def config_tab(frame):
    param_select = StringVar()

    params_calls = {
        'save settings': robot.save_settings, 
        'set zero pos': robot.send_zero_pos,
        'enable modbus': robot.send_enable_modbus,
        'disable modbus': robot.send_disable_modbus,
        'enable output': robot.send_enable_output,
        'disable output': robot.send_disable_output,
    }
    
    def param_button(param_name: str,  frame, row: int, column: int, call: typing.Callable):
        name_field = Button(master=frame, text=param_name, command=call)
        name_field.grid(row=row, column=column, padx=10, pady=10)


    def axis_params(axis_name: str,  frame, axis_id: int):
        axis_name = Label(master=frame, text=axis_name, background='white')
        axis_name.grid(row=axis_id, column=0, padx=5, pady=5)

        def axis_call():
            params_calls[param_select.get()](servo_id=axis_id)
            
        param_button(param_name='execute', row=axis_id, column=2, frame=frame,  call=axis_call)
        
    
    all_parameters = params_calls.keys()        

    curr_row = 7
    curr_column = 1

    for param_name in all_parameters:
        btn = Radiobutton(master=frame, text=param_name, variable=param_select, anchor=W, value=param_name)
        btn.grid(column=curr_column, row=curr_row, sticky=W)

        curr_row += 1

    
    for axis_id in range(1,7):
        axis_params(f'axis {axis_id}', frame, axis_id)
