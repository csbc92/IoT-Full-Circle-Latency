import pycom
from machine import UART
from LTR329ALS01 import LTR329ALS01

pycom.heartbeat(False)
uart = UART(0)                               # init with given bus
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters:  Baudrate=9600

integration_time = LTR329ALS01.ALS_INT_50 # Integration time of the light sensor.
measurement_rate = LTR329ALS01.ALS_RATE_50 # A lower rate means higher sampling rate i.e. ALS_50 is quick, ALS_2000 is slow.
                                            # MUST be equal or larger than integration time
gain = LTR329ALS01.ALS_GAIN_1X # A higher gain means a more precise measures in the lower end i.e. 8X gives a range [0.125, 8K] lux

lightsensor = LTR329ALS01(integration=integration_time, rate=measurement_rate, gain=gain)

isOn = True

while True:
    lux = lightsensor.light() # light() provides a tuple of lux values. The light sensor is a dual light sensor, hence two values.

    luxC1 = lux[0]

    if (luxC1 < 10 and isOn):
        isOn = False
        print(0) # Prints a 0 and a newline i.e. \n implicitly
    
    elif luxC1 > 100 and not isOn:
        isOn = True
        print(1) # Prints a 1 and a newline i.e. \n implicitly