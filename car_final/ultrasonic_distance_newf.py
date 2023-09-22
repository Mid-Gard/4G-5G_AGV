import RPi.GPIO as GPIO
import time


#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) 
TRIG = 20
ECHO = 21
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("Calibrating.....")
initial_start = time.time()
time.sleep(2)

print("Place the object......")
j=0

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    j=j+1
    if(j==1):
        diff=pulse_end-initial_start
        print("Initializing time: ",diff)
    distance = round(distance+1.15, 2)
       #print("Distance:",distance)
    if distance<=300 and distance>=3:
        print("distance:",distance,"cm",'time: ',pulse_duration)
        i=1
          
        if distance>300 and i==1:
            print("place the object....")
            i=0
        time.sleep(2)
        
except KeyboardInterrupt:
     GPIO.cleanup()


