# Pi-Weather-Station

## About the Project

The Pi-Weather-Station program was originally developed for my CS-350 class at Southern New Hampshire University to show how embedded systems work and how to manipulate hardware through the use of software. The weather station program is written in Python and uses a Raspberry Pi 4 (although a Raspberry Pi 3 is perfectly fine as well) along with the GrovePi Starter Kit from Dexter Industries. Once the GrovePi interface is connected to the Pi's GPIO, the sensor hardware is available to connect and create the fully functional weather station!

## Motivation

This project start off as a final assignment for CS-350, but has now evolved into an upgraded version with a few more features for my CS-499 class. The Raspberry Pi has been an absolute joy to work with and feels more like a fun hobby than a class assigment.

## Installation

To install this software, you simply have to run the Python code provided on the Raspberry Pi of your choice, with the operating system of your choice. In this project, Raspberry Pi OS was used along with provided Thonny IDE. The GrovePi kit is also required with the correct hardware connections(as noted in the Getting Started section) for the program to function properly. 

## Getting Started

To begin, first install the GrovePi interface on top the Raspberry Pi connected properly to it's GPIO ports. If you are following installation exactly as the code is written without changing the port numbers used for connection, the following ports are used:
- Red LED to digital port 4
- Green LED to digital port 2
- Blue LED to digital port 3
- Light sensor to analog port 0
- Temp/Humidity sensor to digital port 5
- LCD screen to any I2C port

Once all connections have been made, run the provided EnhancedPiWeatherStation.py in the IDE and the startup sequence should begin!

## Usage

The Enhanced Pi Weather Station will run on it's own constantly collecting data from the temperature and humidity sensor until the user presses ctl-c to start the shutdown sequence. If there is no light detected, the data collection will stop for 10 seconds and then recheck for light. This is to stop the station from gathering information at night and restart during the day. Depending on what weather conditions are met, the LED's will light up to give a visual indication of what is currently being read from the sensors.
- If the temperature is greater than 60 but less than 85, and humidity less than 80 --- Green LED 
- If the temperature is greater than 85 but less than 95, and humidity less than 80 --- Blue LED
- If the temperature is greater than 95 --- Red LED
- If the humidity is greater than 80 --- Blue and green LED

Once you are finished and ready for the program to stop running, simple use ctl-c and the program will run the shutdown sequence telling the user it is shutting down on the LCD  and illuminating the red LED

## Changelog

[1.1.0] - 2021-6-9

Version 1.1.0 was created as a Pi Weather Station enhancement for my CS - 499 class to demonstrate the concept of software design and engineering. The first changes made include updating the variables to reflect best practices for variable and method naming. Specific changes are below:
- GrLed --> greenLED
- BlLed --> blueLED
- RdLed --> redLED
- tempSensor --> tempSensorPort
- blue --> tempOutputPort

Following this, two new methods were created for version 1.1.0, the startup and shutdown methods. The startup method will run when the program is initially started, which will utilize the LCD screen from the GrovePi Kit to display a startup message and also blink the green LED twice. The shutdown method will run when the user presses ctr-c at any time and displays a shutdown message to the LCD while blinking the red LED twice. After the message is displayed, the program will exit by calling the sys.exit() function.

[1.0.0] - 2021-5-22

Original project upload from CS-350 class. Project includes all code necessary to get the user up and running, collecting weather data.
