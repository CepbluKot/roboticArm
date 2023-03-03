import time
from servo_realisation.output import protocol


while 1:
    protocol.read_goto_home_mode(6)
    time.sleep(2)