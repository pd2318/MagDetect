#!/bin/python3

#Import Python GPIO and time modules

import RPi.GPIO as GPIO
import time

#Setup the GPIO Pin numbers. (Leave if following directions.)

GPIO.setmode(GPIO.BCM)
REED = 6
LED = 18
BUZZ = 21
GPIO.setup(REED, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZ, GPIO.OUT)

#Show an introduction message with instruction."

print ("MagDetect - Find magnetic objects!")
print ("[Press ctrl+c to end the test]")
print ("Starting in 3 seconds")
time.sleep(3)

#Start the loop for the Reed Sensor to detect magnetic objects.
#LED and Buzzer will light and sound upon magnetic field detection.

try:
    while 1:
        RawValue = GPIO.input(REED)
        if (RawValue == 0):
            print("Magnetic Object Has Been Detected!")
            GPIO.output(LED, GPIO.HIGH)
            GPIO.output(BUZZ, GPIO.HIGH)
        else:
            print("No Magnetic Objects Detected ...")
            GPIO.output(LED, GPIO.LOW)
            GPIO.output(BUZZ, GPIO.LOW)
            time.sleep(0.2)
    print(",RawValue:",RawValue)

#The Except clause of Try to exit the loop upon pressing Ctrl-C.

except KeyboardInterrupt:
    pass
    print("Exiting MagDetect")
    print("Thank you!")
    GPIO.cleanup()

