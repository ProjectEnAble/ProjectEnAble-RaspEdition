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

NOTE: Purpose of this file: This file is used to test the servo motors. This file is not part of the main program.

"""
import RPi.GPIO as GPIO
import time

def test_motors_result():
    # SETTING UP THE GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

    # SETTING UP THE SERVO MOTORS
    print("Setting up the servo motors...")
    index_servo = GPIO.PWM(5, 50)
    middle_servo = GPIO.PWM(6, 50)
    ring_servo = GPIO.PWM(13, 50)
    pinky_servo = GPIO.PWM(19, 50)
    thumb_servo = GPIO.PWM(26, 50)
    print("Servo motors set up!")
    print("Starting the servo motors...")
    index_servo.start(0)
    middle_servo.start(0)
    ring_servo.start(0)
    pinky_servo.start(0)
    thumb_servo.start(0)

    # TESTING THE SERVO MOTORS FUNCTION 
    def test_motors(): 
        try:
            print("Testing the servo motors...")
            index_servo.ChangeDutyCycle(10)
            time.sleep(1)
            middle_servo.ChangeDutyCycle(10)
            time.sleep(1)
            ring_servo.ChangeDutyCycle(10)
            time.sleep(1)
            pinky_servo.ChangeDutyCycle(10)
            time.sleep(1)
            thumb_servo.ChangeDutyCycle(10)
            time.sleep(1)

            reset_motors()
            return "SUCCESSFULL"
        except:
            print("Error: Something went wrong while testing the servo motors!")
            GPIO.cleanup()
            return "ERROR"

    # RESET THE SERVO MOTORS
    def reset_motors():
        try:
            print("Resetting the servo motors...")
            index_servo.ChangeDutyCycle(2.5)
            time.sleep(1)
            middle_servo.ChangeDutyCycle(2.5)
            time.sleep(1)
            ring_servo.ChangeDutyCycle(2.5)
            time.sleep(1)
            pinky_servo.ChangeDutyCycle(2.5)
            time.sleep(1)
            thumb_servo.ChangeDutyCycle(2.5)
            time.sleep(1)
            print("Servo motors reset!")
            GPIO.cleanup()

            print("Testing complete!")
            return "SUCCESSFULL"
        except:
            print("Error: Something went wrong while resetting the servo motors!")
            GPIO.cleanup()
            return "ERROR"
    
    testresult = test_motors()
    resetresult = reset_motors()
    
    # CALLING THE FUNCTIONS
    test_motors()

    # RETURNING THE RESULTS
    if testresult == "SUCCESSFULL" and resetresult == "SUCCESSFULL":
        return "SUCCESSFULL"
    elif testresult == "ERROR" or resetresult == "ERROR":
        return "ERROR"

# END OF FILE
"""
Project: EnAble© is under Copyright 2023 by Jeron Osguthorpe. Though the project is open source, taking all 
credit for works is not. Though you are allowed to use the code for your own projects, you are not allowed to
take credit for the code. If you would like help with the code, please contact Jeron Osguthorpe. Contact 
information can be found on the Project: EnAble© website and GitHub repository/organization.
"""