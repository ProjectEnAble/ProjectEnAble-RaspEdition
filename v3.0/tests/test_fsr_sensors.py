"""
Welcome to Project:EnAble v3.0
Project:EnAble is under Copyright © 2023 Jeron Osguthorpe

Project: EnAble
Author: Jeron Osguthorpe
Version: v3.1.0 - Beta

BASIC INFORMATION REGARDING PROJECT: ENABLE
Git Hub Organization Link: https://github.com/projectenable
Git Hub Repository Link: https://github.com/projectenable/Project-Enable
Website: https://enable.codingtricksyt.com
Email: enable@codingtricksyt.com
YouTube: https://youtube.com/codingtricks
Twitter: https://twitter.com/proj_enable
License, Code of Conduct, and Contributing: https://github.com/projectenable/Project-Enable
Donate: https://enable.codingtricksyt.com/

ChatGPT Involment: ChatGPT was used to help create this part of the project. Among ChatGPT, 
Copilot was also used to help create this part of the project. ChatGPT is a project by OpenAI. 
Copilot is a project by OpenAI and GitHub. Both projects are under the MIT License.

NOTE: Purpose of this file: This file is used to test the fsr sensors. This file is not part of the main program.

"""

# Importing Libraries
from fileinput import close
from multiprocessing.resource_sharer import stop 
import RPi.GPIO as GPIO 
import time
from time import sleep
import os
import random
import serial

def test_fsr_sensors_result():
    print("To test the fsr sensors, please apply pressure to each of the sensors. The sensors go in numbers to 5, starting from the index finger.")
    # SETTING UP THE GPIO
    GPIO.setmode(GPIO.BCM)

    # Pin Definitions
    CLK = 12
    MISO = 16
    MOSI = 20
    CS = 21

    # Set Up GPIO using BCM numbering
    GPIO.setup(CLK, GPIO.OUT)
    GPIO.setup(MISO, GPIO.IN)
    GPIO.setup(MOSI, GPIO.OUT)
    GPIO.setup(CS, GPIO.OUT)

    # Function to read data from ADC using software SPI
    def read_adc(channel):
        # SETTING UP THE GPIO
        GPIO.setmode(GPIO.BCM)  

        # Set Up GPIO using BCM numbering
        GPIO.setup(CLK, GPIO.OUT)
        GPIO.setup(MISO, GPIO.IN)
        GPIO.setup(MOSI, GPIO.OUT)
        GPIO.setup(CS, GPIO.OUT)

        try:
            # Chip Select Signal
            GPIO.output(CS, GPIO.HIGH)
            GPIO.output(CS, GPIO.LOW)

            # Start Bit
            GPIO.output(MOSI, GPIO.HIGH)
            GPIO.output(CLK, GPIO.HIGH)
            GPIO.output(CLK, GPIO.LOW)

            # Channel Selection
            for i in range(3):
                if (channel & (1 << i)) == 0:
                    GPIO.output(MOSI, GPIO.LOW)
                else:
                    GPIO.output(MOSI, GPIO.HIGH)
                GPIO.output(CLK, GPIO.HIGH)
                GPIO.output(CLK, GPIO.LOW)
            
            # Dummy Bit
            GPIO.output(MOSI, GPIO.LOW)
            GPIO.output(CLK, GPIO.HIGH)
            GPIO.output(CLK, GPIO.LOW)

            # Read Data
            data = 0
            for i in range(11):
                GPIO.output(CLK, GPIO.HIGH)
                if GPIO.input(MISO) == GPIO.HIGH:
                    data |= 1 << (10 - i)
                GPIO.output(CLK, GPIO.LOW)
            
            # Chip Select Signal
            GPIO.output(CS, GPIO.HIGH)

            return data
        except:
            print("Error reading ADC data")
            GPIO.cleanup()
            return 0

    for i in range(5):
        try:
            # Read ADC Data
            data = read_adc(i)
            print("ADC Data: %d" % data, "Finger: ", i)
            # Wait for 1 second
            print("Waiting for 5 seconds...")
            time.sleep(5)
        except:
            print("Error printing ADC data")
            GPIO.cleanup()

    result = read_adc()
    if result == 0:
        print("The FSR sensors are not working properly")
        GPIO.cleanup()
        return "ERROR"
    else:
        print("The FSR sensors are working properly")
        GPIO.cleanup()
        return "SUCCESSFULL"

# Close the GPIO
GPIO.cleanup()

# END OF PROGRAM
"""
Project: EnAble© is under Copyright 2023 by Jeron Osguthorpe. Though the project is open source, taking all 
credit for works is not. Though you are allowed to use the code for your own projects, you are not allowed to
take credit for the code. If you would like help with the code, please contact Jeron Osguthorpe. Contact 
information can be found on the Project: EnAble© website and GitHub repository/organization.
"""