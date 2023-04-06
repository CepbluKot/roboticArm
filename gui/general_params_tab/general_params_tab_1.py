
from tkinter import *
from gui.general_params_tab.storages.output import general_params_repo


def general_params_tab_1(frame):
    def param_field(param_name: str,  frame, row: int, column: int, axis_id: int, param_value=None):
        name_field = Label(master=frame, text=param_name, background='white')
        name_field.grid(row=row, column=column, padx=10, pady=10)

        if param_value:
            value_field = Label(master=frame, text=str(param_value), background='white')
            value_field.grid(row=row, column=column+1, padx=5, pady=5)
            general_params_repo.set(axis_id=axis_id, widget=value_field, value_name=param_name)
            

    def axis_params(axis_name: str,  frame, axis_id: int, row: int):
        param_field(param_name=axis_name, row=axis_id+row, column=0, frame=frame, axis_id=axis_id)
        param_field(param_name='speed', row=axis_id+row, column=2, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='accel', row=axis_id+row, column=4, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='mode', row=axis_id+row, column=6, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='position', row=axis_id+row, column=8, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='target position', row=axis_id+row, column=10, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='error code', row=axis_id+row, column=12, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='voltage', row=axis_id+row, column=14, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='current', row=axis_id+row, column=16, frame=frame, axis_id=axis_id, param_value=-1)
        param_field(param_name='temperature', row=axis_id+row, column=18, frame=frame, axis_id=axis_id, param_value=-1)

        
    
    for axis_id in range(1,7):
        axis_params(f'axis {axis_id}', frame, axis_id, 0)
    
    # separator = Frame(frame, height=2, width=15000, bg='black')
    # separator.place(x=0, y = 245) 
