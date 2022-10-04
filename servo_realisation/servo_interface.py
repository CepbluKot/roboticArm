import abc

# to - do

# create base class and use it as parent class
# https://stackoverflow.com/questions/70970877/how-to-group-methods-in-python-class


class ServoInterface(abc.ABC):
    device_id: int


class ServoSdoAbsolutePositionModeInterface(abc.ABC):
    @abc.abstractmethod
    def control_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def working_mode(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def actual_position(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def trapezoidal_speed(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def trapezoidal_acceleration(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def control_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def location_cache(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def status_word_read(self) -> str:
        raise NotImplemented


class ServoSdoRelativePositionModeInterface(abc.ABC):
    @abc.abstractmethod
    def control_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def working_mode(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def actual_position(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def trapezoidal_speed(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def trapezoidal_acceleration(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def control_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def location_cache(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def status_word_read(self) -> str:
        raise NotImplemented


class ServoSdoSpeedModeInterface(abc.ABC):
    @abc.abstractmethod
    def working_mode(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def speed_mode(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def control_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def status_word(self) -> str:
        raise NotImplemented


class ServoPdoControlTheProcessOfFindingTheOriginInterface(abc.ABC):
    @abc.abstractmethod
    def find_the_origin(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def working_mode(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def status_word(self) -> str:
        raise NotImplemented


class ServoPdoAbsolutePositionModeInterface(abc.ABC):
    @abc.abstractmethod
    def find_the_origin(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def control_word_working_mode_target_position_current_position_status_word(
        self,
    ) -> str:
        raise NotImplemented


class ServoPdoSpeedModeInterface(abc.ABC):
    @abc.abstractmethod
    def control_word_working_mode_target_speed_current_position_status_word(
        self,
    ) -> str:
        raise NotImplemented


class ServoPdoPositionInterpolationModeInterface(abc.ABC):
    @abc.abstractmethod
    def destination_location(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def current_position_status_word(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def target_location(self) -> str:
        raise NotImplemented
