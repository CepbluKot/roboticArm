from abc import ABC



# to -do 

# create base class and use it ads aprent class
# https://stackoverflow.com/questions/70970877/how-to-group-methods-in-python-class


class servo_interface(ABC):
    # absolute_positon_mode

    def control_word(self) -> str:
        pass

    def working_mode(self) -> str:
        pass

    def actual_position(self) -> str:
        pass

    def trapezoidal_speed(self) -> str:
        pass

    def trapezoidal_acceleration(self) -> str:
        pass

    def control_word(self) -> str:
        pass

    def location_cache(self) -> str:
        pass

    def status_word_read(self) -> str:
        pass

    #relative position mode

    def control_word(self) -> str:
        pass

    def working_mode(self) -> str:
        pass

    def actual_position(self) -> str:
        pass

    def trapezoidal_speed(self) -> str:
        pass

    def trapezoidal_acceleration(self) -> str:
        pass

    def control_word(self) -> str:
        pass

    def location_cache(self) -> str:
        pass

    def status_word_read(self) -> str:
        pass

    # speed mode

    def working_mode(self) -> str:
        pass

    def speed_mode(self) -> str:
        pass

    def control_word(self) -> str:
        pass

    def status_word(self) -> str:
        pass

    # pdo position maode - control proces of finding th origin

    def find_the_origin(self) -> str:
        pass

    def working_mode(self) -> str:
        pass

    def status_word(self) -> str:
        pass
    
    # position mode

    def find_the_origin(self) -> str:
        pass

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        pass

    def control_word_working_mode_target_position_current_position_status_word(self) -> str:
        pass

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        pass
    
    # speed mode

    def control_word_working_mode_target_speed_current_position_status_word(self) -> str:
        pass

    def control_word_working_mode_target_speed_current_position_status_word(self) -> str:
        pass

    # position interpolation mode

    def destination_location(self) -> str:
        pass

    def current_position_status_word(self) -> str:
        pass

    def target_location(self) -> str:
        pass
