import typing
from tkinter import *
from gui.config_tab.storages.output import config_calls_repo


def congfig_tab(frame, save_settings_calls: typing.Callable, set_zero_pos_calls: typing.Dict):
    def param_field(param_name: str,  frame, row: int, column: int, call: typing.Callable):
        name_field = Button(master=frame, text=param_name, command=call)
        name_field.grid(row=row, column=column, padx=10, pady=10)


    def axis_params(axis_name: str,  frame, axis_id: int):
        axis_name = Label(master=frame, text=axis_name, background='white')
        axis_name.grid(row=axis_id, column=0, padx=5, pady=5)
        
        param_field(param_name='save settings', row=axis_id, column=2, frame=frame,  call=save_settings_calls[axis_id])
        param_field(param_name='set zero pos', row=axis_id, column=4, frame=frame,  call=set_zero_pos_calls[axis_id])
        
    
    for axis_id in range(1,7):
        axis_params(f'axis {axis_id}', frame, axis_id)
