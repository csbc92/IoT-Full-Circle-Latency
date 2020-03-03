# Description
This directory contains C# code which - in principle - measures latency between two IoT devices over serial communication.

# Known issues
The program is not able to read data sent from the Ambient light sensor IoT device. The calls Read() and Readline() are blocking and never returns any data.
It is however possible to send data over the serial port.