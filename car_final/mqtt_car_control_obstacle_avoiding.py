from time import sleep
import os,sys
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import time
#import urlparse
from six.moves.urllib.parse import urlparse
import urllib.parse as urlparse

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

in1 =  24  # RIGHT SIDE
in2 =  23  
en1 = 12
temp1=1
 
in3 =  10  #LEFT SIDE
in4 =  9
en2 = 13
temp2 =1

freq = 1000

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1=GPIO.PWM(en1,freq)

GPIO.setmode(GPIO.BCM)


GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(en2,freq)



p1.start(0)
p2.start(0)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")


def on_connect(self, mosq, obj, rc):
        self.subscribe("crlcar", 0)
    
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    data = msg.payload
    d1 = data.decode("UTF-8")
    d = d1[0]

    if(d == "F"):    
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=1
        temp2=1

    elif(d == "B"):    
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        temp2=0

    elif(d == "L"):    
        print("left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
#        on_stop()
    
    elif(d == "R"):    
        print("right")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
#        on_stop()
        
    elif(d =='S'):
        on_stop()
 
    elif (d =='v'):
        print(d1)
        p1.ChangeDutyCycle(int(d1[1:]))
        p2.ChangeDutyCycle(int(d1[1:]))
        
    elif(d=="A"):
        TRIG = 17
        ECHO = 27
        TRIG1 = 18
        ECHO1 = 28
        led = 22
        
        m11=9
        m12=10
        m21=24
        m22=23

        GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
        GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
        GPIO.setup(TRIG1,GPIO.OUT)                  # initialize GPIO Pin as outputs
        GPIO.setup(ECHO1,GPIO.IN)                   # initialize GPIO Pin as input
        
        GPIO.setup(led,GPIO.OUT)                  
        
        GPIO.setup(m11,GPIO.OUT)
        GPIO.setup(m12,GPIO.OUT)
        GPIO.setup(m21,GPIO.OUT)
        GPIO.setup(m22,GPIO.OUT)
        
        GPIO.output(led, 1)
        
        time.sleep(5)
        
        def stop():
            print("stop")
            GPIO.output(m11, 0)
            GPIO.output(m12, 0)
            GPIO.output(m21, 0)
            GPIO.output(m22, 0)
        
        def forward():
            GPIO.output(m11, 1)
            GPIO.output(m12, 0)
            GPIO.output(m21, 1)
            GPIO.output(m22, 0)
            print("Forward")
        
        def back():
            GPIO.output(m11, 0)
            GPIO.output(m12, 1)
            GPIO.output(m21, 0)
            GPIO.output(m22, 1)
            print("back")
        
        def left():
            GPIO.output(m11, 0)
            GPIO.output(m12, 0)
            GPIO.output(m21, 1)
            GPIO.output(m22, 0)
            print("left")
        
        def right():
            GPIO.output(m11, 1)
            GPIO.output(m12, 0)
            GPIO.output(m21, 0)
            GPIO.output(m22, 0)
            print("right")
        
        stop()
        count=0
        while True:
         i=0
         avgDistance=0
         for i in range(5):
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
          time.sleep(0.1)                                   #Delay
        
          GPIO.output(TRIG, True)                  #Set TRIG as HIGH
          time.sleep(0.00001)                           #Delay of 0.00001 seconds
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
        
          while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
               GPIO.output(led, False)             
          pulse_start = time.time()
        
          while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
               GPIO.output(led, False) 
          pulse_end = time.time()
          pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
        
          distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
          distance = round(distance,2)                 #Round to two decimal points
          avgDistance=avgDistance+distance
        
         avgDistance=avgDistance/5
         print("Avg.distance:",avgDistance)
         flag=0
         if avgDistance < 15:      #Check whether the distance is within 15 cm range
            count=count+1
            stop()
            time.sleep(1)
            back()
            time.sleep(1.5)
            if (count%3 ==1) & (flag==0):
             right()
             flag=1
            else:
             left()
             flag=0
            time.sleep(1.5)
            stop()
            time.sleep(1)
         else:
            forward()
            flag=0
        
    else:    
        print ("RETRY!!")  # LED OFF

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_stop():
        print("STOP!")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

mqttc = paho.Client()                        # object declaration
# Assign event callbacks
mqttc.on_message = on_message                          # called as callback
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe


#url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')                  # pass broker addr e.g. "tcp://iot.eclipse.org"
#url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.hivemq.com:1883')
url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883') 
url = urlparse.urlparse(url_str)
mqttc.connect(url.hostname, url.port)

rc = 0
while True:
    while rc == 0:
        import time   
        rc = mqttc.loop()
        #time.sleep(0.5)
    print("rc: " + str(rc))
