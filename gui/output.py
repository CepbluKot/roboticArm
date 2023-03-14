import typing
from tkinter.ttk import Frame, Notebook, Treeview
from tkinter import *

from gui.controls_tab.controls_tab import controls_tab
from gui.general_params_tab.general_params_tab import general_params_tab
from gui.config_tab.config_tab import config_tab
from gui.points_ride_tab.points_ride_tab import points_ride_tab
from gui.set_params_tab.params_tab import params_tab
from servo_realization.output import robot


speed = 30
axis_set_angle_slider_data = {}

def init_gui(move_to_point_call: typing.Callable, get_axis_target_pos_value_funcs_dict: typing.Dict, set_speed_call: typing.Callable, points_ride_call: typing.Callable[[Treeview], None]):
    window = Tk()
    window.title("Robot service app")
    window.geometry('1500x900')
    
    tab_control = Notebook(window)  
    tab1 = Frame(tab_control)  
    tab2 = Frame(tab_control)  
    tab3 = Frame(tab_control)  
    tab4 = Frame(tab_control)
    tab5 = Frame(tab_control)
    tab4.pack(fill=BOTH, expand=1)
    
    tab_control.add(tab1, text='controls')  
    tab_control.add(tab4, text='points_ride') 
    tab_control.add(tab2, text='data')  
    tab_control.add(tab3, text='config')
    tab_control.add(tab5, text='set_params')  
    tab_control.pack(expand=1, fill='both')  

    controls_tab(tab1, move_to_point_call, get_axis_target_pos_value_funcs_dict, set_speed_call, axis_data_from_robot=robot.servos)
    general_params_tab(tab2)
    config_tab(tab3)
    points_ride_tab(tab4, points_ride_call)
    params_tab(tab5)

    window.mainloop()
            