import time, threading
from tkinter.ttk import  Treeview
from servo_realisation.output import robot, current_positions
from control_system.axis_sync import syncronise_2
from servo_realisation.output import robot


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
                    pulses_per_rev = robot.servos[axis_id].pulses_per_revolution
                    gearbox_val = robot.servos[axis_id].gearbox_value
                    positions[axis_id] = pulses_per_rev*gearbox_val/360*float(axis_val)
                axis_id += 1


            max_speed = 100    

            speeds, accelerations = {}, {}

            robot.send_target_pos(positions)
            
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
        
                
                robot.send_axis_accel(servo_id, accelerations[servo_id] )
                robot.send_axis_speed(servo_id, speeds[servo_id] )

            prev_row = curr_row
            
            robot.move()
            time.sleep(6)

        if prev_row:
            prev_row_tag = prev_row['tags'][0]
            tree.tag_configure(prev_row_tag, background='white')


    test_thr = threading.Thread(target=smth)
    test_thr.start()
