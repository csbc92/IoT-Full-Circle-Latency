import pycom
import time
from machine import UART
from builtins import bytes

# Initializer
pycom.heartbeat(False)
uart = UART(0)                               # init with given bus
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters:  Baudrate=9600


# Turn on the LED with a given color
# Example input:
# RED=0xff0000
# GREEN=0x00ff00
# BLUE=0x0000ff
# YELLOW=0xffff00
def turn_on_led(color):
    pycom.rgbled(color)

def turn_off_led():
    pycom.rgbled(0x0) # 0x0 equals to black or turned off

def rgbToInt(red, green, blue):
    red = int(bin(red) + "0000000000000000", 2)
    green = int(bin(green)+"00000000", 2)

    return red + green + blue

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
        #print("Received some bytes")
        command = myBytes[0]

        # React to the parsed message
        if command == 0:

            pycom.rgbled(0xffffff)

        elif command == 1:
            pycom.rgbled(0x00)
