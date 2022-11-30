import typing
from tkinter import *
import tkinter.ttk as ttk


def points_ride_tab(frame, start_ride_call=None):

    params_frame = Frame(master=frame,height=100)
    params_frame.pack()

    
    def params(frame, list_of_axis_ids: typing.List):
        entrys: typing.Dict[int, Entry] = {}
        
        for axis_id in list_of_axis_ids:
            axis_inp = Entry(frame, width=10)
            axis_inp.grid( column=axis_id, row=1, padx=10)
            entrys[axis_id] = axis_inp
            
        return entrys


    axis_ids_list = [1,2,3,4,5,6]
    axis_entrys = params(params_frame, axis_ids_list)
   

    columns = ("#1", "#2", "#3", "#4", "#5", "#6")
    points_table = ttk.Treeview(master=frame, columns=columns, show="headings")
    points_table.pack(side=LEFT, fill=BOTH, expand=1)

    points_table.heading('#1', text='axis 1')
    points_table.heading('#2', text='axis 2')
    points_table.heading('#3', text='axis 3')
    points_table.heading('#4', text='axis 4')
    points_table.heading('#5', text='axis 5')
    points_table.heading('#6', text='axis 6')

    scroll = ttk.Scrollbar( points_table, orient=VERTICAL, command=points_table.yview)
    
    points_table.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)

    def add_btn_call():
        angles_vals = ()
        for axis_id in axis_entrys:
            entry_data = axis_entrys[axis_id].get()
            if entry_data or entry_data == 0:
                angles_vals += (entry_data, )

            else:
                angles_vals += (None, )
        

        last_elem_id = 0

        elements = points_table.get_children()
        if elements:
            last_elem_id = int(elements[-1][1:])
        
        points_table.insert("", END, values=angles_vals, tags=(f'{last_elem_id}'))

 
  

    def delete(click_data):
        try:
            selected_item = points_table.selection()[0] ## get selected item
            print('selected_item',selected_item)
            points_table.delete(selected_item)
        except:
            pass
    


    def start_ride_call_with_argc():
        start_ride_call(points_table)
    
    send_to_table_btn = Button(params_frame, text='ADD', command=add_btn_call ).grid(column=len(axis_ids_list)+1, row=1, padx=20)
    launch = Button(params_frame, text='LAUNCH', command=start_ride_call_with_argc ).grid(column=len(axis_ids_list)+3, row=1, padx=20)
      
    points_table.bind('<Double-Button-1>', delete)


    return points_table
    # points_table['columns'] = ('axis 1', 'axis 2','axis 3','axis 4','axis 5','axis 6',)
    # points_table.insert(values=(1,2,3,4,5,6))
