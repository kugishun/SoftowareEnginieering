#coding: utf-8
import RPi.GPIO as GPIO
import time

#macro
led=24
button=25

#setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

print("push button")

while True:
    btn = GPIO.input(button) #read the statement of button
    if btn == True:
        GPIO.output(led,1)#turn on
        time.sleep(6)     #6 second wait
        GPIO.output(led,0)#turn off
        break

print("finish")
GPIO.cleanup()
