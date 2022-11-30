import typing
from tkinter.ttk import Combobox, Button, Scale, Label, Frame, Notebook, Treeview
from tkinter import *

from gui.controls_tab.controls_tab import controls_tab
from gui.general_params_tab.general_params_tab import general_params_tab
from gui.config_tab.config_tab import congfig_tab
from gui.points_ride_tab.points_ride_tab import points_ride_tab


def init_gui(interpolation_call: typing.Callable, get_axis_value_funcs_dict: typing.Dict, set_speed_call: typing.Callable, set_accel_call: typing.Callable, set_sync_call: typing.Callable, get_speed_call: typing.Callable, get_accel_call: typing.Callable, get_sync_call: typing.Callable, save_settings_calls: typing.Callable, set_zero_pos_calls: typing.Dict, points_ride_call: typing.Callable[[Treeview], None]):
    window = Tk()
    window.title("Robot service app")
    window.geometry('1500x900')
    

    tab_control = Notebook(window)  
    tab1 = Frame(tab_control)  
    tab2 = Frame(tab_control)  
    tab3 = Frame(tab_control)  
    tab4 = Frame(tab_control)
    tab4.pack(fill=BOTH, expand=1)
    
    tab_control.add(tab1, text='controls')  
    tab_control.add(tab2, text='data')  
    tab_control.add(tab3, text='config')
    tab_control.add(tab4, text='points_ride')  
    tab_control.pack(expand=1, fill='both')  

    controls_tab(tab1, interpolation_call, get_axis_value_funcs_dict, set_speed_call, set_accel_call, set_sync_call, get_speed_call, get_accel_call, get_sync_call)
    general_params_tab(tab2)
    congfig_tab(tab3, save_settings_calls, set_zero_pos_calls)
    points_ride_tab(tab4, points_ride_call)
    
    window.mainloop()
            