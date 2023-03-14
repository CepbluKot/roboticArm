import typing
from tkinter.ttk import Combobox, Button, Scale, Label
from tkinter import *
from servo_realization.robot.servo_motor import ServoMotorAliexpress


def controls_tab(frame, interpolation_call: typing.Callable, get_axis_target_pos_value_funcs: typing.Dict, set_speed_call: typing.Callable, axis_data_from_robot: typing.Dict[int, ServoMotorAliexpress]):
    def eng_control(location, frame, axis_id):
        scale = Scale(frame, from_=0, to=360,  orient=HORIZONTAL, length=200)    
        scale.grid(row=location+1, column=2)
        scale.set(0)

        get_axis_target_pos_value_funcs[axis_id] = scale.get

        def plus_scale():
            cur_val = scale.get()
            
            scale.set(cur_val+1)

        def minus_scale():
            cur_val = scale.get()
            scale.set(cur_val-1)


        btn_decrease = Button(master=frame, text="-", command=minus_scale)
        btn_decrease.grid(row=location, column=1)
        btn_increase = Button(master=frame, text="+", command=plus_scale)
        btn_increase.grid(row=location, column=3, padx=10, pady=10)


        labl = Label(frame, text="axis " + str(axis_id))
        labl.grid(row=location+1, column=4, padx=10)

        space = Label(frame, text=" ")
        space.grid(row=location+2, column=2, pady=10)


    def robot_set_params(frame, set_speed, ):
        speed_lbl = Label(frame, text='speed', ).grid(padx=30, pady=10, row=1, column=6, )
        speed_inp = Entry(frame, )
        speed_inp.grid(row=1, column=7, padx=10, pady=10)
        set_btn = Button(frame, text='set', command=set_speed)
        set_btn.grid(row=1, column=8, padx=10, pady=10)


        return speed_inp


 
    cur_cood = 1
    for axis_id in axis_data_from_robot:

        eng_control(cur_cood, frame, axis_id)
        cur_cood += 5


    


    def set_speed():
        value = speed_inp.get()
        if value:
            set_speed_call(value)
         




    speed_inp = robot_set_params(frame, set_speed)


    interpolation_button = Button(frame, command=interpolation_call, text='SEND')

    interpolation_button.grid(row=33, column=2, padx=10, pady=10)

