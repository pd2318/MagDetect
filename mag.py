#!/bin/python3

#Import Python GPIO and time modules

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

REED = 6
LED = 18
BUZZ = 21
GPIO.setup(REED, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZ, GPIO.OUT)

print ("Sensor Test [Press ctrl+c to end the test]")
print ("Starting in 3 seconds")
time.sleep(3)

# signal detection (raising edge).
try:
    while 1:
        RawValue = GPIO.input(REED)
        if (RawValue == 0):
            print("Reed Switch Detects Magnet")
            GPIO.output(LED, GPIO.HIGH)
            GPIO.output(BUZZ, GPIO.HIGH)
        else:
            print("No Magnet Detected ...")
            GPIO.output(LED, GPIO.LOW)
            GPIO.output(BUZZ, GPIO.LOW)
            time.sleep(0.3)
    print(",RawValue:",RawValue)

except KeyboardInterrupt:
    pass
    print("Exiting Reed Switch Test ...")
    GPIO.cleanup()

