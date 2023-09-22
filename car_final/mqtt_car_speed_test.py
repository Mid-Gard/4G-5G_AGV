#!/usr/bin/python
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM) 
 
in1=24
in2=23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
 
direction = input('Please define the direction (Left=1 or Right=2): ')
dc = int(input('Please define the Motor PWM Duty Cycle (0-100): '))
hz = int(input('HZ: '))
pwm = GPIO.PWM(17, hz)
 
if direction == 1:
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
elif direction == 2:
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
 
try:
        while True:
                pwm.start(dc)
 
except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
