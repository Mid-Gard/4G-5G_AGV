
**A] Program Explaination:**

**Block 1: Imports and Library Setup**
```python
from time import sleep
import os, sys
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
from six.moves.urllib.parse import urlparse
import urllib.parse as urlparse
```

- **Function**: This block imports necessary Python libraries/modules required for the program.
- **Explanation**:
  - `from time import sleep`: Imports the `sleep` function from the `time` module, which is used for creating delays.
  - `import os, sys`: Imports the `os` and `sys` modules, which are often used for system-related operations.
  - `import RPi.GPIO as GPIO`: Imports the `RPi.GPIO` library and aliases it as `GPIO`. This library is essential for controlling the GPIO pins on a Raspberry Pi.
  - `import paho.mqtt.client as paho`: Imports the Paho MQTT client library and aliases it as `paho`. This library is used for MQTT communication.
  - The last two lines import modules for URL parsing and handling.

**Block 2: GPIO Setup**
```python
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
```

- **Function**: Configures the GPIO (General Purpose Input/Output) for the Raspberry Pi.
- **Explanation**:
  - `GPIO.setmode(GPIO.BCM)`: Sets the GPIO pin numbering mode to BCM (Broadcom SOC channel numbers), which is a common numbering scheme for Raspberry Pi GPIO pins.
  - `GPIO.setwarnings(False)`: Disables GPIO warnings, preventing them from displaying in the console.

**Block 3: GPIO Pin and Frequency Definitions**
```python
in1 =  24  # RIGHT SIDE
in2 =  23  
en1 = 12
temp1 = 1
 
in3 =  10  # LEFT SIDE
in4 =  9
en2 = 13
temp2 = 1

freq = 1000
```

- **Function**: Defines variables to represent GPIO pin numbers and PWM frequency for motor control.
- **Explanation**:
  - `in1`, `in2`, `en1`, `temp1`: Variables representing GPIO pins for controlling the right side of the motor and a temporary variable.
  - `in3`, `in4`, `en2`, `temp2`: Variables representing GPIO pins for controlling the left side of the motor and a temporary variable.
  - `freq`: Specifies the PWM (Pulse Width Modulation) frequency as 1000 Hz, which determines the motor speed control granularity.

**Block 4: GPIO Setup for Motor Control**
```python
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p1 = GPIO.PWM(en1, freq)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p2 = GPIO.PWM(en2, freq)

p1.start(0)
p2.start(0)
```

- **Function**: Sets up the GPIO pins for motor control and initializes PWM for speed control.
- **Explanation**:
  - The code is divided into two parts, one for the right side and one for the left side of the motor.
  - `GPIO.setup`: Configures pins as outputs.
  - `GPIO.output`: Initializes the output state of pins as LOW (motor off).
  - `GPIO.PWM`: Sets up PWM objects for speed control.
  - `p1.start(0)` and `p2.start(0)`: Starts the PWM objects with an initial duty cycle of 0, effectively stopping the motors initially.

**Block 5: Print Initial Instructions**
```python
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")
```

- **Function**: Prints introductory messages to the console.
- **Explanation**: These messages provide information to the user about the default motor state, directions, and the available control options.

**Block 6: MQTT Callback Functions**
```python
def on_connect(self, mosq, obj, rc):
    self.subscribe("crlcar", 0)

def on_message(mosq, obj, msg):
    # ...
    # Message handling logic
    # ...

def on_publish(mosq, obj, mid):
    # ...

def on_subscribe(mosq, obj, mid, granted_qos):
    # ...
```

- **Function**: Defines callback functions for MQTT event handling.
- **Explanation**:
  - `on_connect`: Callback called when the MQTT client successfully connects to the broker. It subscribes to the "crlcar" topic with QoS 0 (Quality of Service).
  - `on_message`: Callback for handling incoming MQTT messages. It interprets the messages to control the motor.
  - `on_publish`: Callback for handling MQTT message publishing (not used in this code).
  - `on_subscribe`: Callback for handling subscription confirmation (not used in this code).

**Block 7: Custom Function `on_stop`**
```python
def on_stop():
    print("STOP!")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
```

- **Function**: Defines a custom function to stop the motor.
- **Explanation**:
  - When called, this function sets all motor control pins to LOW, effectively turning off the motor.

**Block 8: MQTT Client Setup**
```python
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')
url = urlparse.urlparse(url_str)
mqttc.connect(url.hostname, url.port)
```

- **Function**: Sets up the MQTT client for communication with an MQTT broker.
- **Explanation**:
  - Creates an MQTT client object `mqttc`.
  - Assigns the defined callback functions to corresponding MQTT events.
  - Parses the MQTT broker URL from an environment variable named `CLOUDMQTT_URL` or uses a default URL.
  - Connects to the MQTT broker using the parsed hostname and port.

**B] Connection Details:**

**(GPIO number)**
en1 = 12
in1 =  24  
in2 =  23  
in3 =  10 
in4 =  9
en2 = 13

**(RasPi pin configuration)**
en1 = 32
in1 =  18
in2 =  16
in3 =  19 
in4 =  21
en2 = 33
