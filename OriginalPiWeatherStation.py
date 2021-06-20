### Jay Authement ###
### CS-350 ###
### FinalProject1 ###

import time
import math
import grovepi
import json

# LED digital port declarations #
GrLED = 2
BlLED = 3
RdLED = 4

# Temp/Humidity sensor port and output declaration #
tempSensor = 5
blue = 0

# Light sensor analog port declaration #
lightSensor = 0

# Light sensor threshold #
threshold = 100

# Sets the ports delcared above to outputs #
grovepi.pinMode(GrLED, "OUTPUT")
grovepi.pinMode(BlLED, "OUTPUT")
grovepi.pinMode(RdLED, "OUTPUT")

# Sets the lightSensor port to an input #
grovepi.pinMode(lightSensor, "INPUT")

# Data list declaration #
data = []

while True:
    
    try:
        
        # Gather information every 30min / 1800s #
        time.sleep(1800)
        
        # Sets the variable to hold the sensor value #
        sensor_value = grovepi.analogRead(lightSensor)
        
        # Formula used to calculate the resistance of the sensor in K
        resistance = (float)(1023 - sensor_value)*10 / sensor_value

        # Runs the code if it's daytime #
        if sensor_value > threshold:
                    
            # Reads temp and humidity from sensor in port 5 #
            [temp, humidity] = grovepi.dht(tempSensor, blue)
            
            # Formula to convert celcius to farenheit #
            farenheit = (temp * 9/5) + 32
            
            # Only prints and runs following code if the sensor reading is not nan #
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("Current temperature is: %.02fF and the current humidity is %.02f%%" % (farenheit, humidity) + ".")
                
                # Appending collected data and json creation for the temperature and humidity data collected #
                data.append([farenheit, humidity])
                
                with open('sensorData.json', 'w') as outfile:
                    json.dump(data, outfile)

                # Weather conditions that will trigger the LED's #
                if farenheit > 60 and farenheit < 85 and humidity < 80:
                    grovepi.digitalWrite(GrLED, 1)
                    grovepi.digitalWrite(BlLED, 0)
                    grovepi.digitalWrite(RdLED, 0)
                                        
                if farenheit > 85 and farenheit < 95 and humidity < 80:
                    grovepi.digitalWrite(GrLED, 0)
                    grovepi.digitalWrite(BlLED, 1)
                    grovepi.digitalWrite(RdLED, 0)
                    
                if farenheit > 95:
                    grovepi.digitalWrite(GrLED, 0)
                    grovepi.digitalWrite(BlLED, 0)
                    grovepi.digitalWrite(RdLED, 1)
                    
                if humidity > 80:
                    grovepi.digitalWrite(GrLED, 1)
                    grovepi.digitalWrite(BlLED, 1)
                    grovepi.digitalWrite(RdLED, 0)
        
        # This runs if the light sensor does not detect daylight #
        else:
            print("Night time. Checking again in 30 minutes.")
            grovepi.digitalWrite(GrLED, 0)
            grovepi.digitalWrite(BlLED, 0)
            grovepi.digitalWrite(RdLED, 0)
            
    except IOError:
        
        print("Critical ERROR! Critical ERROR! ABORT! ABORT!")