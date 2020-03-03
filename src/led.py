import pycom
import time
from machine import UART
from builtins import bytes

# Initializer
pycom.heartbeat(False)
uart = UART(0)                               # init with given bus
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters:  Baudrate=9600


## Dummy init: check LEDs are working
for green in range(0, 255):
    turn_on_led(rgbToInt(255, green, 0))
for red in reversed(range(0, 255)):
    turn_on_led(rgbToInt(red, 255, 0))
for blue in range(0, 255):
    turn_on_led(rgbToInt(0, 255, blue))
for green in reversed(range(0, 255)):
    turn_on_led(rgbToInt(0, green, 255))
for red in range(0, 255):
    turn_on_led(rgbToInt(red, 0, 255))
for blue in reversed(range(0, 255)):
    turn_on_led(rgbToInt(255, 0, blue))


while True:
    # Receive serial communication
    myBytes = uart.read(1) # Read the received bytes into the byte array

    # Parse the serial communication
    if myBytes != None:
        command = myBytes[0]

        # React to the parsed message
        if command == 0:
            pycom.rgbled(0xffffff)
        elif command == 1:
            pycom.rgbled(0x00)
