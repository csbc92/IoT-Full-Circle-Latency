import serial
import threading
import time

# configure the serial connections (the parameters differs on the device you are connecting to)
ser_led = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser_sensor = serial.Serial(
    port='/dev/ttyACM1',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

#ser_led.open()
#ser_sensor.open()

def led_thread():
    sendZero = True

    while True:
        if (sendZero):
            ser_led.write(bytearray([0]))
            sendZero = False
        else:
            ser_led.write(bytearray([1]))
            sendZero = True
        
        global send_time
        send_time = time.time_ns()
        time.sleep(1)


def sensor():
    file_object = open("log.txt", "w") # Overwrite existing log file and append to it
    file_object.write("latency ns\n")

    while True:
        ser_sensor.readline()
        latency = str(time.time_ns() - send_time)
        file_object.write(latency + "\n")



sender = threading.Thread(target=led_thread)
sender.start()

sensor()