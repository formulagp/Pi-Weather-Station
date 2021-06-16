### Jay Authement ###
### Version: [1.1.0] ###
### Enhanced Pi Weather Station  ###

# Libraries required for the program to run correctly #
import time
import math
import grovepi
import json
from grove_rgb_lcd import *

# LED digital port declarations #
greenLED = 2
blueLED = 3
redLED = 4

# Temp/Humidity sensor port and output port declaration #
tempSensorPort = 5
tempOutputPort = 0

# Light sensor analog port declaration #
lightSensorPort = 0

# Light sensor threshold #
threshold = 100

# Sets the ports declared above to outputs #
grovepi.pinMode(greenLED, "OUTPUT")
grovepi.pinMode(blueLED, "OUTPUT")
grovepi.pinMode(redLED, "OUTPUT")

# Sets the lightSensor port to an input #
grovepi.pinMode(lightSensorPort, "INPUT")

# Data list declaration #
data = []

# Startup Function #
def piStartup():

    print("Starting up Enhanced Pi Weather Station!")

    # Sets the LCD color and prints to it's screen #
    setRGB(0, 128, 0)
    setText("Starting up Enhanced Pi Weather Station!")
    time.sleep(2)

    # Blinks the green LED #
    for i in range(2):
        grovepi.digitalWrite(greenLED, 1)
        time.sleep(1)
        grovepi.digitalWrite(greenLED, 0)
        time.sleep(1)

# Shutdown Function #
def piShutdown():

    print("Shutting down Enhanced Pi Weather Station!")

    # Sets the LCD color and prints to it's screen #
    setRGB(128, 0, 0)
    setText("Shutting down Enhanced Pi Weather Station!")
    time.sleep(2)

    # Blinks the red LED #
    for i in range(2):
        grovepi.digitalWrite(redLED, 1)
        time.sleep(1)
        grovepi.digitalWrite(redLED, 0)
        time.sleep(1)

# Run the startup function #
piStartup()

while True:
    
    try:

        # Sets the LCD color and prints to it's screen #
        setRGB(0,0,70)
        setText("Gathering weather data!")
        time.sleep(1)
        setText("Press ctr-c to quit!")
        time.sleep(1)
      
        # Sets the variable to hold the sensor value #
        sensor_value = grovepi.analogRead(lightSensorPort)
        
        # Formula used to calculate the resistance of the sensor in K
        resistance = (float)(1023 - sensor_value)*10 / sensor_value

        # Runs the code if it's daytime based off the light sensor value #
        if sensor_value > threshold:
                    
            # Reads temp and humidity from sensor in port 5 #
            [temp, humidity] = grovepi.dht(tempSensorPort, tempOutputPort)
            
            # Formula to convert celcius to farenheit #
            farenheit = (temp * 9/5) + 32
            
            # Only prints and runs following code if the sensor reading is not nan #
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("Current temperature is: %.02fF and the current humidity is %.02f%%" % (farenheit, humidity) + ".")
                
                # Appending collected data and json creation for the temperature and humidity data collected #
                data.append([farenheit, humidity])

                # Creates a JSON file and dumps all collected data from the sensor readings. #
                with open('sensorData.json', 'w') as outfile:
                    json.dump(data, outfile)

                # Weather conditions that will trigger the LED's #

                # Illuminates the green LED based off the conditions below #
                if farenheit > 60 and farenheit < 85 and humidity < 80:
                    grovepi.digitalWrite(greenLED, 1)
                    grovepi.digitalWrite(blueLED, 0)
                    grovepi.digitalWrite(redLED, 0)

                # Illuminates the blue LED based off the conditions below #
                elif farenheit > 85 and farenheit < 95 and humidity < 80:
                    grovepi.digitalWrite(greenLED, 0)
                    grovepi.digitalWrite(blueLED, 1)
                    grovepi.digitalWrite(redLED, 0)

                # Illuminates the red LED based off the conditions below #
                elif farenheit > 95:
                    grovepi.digitalWrite(greenLED, 0)
                    grovepi.digitalWrite(blueLED, 0)
                    grovepi.digitalWrite(redLED, 1)

                # Illuminates the green and blue LEDs based off the conditions below #
                elif humidity > 80:
                    grovepi.digitalWrite(greenLED, 1)
                    grovepi.digitalWrite(blueLED, 1)
                    grovepi.digitalWrite(redLED, 0)
        
        # This runs if the light sensor reading is below the threshold value #
        else:
            print("Night time. Checking again in 10 seconds.")
            time.sleep(10)

            # No LED's are illuminated #
            grovepi.digitalWrite(greenLED, 0)
            grovepi.digitalWrite(blueLED, 0)
            grovepi.digitalWrite(redLED, 0)

    # Catches and handles the error from the 'try' function #
    except KeyboardInterrupt:
        piShutdown()
        sys.exit()
