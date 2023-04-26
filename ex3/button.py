#coding: utf-8
import RPi.GPIO as GPIO
import time
#macro
button = 25

#settings
GPIO.setmode(GPIO.BCM) #button 25-> GPIO25
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

print("push button")
while True:
    btn = GPIO.imput(button) #read the statement of button
    if btn == True:
        print("pushed")
        break
    time.sleep(1)

GPIO.cleanup()