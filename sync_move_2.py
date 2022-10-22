import threading
import can
import time
import typing

import servo_realisation.commands_constructor.input_output_realisation
import servo_realisation.commands_reader.input_output_realisation
import servo_realisation.control_objects.input_output_realisation
import servo_realisation.commands_constructor.commands_constructor_interface
import servo_realisation.control_objects.servo_interface
import servo_realisation.commands_abstraction.commands

import servo_realisation.commands_abstraction.input_output_realisation


import servo_realisation.commands_reader.input_output_realisation

import servo_realisation.thread_readr.thread_reader

import servo_realisation.commands_abstraction.commads_storage


from servo_realisation.commands_abstraction.commads_storage import servo_info_storage

# servo_1 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=1
# )
# servo_2 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=2
# )
# servo_3 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=3
# )
# servo_4 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=4
# )
# servo_5 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=5
# )
# servo_6 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=6
# )


servo_1 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=1
)
servo_2 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=2
)
servo_3 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=3
)
servo_4 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=4
)
servo_5 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=5
)
servo_6 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=6
)

# servo_1_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_1
# )
# servo_2_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_2
# )
# servo_3_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_3
# )
# servo_4_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_4
# )
# servo_5_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_5
# )
# servo_6_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_6
# )

servo_1_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_1
)
servo_2_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_2
)
servo_3_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_3
)
servo_4_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_4
)
servo_5_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_5
)
servo_6_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_6,
)


servo_1_abs.set_mode(1)

servo_2_abs.set_mode(1)

servo_3_abs.set_mode(1)

servo_4_abs.set_mode(1)

servo_5_abs.set_mode(1)

servo_6_abs.set_mode(1)
'''
class ServoThreadOperations():
    def __init__(self, servo_abstraction: servo_realisation.commands_abstraction.commands.ControlServoThread, servo_info_storage: typing.Dict[int, servo_realisation.commands_abstraction.commads_storage.ServoData]) -> None:
        self.servo_abs = servo_abstraction
        self.servo_info_storage = servo_info_storage
        self.link_to_servo_speed_data = self.servo_info_storage[servo_abstraction.servo.servo_id].commands_info_storage['6081']
        self.link_to_servo_current_pos_data = self.servo_info_storage[servo_abstraction.servo.servo_id].commands_info_storage['6064']
        self.link_to_servo_mode_data = self.servo_info_storage[servo_abstraction.servo.servo_id].commands_info_storage['6060']
        self.link_to_servo_target_pos_data = self.servo_info_storage[servo_abstraction.servo.servo_id].commands_info_storage['interpolation']
        self.link_to_servo_is_saved_data = self.servo_info_storage[servo_abstraction.servo.servo_id].commands_info_storage['6060']


        # while self.link_to_servo_speed_data.value_link == -1:
        #     servo_1_abs.read_speed()
   
        # print('sped dato ', self.link_to_servo_speed_data.value_link)

    def read_speed(self):
        print('redvalu',self.servo_info_storage[self.servo_abs.servo.servo_id].commands_info_storage['6081'].value_link, )

        if self.link_to_servo_speed_data.is_new_value:
            return self.link_to_servo_speed_data.value_link

        return -1

    def read_current_pos(self):
        print('posss',self.servo_info_storage[self.servo_abs.servo.servo_id].commands_info_storage['6064'].value_link, )

        if self.link_to_servo_current_pos_data.is_new_value:
            return self.link_to_servo_current_pos_data.value_link

        return -1

    def read_mode(self):
        

        if self.link_to_servo_mode_data.is_new_value:
            return self.link_to_servo_mode_data.value_link

        return -1

    def read_is_saved(self):
        if self.link_to_servo_is_saved_data.is_new_value:
            return self.link_to_servo_is_saved_data.value_link

        return -1

    def read_target_pos(self):
        if self.link_to_servo_target_pos_data.is_new_value:
            return self.link_to_servo_target_pos_data.value_link

        return -1

    def current_values_checker(self):
        if self.link_to_servo_speed_data.value_link == -1:
            self.servo_abs.read_speed()
            return False

        if self.link_to_servo_current_pos_data.value_link == -1:
            self.servo_abs.read_pos()
            return False

        if self.link_to_servo_mode_data.value_link == -1:
            self.servo_abs.read_mode()
            return False

        return True

    def check_is_all_target_parameters_set(self, target_pos=-1, target_speed=-1, ):
        
        
        if target_pos != -1:
            if not (self.link_to_servo_current_pos_data.is_new_value and self.link_to_servo_current_pos_data.value_link == target_pos):
                
               
                self.servo_abs.set_pos(target_pos)
                return False

        if target_speed != -1:
            if not (self.link_to_servo_speed_data.is_new_value and self.link_to_servo_speed_data.value_link == target_speed):
                self.servo_abs.set_speed(target_speed)
                return False
    
        # if target_mode != -1:
        #     if not (self.link_to_servo_mode_data.is_new_value and self.link_to_servo_mode_data.value_link == target_mode):
        #         self.servo_abs.set_mode(target_mode)
        #         return False 

        # if target_is_saved != -1:
        #     if not (self.link_to_servo_is_saved_data.is_new_value and self.link_to_servo_is_saved_data.value_link == target_is_saved):
        #         self.servo_abs.save_settings()
        #         return False 

        return True

# can_obj = servo_realisation.control_objects.input_output_realisation.get_can_object()
# read_thread = threading.Thread(target=servo_realisation.thread_readr.thread_reader.thread_reader, args=(can_obj, ), )
# read_thread.start()

# ser1_thr = ServoThreadOperations(servo_abstraction=servo_1_abs, servo_info_storage=servo_info_storage)
# ser2_thr = ServoThreadOperations(servo_abstraction=servo_2_abs, servo_info_storage=servo_info_storage)
# ser3_thr = ServoThreadOperations(servo_abstraction=servo_3_abs, servo_info_storage=servo_info_storage)
# ser4_thr = ServoThreadOperations(servo_abstraction=servo_4_abs, servo_info_storage=servo_info_storage)
# ser5_thr = ServoThreadOperations(servo_abstraction=servo_5_abs, servo_info_storage=servo_info_storage)
# ser6_thr = ServoThreadOperations(servo_abstraction=servo_6_abs, servo_info_storage=servo_info_storage)



# def write_test_2():
#     # while 1:
#         print('sent sped')
        
#         ser1_thr.read_speed()
#         time.sleep(1)
#         ser1_thr.read_speed()

#         print('sent mod')

#         ser1_thr.read_mode()
#         time.sleep(1)

#         print('sent pos')

#         ser1_thr.read_current_pos()
#         time.sleep(1)


# read_thread = threading.Thread(target=write_test_2,  )
# read_thread.start()



def move_to_pos_sync_thread(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    spd1 = 100
    spd2 = 100
    servo_1_abs.set_speed(value=spd1)
    servo_2_abs.set_speed(value=spd2)
    
    servo_1_abs.read_speed()
    servo_2_abs.read_speed()

    # getting SPEED



    servo_1_current_speed = ser1_thr.read_speed()
    servo_2_current_speed = ser2_thr.read_speed()
    
    
    if servo_1_current_speed == -1:
        ser1_thr.current_values_checker()
        servo_1_current_speed = ser1_thr.read_speed()
    if servo_2_current_speed == -1:
        ser2_thr.current_values_checker()
        servo_2_current_speed = ser2_thr.read_speed()

    print('red', servo_1_current_speed, servo_2_current_speed)


    # getting POSITION
    servo_1_abs.read_pos()
    servo_2_abs.read_pos()

    servo_1_current_pos = ser1_thr.read_current_pos()
    servo_2_current_pos = ser2_thr.read_current_pos()


    if servo_1_current_pos == -1:
        ser1_thr.current_values_checker()
    if servo_2_current_pos == -1:
        ser2_thr.current_values_checker()

    
    if servo_1_current_pos >= 42949672900:
        servo_1_current_pos = 0

    if servo_2_current_pos >= 42949672900:
        servo_2_current_pos = 0


    servo_1_target_pos = int(32768 * 50 /360 * servo_1_target_pos)
    servo_2_target_pos = int(32768 * 50 /360 * servo_2_target_pos)
   
    servo_1_distance_delta = abs(servo_1_target_pos - servo_1_current_pos)
    servo_2_distance_delta = abs(servo_2_target_pos - servo_2_current_pos)


    target_time = 0
    if abs(servo_1_distance_delta) >= abs(servo_2_distance_delta):
        print("PRIORITY - SERVO 1")
        servo_1_distance_delta = abs(servo_1_distance_delta)
        target_time = servo_1_distance_delta / servo_1_current_speed
        print('CALC TARG TIME: ', servo_1_distance_delta, ' /', servo_1_current_speed, ' =', target_time)
        
        if target_time:
            # print(target_time)
            servo_2_current_speed = abs(servo_2_distance_delta / target_time)

            servo_2_abs.set_speed(value=servo_2_current_speed)
            servo_2_abs.read_speed()
        else:
            servo_2_abs.set_speed(value=0)
            servo_2_abs.read_speed()

    else:
        print("PRIORITY - SERVO 2")
        target_time = abs(servo_2_distance_delta) / servo_2_current_speed
        print('CALC TARG TIME: ', abs(servo_2_distance_delta), ' /', servo_2_current_speed, ' =', target_time)
        if target_time:
            servo_1_current_speed = abs(servo_1_distance_delta / target_time)
            

            servo_1_abs.set_speed(value=servo_1_current_speed)
            servo_1_abs.read_speed()
        else:
            servo_1_abs.set_speed(value=0)
            servo_1_abs.read_speed()
       

    print('servo_1_current_pos', servo_1_current_pos, 'servo_1_target_pos', servo_1_target_pos)
    print('servo_2_current_pos', servo_2_current_pos, 'servo_2_target_pos', servo_2_target_pos)
    
    
    servo_1_abs.set_pos(value=servo_1_target_pos)
    servo_2_abs.set_pos(value=servo_2_target_pos)

    

    servo_3_abs.set_pos(value=0)
    servo_4_abs.set_pos(value=0)
    servo_5_abs.set_pos(value=0)
    servo_6_abs.set_pos(value=0)

    print('servo_1_speed', servo_1_current_speed, 'servo_2_speed', servo_2_current_speed)


    while not ser1_thr.check_is_all_target_parameters_set(target_pos=servo_1_target_pos, target_speed=servo_1_current_speed,  ):
        
        pass
        # print('eror check values thr 1')

    while not ser2_thr.check_is_all_target_parameters_set(target_pos=servo_2_target_pos, target_speed=servo_2_current_speed,  ):
        # print('eror check values thr 2')
        pass
    servo_1_abs.general_move_command()




def move_to_pos_sync(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    spd1 = 100
    spd2 = 100
    servo_1_abs.set_speed(value=spd1)
    servo_2_abs.set_speed(value=spd2)
    # getting SPEED
     
    servo_1_current_speed = servo_1_abs.read_speed().decoded_data
    servo_2_current_speed = servo_2_abs.read_speed().decoded_data

    # getting POSITION
    servo_1_current_pos = servo_1_abs.read_pos().decoded_data
    servo_2_current_pos = servo_2_abs.read_pos().decoded_data


    if servo_1_current_pos >= 42949672900:
        servo_1_current_pos = 0

    if servo_2_current_pos >= 42949672900:
        servo_2_current_pos = 0

    

    servo_1_target_pos = int(32768 * 50 /360 * servo_1_target_pos)
    servo_2_target_pos = int(32768 * 50 /360 * servo_2_target_pos)
   
    servo_1_distance_delta = abs(servo_1_target_pos - servo_1_current_pos)
    servo_2_distance_delta = abs(servo_2_target_pos - servo_2_current_pos)


    if not servo_1_current_speed:
        n =spd1
        servo_1_abs.set_speed(value=n)
        servo_1_current_speed = n

    if not servo_2_current_speed:
        n = spd2
        servo_2_abs.set_speed(value=n)
        servo_2_current_speed = n

    target_time = 0
    servo_1_target_speed = servo_1_current_speed
    servo_2_target_speed = servo_2_current_speed


    if abs(servo_1_distance_delta) >= abs(servo_2_distance_delta):
        print("PRIORITY - SERVO 1")
        target_time = abs(servo_1_distance_delta) / servo_1_current_speed
        print('CALC TARG TIME: ', abs(servo_1_distance_delta), ' /', servo_1_current_speed, ' =', target_time)
        if target_time:
            # print(target_time)
            servo_2_target_speed = abs(servo_2_distance_delta / target_time)

            if not servo_2_target_speed:
                servo_2_target_speed = 10

            servo_2_abs.set_speed(value=servo_2_target_speed)
        else:
            servo_2_abs.set_speed(value=0)
        

    else:
        print("PRIORITY - SERVO 2")
        target_time = abs(servo_2_distance_delta) / servo_2_current_speed
        print('CALC TARG TIME: ', abs(servo_2_distance_delta), ' /', servo_2_current_speed, ' =', target_time)
        if target_time:
            servo_1_target_speed = abs(servo_1_distance_delta / target_time)
            
            if not servo_1_target_speed:
                servo_1_target_speed = 10

            servo_1_abs.set_speed(value=servo_1_target_speed)
        else:
            servo_1_abs.set_speed(value=0)

       

    print('servo_1_current_pos', servo_1_current_pos, 'servo_1_target_pos', servo_1_target_pos)
    print('servo_2_current_pos', servo_2_current_pos, 'servo_2_target_pos', servo_2_target_pos)
    
    
    servo_1_abs.set_pos(value=servo_1_target_pos)
    servo_2_abs.set_pos(value=servo_2_target_pos)

    servo_3_abs.set_pos(value=0)
    servo_4_abs.set_pos(value=0)
    servo_5_abs.set_pos(value=0)
    servo_6_abs.set_pos(value=0)

    print('servo_1_speed', servo_1_target_speed, 'servo_2_speed', servo_2_target_speed)

    
    servo_1_abs.general_move_command()

    while servo_1_abs.read_cur_speed().decoded_data and servo_2_abs.read_cur_speed().decoded_data:
        pass

while 1:
    a, b = input('wegaewg').split()
    move_to_pos_sync(servo_1_target_pos=int(a), servo_2_target_pos=int(b))

'''
'''

def reader():
    print('start read')
    start_time = 0
    while True:
        tem = time.time()
        if tem - start_time >= 1:
            print('1 sec passed')
            start_time = tem
        
        read_1 = servo_1.receive(channel=0)
        # read_1 = servo_1_abs.decode_everyth(read_1)
        # if read_1.arbitration_id == 0x581:
            # tiem = time.time()
            # print(  "!!!      read ", read_1)
            # recv_time = tiem
        print(read_1)
        # print(read_1.id, read_1.ts)

def test_writer():
    print('start write')
    # start_time = time.time()
    
    a = [servo_1_abs, servo_2_abs, servo_3_abs, servo_4_abs, servo_5_abs, servo_6_abs, ]
    while True:
        # if time.time() - start_time >= 0.1:

            for x in a:
                x.read_speed()
                print('sent', x.servo.servo_id)

            # servo_1_abs.read_speed()
            # start_time = time.time()

def writer():
    # while 1:
        a, b = input('input').split(' ')
        # print(int(a), int(b))
        move_to_pos_sync(servo_1_target_pos=int(a), servo_2_target_pos=int(b))


def write_test_2():
    # while 1:
        print('sent sped')

        ser1_thr.read_speed()
        time.sleep(1)


        print('sent mod')

        ser1_thr.read_mode()
        time.sleep(1)

        print('sent pos')

        ser1_thr.read_current_pos()
        time.sleep(1)


def read_test_2():
    redr = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()
    while 1:
        # res2 = servo_1_abs.decode_everyth(res)
        
        res = servo_1.receive(0)
        res2 = []
        for elem in res:
            elem = redr.read_recieve(recieve=elem)
            res2.append(elem)



# servo_1_abs.set_zero_pos()
# servo_2_abs.set_zero_pos()
# servo_3_abs.set_zero_pos()
# servo_4_abs.set_zero_pos()
# servo_5_abs.set_zero_pos()
# servo_6_abs.set_zero_pos()

# servo_1_abs.set_mode(value=1)
# servo_2_abs.set_mode(value=1)
# servo_3_abs.set_mode(value=1)
# servo_4_abs.set_mode(value=1)
# servo_5_abs.set_mode(value=1)
# servo_6_abs.set_mode(value=1)



def mainthr():
    while 1:
        # a, b = input('inp').split(' ')
        a, b = 13, 13
        move_to_pos_sync_thread(servo_1_target_pos=int(a), servo_2_target_pos=int(b))



can_obj = servo_realisation.control_objects.input_output_realisation.get_can_object()
write_thread = threading.Thread(target=mainthr)



# read_thread = threading.Thread(target=servo_realisation.thread_readr.thread_reader.thread_reader, args=(can_obj, ), )
# read_thread.start()
# write_thread.start()
'''