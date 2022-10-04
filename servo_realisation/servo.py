from servo_realisation import servo_interface
import canalystii


class Servo(servo_interface.ServoInterface):
    def __init__(self, device_id: int) -> None:

        self.device = canalystii.CanalystDevice(bitrate=1000000, device_index=device_id)

class ServoSdoAbsolutePositionMode(servo_interface.ServoSdoAbsolutePositionModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        

        self.dev = servo_interface.device

        

    def control_word_1(self) -> str:
        '''
        Пуск + выход напряжения + аварийный останов
        разрешен + работа разрешена
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def working_mode(self) -> str:
        '''
        Режим работы установлен на режим 
        позиционирования
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x01),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def actual_position(self) -> str:
        '''
        Считывание текущей позиции
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x64, 0x60, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_speed(self) -> str:
        '''
        Скорость записи трапеции 1000 об/мин (опущено,
        если используется по умолчанию)
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x81, 0x60, 0x00, 0xE8, 0x03, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_acceleration(self) -> str:
        '''
        Трапецеидальная запись ускорения/замедления
        20000 об/мин/с (опущено, если используются
        значения по умолчанию)
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x83, 0x60, 0x00, 0x20, 0x4E, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word_2(self) -> str:
        '''
        Режим управления абсолютным положением +
        немедленное выполнение нового положения
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x2F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def location_cache(self) -> str:
        '''
        Кэш позиционирования записывает 50 000
        импульсов
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word_read(self) -> str:
        '''
        Чтение слова состояния
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoSdoRelativePositionMode(servo_interface.ServoSdoRelativePositionModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        self.servo_interface = servo_interface

        self.dev = servo_interface.device

    def control_word(self) -> str:
        '''
        Пуск + выход напряжения + аварийный останов
        разрешен + работа разрешена
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def working_mode(self) -> str:
        '''
        Режим работы установлен на режим
        позиционирования
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x01),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def actual_position(self) -> str:
        '''
        Кэш позиционирования записывает 50 000
        импульсов
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=9,
            data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_speed(self) -> str:
        '''
        Скорость записи трапеции 1000 об/мин (опущено,
        если используется по умолчанию)
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=7,
            data=(0x23, 0x81, 0x60, 0x00, 0xE8, 0x03, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_acceleration(self) -> str:
        '''
        Трапецеидальная запись ускорения/замедления
        20000 об/мин/с (опущено, если используются
        значения по умолчанию)
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x83, 0x60, 0x00, 0x20, 0x4E, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word(self) -> str:
        '''
        Режим управления относительным положением
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=7,
            data=(0x2B, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def location_cache(self) -> str:
        '''
        Переход к новой точке местоположения
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=9,
            data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word_read(self) -> str:
        '''
        Чтение слова состояния
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoSdoSpeedMode(servo_interface.ServoSdoSpeedModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.device_id
        )

    def working_mode(self) -> str:
        '''
        Режим работы установлен на скоростной режим
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x03),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def speed_mode(self) -> str:
        '''
        Установленная скорость работы 1000 об/мин/с
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=9,
            data=(0x23, 0xFF, 0x60, 0x00, 0xF4, 0x01, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word(self) -> str:
        '''
        Скорость запуска / Остановить

        state = 1 -> Остановить
        state = 0 -> Скорость запуска
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word(self) -> str:
        '''
        Чтение слова состояния
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoControlTheProcessOfFindingTheOrigin(servo_interface.ServoPdoControlTheProcessOfFindingTheOriginInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.device_id
        )

    def find_the_origin(self) -> str:
        '''
        Метод нахождения начала координат
        установлен на 17
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x98, 0x60, 0x00, 0x11),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def working_mode(self) -> str:
        '''
        Режим работы установлен на режим поиска
        исходного положения
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x06),
        )

        self.dev.send(0, new_message)
        return self.dServoPdoAbsolutePositionModeev.recieve(0), self.dev.recieve(1)

    def status_word(self) -> str:
        '''
        Чтение слова состояния
        '''
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoAbsolutePositionMode(servo_interface.ServoPdoAbsolutePositionModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.device_id
        )

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        '''
        (положение цели 50000) + трапецеидальная
        скорость 1000
        Текущее положение 0x4316 (17175
        десятичное) + слово состояния 0x404
        Примечание: Эта команда предназначена
        для получения текущего положения.
        1. Если двигатель однооборотный
        абсолютный , диапазон текущего
        положения составляет от 0 до 32768.
        2. Если это многооборотный абсолют с
        аккумулятором, то можно записать только
        количество кругов. Ответными данными может
        быть положение многооборота.
        3. Если после процесса нахождения концевого
        выключателя в исходном положении
        значение реакции равно 0
        Несколько вокруг.
        '''
        new_message = canalystii.Message(
            can_id=0x301,
            remote=False,
            extended=False,
            data_len=10,
            data=(0x50, 0xC3, 0x00, 0x00, 0x00, 0xE8, 0x03, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word_working_mode_target_position_current_position_status_word(self) -> str:
        '''
        (абсолютное положение + немедленное
        выполнение) + режим положения + целевое
        положение 50000 текущее положение 0x4355
        + слово состояния 0x037
        Примечание: Текущая позиция не достигла
        заданного значения 0xc350 слово состояния
        10бит
        равно 0, целевая позиция не достигнута.
        '''
        new_message = canalystii.Message(
            can_id=0x201,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x2F, 0x00, 0x01, 0x50, 0xC3, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word_working_mode_target_position_current_position_status_word(
        self,
    ) -> str:
        '''
        (положение цели 50000) + трапецеидальная
        скорость 1000
        Текущее положение 0x50c3 (50,000
        десятичных) + слово состояния 0x437 
        '''
        new_message = canalystii.Message(
            can_id=0x301,
            remote=False,
            extended=False,
            data_len=10,
            data=(0x50, 0xC3, 0x00, 0x00, 0x00, 0xE8, 0x30, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoSpeedMode(servo_interface.ServoPdoSpeedModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.device_id
        )

    def control_word_working_mode_target_speed_current_position_status_word(
        self,
    ) -> str:
        '''
        Разрешение двигателя + скоростной режим +
        целевая скорость 600
        '''
        new_message = canalystii.Message(
            can_id=0x401,
            remote=False,
            extended=False,
            data_len=7,
            data=(0x0F, 0x00, 0x03, 0x58, 0x02, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoPositionInterpolationMode(
    servo_interface.ServoPdoPositionInterpolationModeInterface
):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
    ) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.device_id
        )

    def destination_location(self) -> str:
        '''
        Место назначения 50000 Адрес 1 Двигатель
        '''
        new_message = canalystii.Message(
            can_id=0x501,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x50, 0xC3, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def current_position_status_word(self) -> str:
        '''
        Текущее положение 0xD78 (3448
        десятичных) + слово состояния 0x437
        Примечание: Эта команда предназначена
        для получения текущего положения.
        Двигатель не работает
        1. Если двигатель однооборотный
        абсолютный , диапазонтекущего
        положения составляет от 0 до 32768.
        2. Только если это многооборотный абсолют
        с батарейкой, можно записать количество
        оборотов. 
        Затем эти данные могут быть местом
        расположения многооборотки.
        '''
        new_message = canalystii.Message(
            can_id=0x481,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x78, 0x0D, 0x00, 0x00, 0x37, 0x04),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def target_location(self) -> str:
        '''
        Место назначения 50000 Адрес 2 Двигатель
        Текущее положение 0x4D18 (6221 десятичное)
        + слово состояния 0x437
        '''
        new_message = canalystii.Message(
            can_id=0x501,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x50, 0xC3, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)
