# Full Circle Latency
This repository contains a solution to a problem in the course *Software Engineering of Internet of Things*, University of Southern Denmark. The problem is described briefly below.



# Context
*Copy from Hand-in description*

Delays caused by programs, the underlying support system (e.g., operating sys-tem or framework) and peripherals follow different patterns on your laptop andyour IoT device.

# Exercise
*Copy from Hand-in description*

Create a loop where a laptop  triggers code execution on an IoT device which triggers code execution on another IoT device which triggers code execution onthe laptop, and do as precise measurements as possible of the time it takes from laptop transmission to laptop reception.


# Repository Structure
* src/ambient-sensor.py - contains the source code for IoT-device-1

* src/led.py - contains the source code for IoT-device-2

* src/client.py - contains the source code for the laptop taking measures

* results - contains the raw measurements of latency in nanoseconds

* analysis - contains an estimated normal distribution of the samples


# Running the solution
WIP