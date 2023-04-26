#coding:utf-8
import RPi.GPIO as GPIO
import time

#macro
led=24

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)

#10 times turn on/off
for i in range(10):
    GPIO.output(led,1)#turn on
    time.sleep(1)     #1 second wait
    GPIO.output(led,0)#turn off
    time.sleep(1)     #1 second wait

#finish
GPIO.cleanup()