# import the library
import can

# create a bus instance
# many other interfaces are supported as well (see documentation)
# bus1 = can.Bus(interface='canalystii',
#               channel=0,
#               receive_own_messages=True,
#               bitrate=500000
#               )

testbus = can.Bus(bustype='socketcan', bitrate=500000)



# send a message
message = can.Message(arbitration_id=0, is_extended_id=True,
                      data=[0x11, 0x22, 0x33])



testbus.send(message, timeout=0.2)
testbus.shutdown()
# iterate over received messages


# for msg in bus:
#     print(f"{msg.arbitration_id:X}: {msg.data}")

# or use an asynchronous notifier
# notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])