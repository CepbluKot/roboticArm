from time import sleep
import canalystii

# Connect to the Canalyst-II device
# Passing a bitrate to the constructor causes both channels to be initialized and started.
dev = canalystii.CanalystDevice(bitrate=500000, device_index=0)

# Receive all pending messages on channel 0


# The canalystii.Message class is a ctypes Structure, to minimize overhead
new_message = canalystii.Message(can_id=1,
                                 remote=False,
                                 extended=False,
                                 data_len=7,
                                 data=(0x0F,0x00,0x03,0x58,0x02,0x00,0x00))
# Send one copy to channel 1
dev.send(0, new_message)
# Send 3 copies to channel 0
# (argument can be an instance of canalystii.Message or a list of instances)

sleep(0.2)
print(dev.receive(1))
print(dev.receive(0))
# Stop both channels (need to call start() again to resume capturing or send any messages)
dev.stop(0)
dev.stop(1)