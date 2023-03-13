import time, threading
from tkinter.ttk import  Treeview
from servo_realisation.output import robot, current_positions
from control_system.axis_sync import syncronise_2


def start_ride_call(tree: Treeview):
    def smth():
        prev_row = None

        for itm in tree.get_children():
            curr_row = tree.item(itm)
            if prev_row:
                prev_row_tag = prev_row['tags'][0]
                tree.tag_configure(prev_row_tag, background='white')

            curr_row_tag = curr_row['tags'][0]
            tree.tag_configure(curr_row_tag, background='blue')
            
            curr_row_vals = curr_row['values']

            positions = {}

            axis_id = 1
            for axis_val in curr_row_vals:
                if axis_val == 'None':
                    positions[axis_id] = -1
                else:
                    positions[axis_id] = 32768*50/360*float(axis_val)
                axis_id += 1

      
            
            max_speed = 50    

            speeds, accelerations = {}, {}

            robot.set_target_pos(positions)
            
            target_positions = positions
            # speeds, accelerations = syncronise(movement_time=2, current_positions=current_positions, target_positions=target_positions, max_acceleration=max_accel, max_speed=max_speed)

            speeds, accelerations = syncronise_2(current_positions=current_positions, target_positions=target_positions, max_speed=max_speed)

            print('speds', speeds)

            print('\n\n accels', accelerations)
            
            if not accelerations:
                print('INTERPOL MOVE ERROR')
                return None

            if not speeds:
                print('INTERPOL MOVE ERROR')
                return None
            
            for servo_id in accelerations:
                # if servo_id == 4:
                #     continue
                
                robot.set_axis_accel(servo_id, accelerations[servo_id] * 10)
                robot.set_axis_speed(servo_id, speeds[servo_id] * 10)

            prev_row = curr_row
            
            robot.move()
            time.sleep(6)

        if prev_row:
            prev_row_tag = prev_row['tags'][0]
            tree.tag_configure(prev_row_tag, background='white')


    test_thr = threading.Thread(target=smth)
    test_thr.start()
    