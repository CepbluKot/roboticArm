from tkinter import *
from gui.general_params_tab.storages.output import general_params_repo


def general_params_tab(frame):
    def param_field(param_name: str,  frame, row: int, column: int, axis_id: int, param_value=None):
        name_field = Label(master=frame, text=param_name, background='white')
        name_field.grid(row=row, column=column, padx=10, pady=10)

        if param_value:
            value_field = Label(master=frame, text=str(param_value), background='white')
            value_field.grid(row=row, column=column+1, padx=5, pady=5)
            general_params_repo.set(axis_id=axis_id, widget=value_field, value_name=param_name)
            
    def axis_params(axis_name: str,  frame, axis_id: int):
        param_field(param_name=axis_name, row=axis_id, column=0, frame=frame, axis_id=axis_id)
        param_field(param_name='error code', row=axis_id, column=2, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='voltage', row=axis_id, column=4, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='temperature', row=axis_id, column=6, frame=frame, axis_id=axis_id, param_value=-1)
    
    
    for axis_id in range(1,7):
        axis_params(f'axis {axis_id}', frame, axis_id)
