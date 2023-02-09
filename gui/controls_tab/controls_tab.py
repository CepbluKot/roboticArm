import typing
from tkinter.ttk import Combobox, Button, Scale, Label
from tkinter import *


def controls_tab(frame, interpolation_call: typing.Callable, get_axis_target_pos_value_funcs: typing.Dict, set_speed_call: typing.Callable, set_accel_call: typing.Callable, set_sync_call: typing.Callable, get_speed_call: typing.Callable, get_accel_call: typing.Callable, get_sync_call: typing.Callable):
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


    def robot_set_params(frame, set_speed, set_accel, set_sync):
        speed_lbl = Label(frame, text='speed', ).grid(padx=30, pady=10, row=1, column=6, )
        speed_inp = Entry(frame, )
        speed_inp.grid(row=1, column=7, padx=10, pady=10)
        set_btn = Button(frame, text='set', command=set_speed)
        set_btn.grid(row=1, column=8, padx=10, pady=10)


        accel_lbl = Label(frame, text='accel', ).grid(padx=30, pady=10, row=2, column=6)
        accel_inp = Entry(frame, )
        accel_inp.grid(row=2, column=7, padx=10, pady=10)
        set_btn = Button(frame, text='set', command=set_accel)
        set_btn.grid(row=2, column=8, padx=10, pady=10)


        sync_lbl = Label(frame, text='sync', ).grid(padx=30, pady=10, row=3, column=6, )
        sync_inp = Entry(frame, )
        sync_inp.grid(row=3, column=7, padx=10, pady=10)
        set_btn = Button(frame, text='set', command=set_sync)
        set_btn.grid(row=3, column=8, padx=10, pady=10)

        return speed_inp, accel_inp, sync_inp


    def robot_curr_params(frame):
        speed_lbl = Label(frame, text='speed', background='white').grid(padx=30, pady=10, row=1, column=8+1, )
        speed_val_lbl = Label(frame, text=str(get_speed_call()))
        
        speed_val_lbl.grid(row=1, column=9+1, padx=10, pady=10)

        accel_lbl = Label(frame, text='accel', background='white' ).grid(padx=30, pady=10, row=2, column=8+1, )
        accel_val_lbl = Label(frame, text=str(get_accel_call()))
        
        accel_val_lbl.grid(row=2, column=9+1, padx=10, pady=10)

        sync_lbl = Label(frame, text='sync', background='white' ).grid(padx=30, pady=10, row=3, column=8+1, )
        sync_val_lbl = Label(frame, text=str(get_sync_call()))
        
        sync_val_lbl.grid(row=3, column=9+1, padx=10, pady=10)

        return speed_val_lbl, accel_val_lbl, sync_val_lbl


    eng_control(1, frame, 1)
    eng_control(5, frame, 2)
    eng_control(10, frame, 3)
    eng_control(15, frame, 4)
    eng_control(25, frame, 5)
    eng_control(30, frame, 6)

    
    curr_speed_lbl, curr_accel_lbl, curr_sync_lbl = robot_curr_params(frame)

    def set_speed():
        value = speed_inp.get()
        if value:
            set_speed_call(value)
            curr_speed_lbl.config(text=str(value))


    def set_accel():
        value = accel_inp.get()
        if value:
            set_accel_call(value)
            curr_accel_lbl.config(text=str(value))


    def set_sync():
        value = sync_inp.get()
        if value:
            set_sync_call(value)
            curr_sync_lbl.config(text=str(value))



    speed_inp, accel_inp, sync_inp = robot_set_params(frame, set_speed, set_accel, set_sync)


    interpolation_button = Button(frame, command=interpolation_call, text='SEND')

    interpolation_button.grid(row=33, column=2, padx=10, pady=10)

    obj = Combobox(frame, )
    obj.grid(column=0, row=0)
    obj['values'] = (1,2,3,4)
