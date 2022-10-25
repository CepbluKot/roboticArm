import typing
# import pydantic

import servo_realisation.control_objects.servo_interface


class ServoCommandData():
    def __init__(self, answer_code: int, send_address: int, value_link, is_new_value: bool) -> None:
        self.send_address = send_address
        self.answer_code = answer_code
        self.value_link = value_link
        self.is_new_value = is_new_value

    def set_value(self, value: int):
        self.value_link = value
        self.is_new_value = False

    def read_value(self):
        ''' need to check is value is realy updated'''
        return self.value_link

    def set_flag(self, value: bool):
        self.is_new_value = value

    def read_flag(self):
        return self.is_new_value


class ServoData():
    def __init__(self, servo_id: int) -> None:
        self.speed = -1
        self.pos = -1
        self.mode = -1
        self.saved = -1
        self.acceleration = -1
        self.servo_id = servo_id
        self.target_pos = -1
        self.commands_info_storage: typing.Dict[str, ServoCommandData] = {
            "6060": ServoCommandData(answer_code=0x580+self.servo_id, send_address=0x600+self.servo_id, value_link=self.mode, is_new_value=0), # mode
            "6081": ServoCommandData(answer_code=0x580+self.servo_id, send_address=0x600+self.servo_id, value_link=self.speed, is_new_value=0), # speed 
            "6064": ServoCommandData(answer_code=0x580+self.servo_id, send_address=0x600+self.servo_id, value_link=self.pos, is_new_value=0), # pos
            "2614": ServoCommandData(answer_code=0x580+self.servo_id, send_address=0x600+self.servo_id, value_link=self.saved, is_new_value=0), # save  
            "interpolation": ServoCommandData(answer_code=0x480+self.servo_id, send_address=0x500+self.servo_id, value_link=self.target_pos, is_new_value=0), # interpol (target pos)
            "6083": ServoCommandData(answer_code=0x580+self.servo_id, send_address=0x600+self.servo_id, value_link=self.acceleration, is_new_value=0), # acceleration
                }

    def read_speed(self):
        return self.commands_info_storage["6081"].read_value()

    def read_current_pos(self):
        return self.commands_info_storage["6064"].read_value()

    def read_mode(self):
        return self.commands_info_storage["6060"].read_value()

    def read_acceleration(self):
        return self.commands_info_storage["6083"].read_value()

    def read_target_pos(self):
        return self.commands_info_storage["interpolation"].read_value()

    def set_speed_value(self, value):
        self.commands_info_storage["6081"].set_value(value=value)

    def set_mode_value(self,  value):
        self.commands_info_storage["6060"].set_value(value=value)

    def set_acceleration_value(self, value):
        self.commands_info_storage["6083"].set_value(value=value)

    def set_target_pos_value(self,  value):
        self.commands_info_storage["interpolation"].set_value(value=value)
    
    def set_speed_flag(self, value: bool):
        self.commands_info_storage["6081"].set_flag(value=value)

    def set_mode_flag(self,  value: bool):
        self.commands_info_storage["6060"].set_flag(value=value)

    def set_current_pos_flag(self,  value: bool):
        self.commands_info_storage["6064"].set_flag(value=value)
    

    def set_acceleration_flag(self, value: bool):
        return self.commands_info_storage["6083"].set_value(value=value)

    def set_target_pos_flag(self,  value: bool):
        self.commands_info_storage["interpolation"].set_flag(value=value)
    
    def read_speed_flag(self, ):
        return self.commands_info_storage["6081"].read_flag()

    def read_mode_flag(self,  ):
        return self.commands_info_storage["6060"].read_flag()

    def read_current_pos_flag(self,):
        return self.commands_info_storage["6064"].read_flag()

    def read_target_pos_flag(self,  ):
        return self.commands_info_storage["interpolation"].read_flag()

    def read_acceleration_flag(self):
        return self.commands_info_storage["6083"].read_flag()

    def print_servo_data(self):
        print('SERVO ', self.servo_id)
        print('Speed: ', self.read_speed(), 'Cur_pos: ', self.read_current_pos(), 'Targ_pos: ', self.read_target_pos(), 'Accel: ', self.read_acceleration())


servo_info_storage: typing.Dict[int, ServoData] = {}


class GeneralCommandData():
    def __init__(self, answer_code: int, send_address: int) -> None:
        self.send_address = send_address
        self.answer_code = answer_code

general_commands_info_storage: typing.Dict[str, GeneralCommandData] = {
    "60600008": GeneralCommandData(answer_code=0x580, send_address=0x600), # mode
    "60810020": GeneralCommandData(answer_code=0x580, send_address=0x600), # speed 
    "60640020": GeneralCommandData(answer_code=0x580, send_address=0x600), # pos
    "26140010": GeneralCommandData(answer_code=0x580, send_address=0x600), # save    
    '606C0010': GeneralCommandData(answer_code=0x580, send_address=0x600), 
}
