import serial
import paho.mqtt.client as paho
broker="broker.emqx.io"
port=1883

# Enable USB Communication
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
 
while True:
    incoming = ser.readline().strip()
    data = incoming .decode()
    print('Air Quality Index: '+ data)
    client1= paho.Client()         
    client1.connect(broker,port)
    ret= client1.publish("crlcar/airq",data) 











