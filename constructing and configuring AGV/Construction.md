
**Project Overview:**
The goal of this project is to design and build an Autonomous Ground Vehicle (AGV) that can navigate and perform tasks autonomously. The AGV will be equipped with a Raspberry Pi for onboard processing, a variety of sensors for perception, and the ability to be controlled remotely through an MQTT dashboard app. Below is a more detailed breakdown of the project:

**Objectives:**
1. **Autonomous Navigation:** Develop algorithms and control systems to enable the AGV to move autonomously, avoiding obstacles and following predefined paths.
2. **Remote Control:** Create an MQTT-based dashboard app to remotely control the AGV, send commands, and receive real-time sensor data.
3. **Obstacle Avoidance:** Implement obstacle detection and avoidance mechanisms using sensors like ultrasonic sensors.
4. **Camera Vision:** Optionally, integrate a camera module to provide visual feedback and allow for tasks like object recognition.
5. **Safety Features:** Incorporate safety mechanisms to stop or pause the AGV in emergency situations.
6. **Documentation:** Maintain thorough documentation of hardware, software, and design decisions for future reference.

**Components:**
1. **Chassis:** The physical structure of the AGV, which holds all components together.
2. **Wheels and Motors:** Drive the AGV's movement and direction.
3. **Raspberry Pi:** Acts as the main onboard computer, responsible for processing, decision-making, and communication.
4. **LiPo Battery:** Provides power to the AGV.
5. **Voltage Regulator:** Regulates the battery voltage to provide a stable 5V supply for the Raspberry Pi.
6. **Motor Driver (L298N):** Controls the motors and ensures precise movement.
7. **Sensors:** Such as ultrasonic sensors for obstacle detection and potentially a camera module for vision.
8. **Power Switch:** Enables easy on/off control of the AGV.
9. **MQTT Dashboard App:** An app that allows remote control and monitoring of the AGV.
10. **Jumper Wires and Connectors:** For wiring and connecting components.
11. **Safety Features:** Emergency stop buttons or other safety mechanisms.

**Functionality:**
1. **Autonomous Movement:** The AGV should be able to move forward, backward, turn, and stop autonomously.
2. **Obstacle Avoidance:** Using sensors, the AGV should detect obstacles in its path and navigate around them.
3. **Remote Control:** The MQTT dashboard app should provide a user-friendly interface to control the AGV's movement.
4. **Sensor Data:** The app should display real-time sensor data, including distance measurements and camera feed if used.
5. **Safety:** Implement safety features to ensure the AGV can be stopped in emergencies.

**Challenges and Considerations:**
1. **Power Management:** Ensure efficient power usage to extend battery life.
2. **Sensor Integration:** Properly integrate and calibrate sensors for reliable obstacle avoidance.
3. **Motor Control:** Develop precise motor control algorithms for smooth movement.
4. **Wireless Communication:** Set up a reliable MQTT communication system between the AGV and the dashboard app.
5. **Safety:** Implement safety mechanisms to prevent accidents and protect the AGV from damage.
6. **Documentation:** Maintain detailed documentation for easier troubleshooting and future development.
7. **Testing:** Rigorous testing and iterative development are crucial to ensure the AGV's reliability and performance.

*****************************************************************************

**Step 1: Assemble the Chassis and Mount Motors**
- Start by assembling the chassis of your AGV according to the manufacturer's instructions.
- Attach the motors securely to the chassis using mounting brackets and screws. Ensure they are evenly spaced and aligned with the wheels.

**Step 2: Wire the Motors to the Motor Driver (L298N)**
- Connect the wires from each motor to the motor driver (L298N) as follows:
  - Motor 1: Connect the wires from one motor to the OUT1 and OUT2 terminals on the L298N.
  - Motor 2: Connect the wires from the other motor to the OUT3 and OUT4 terminals on the L298N.
- Connect the ground (GND) wires of the motors to the ground (GND) terminal on the L298N.

**Step 3: Connect the L298N to the Raspberry Pi**
- Connect the control pins of the L298N to the GPIO pins on the Raspberry Pi. For example:
  - IN1 to a GPIO pin (e.g., GPIO17)
  - IN2 to a GPIO pin (e.g., GPIO18)
  - IN3 to a GPIO pin (e.g., GPIO22)
  - IN4 to a GPIO pin (e.g., GPIO23)
- Connect the L298N's 5V and GND pins to the 5V and GND pins on the Raspberry Pi.

**Step 4: Wire the LiPo Battery and Voltage Regulator**
- Connect the LiPo battery to the voltage regulator's input. Ensure correct polarity.
- Connect the voltage regulator's output to the 5V input of the Raspberry Pi.
- Connect the voltage regulator's ground (GND) to the Raspberry Pi's GND.
- Ensure the voltage regulator is properly set to output 5V.

**Step 5: Add a Power Switch for the LiPo Battery**
- Wire a power switch in series with the LiPo battery's positive (+) lead. This switch will allow you to turn the AGV's power on and off.

**Step 6: Attach Sensors (if applicable)**
- If you are using sensors such as ultrasonic sensors or cameras, mount them securely on the AGV's chassis.
- Connect the sensors to the appropriate GPIO pins on the Raspberry Pi.

**Step 7: Install the Raspberry Pi Operating System**
- Insert the microSD card with the Raspberry Pi's operating system (e.g., Raspbian) into the Raspberry Pi.
- Follow the official Raspberry Pi documentation to set up the operating system: https://www.raspberrypi.org/documentation/

**Step 8: Install Necessary Software and Libraries**
- Connect the Raspberry Pi to the internet and install the required software and libraries for motor control, sensor input, and MQTT communication.
- You may need to use the `pip` package manager to install Python libraries for your specific hardware and sensors.

**Step 9: Write and Test the Motor Control Code**
- Write Python code to control the motors using the GPIO pins and the L298N motor driver.
- Test the motor control code to ensure the AGV can move forward, backward, and turn in both directions.

**Step 10: Implement MQTT Communication**
- Develop Python code to establish MQTT communication between the Raspberry Pi and your MQTT broker.
- Define MQTT topics for sending control commands to the AGV and receiving sensor data from the AGV.

**Step 11: Create the MQTT Dashboard App**
- Develop the MQTT dashboard app using a programming language and framework of your choice.
- Design the user interface (UI) for controlling the AGV and displaying sensor data.
- Implement MQTT communication between the app and the AGV.

**Step 12: Test the AGV's Functionality**
- Test the AGV's overall functionality, including motor control, sensor input, and MQTT communication.
- Ensure that the AGV can move autonomously and respond to remote commands via the MQTT dashboard app.

**Step 13: Implement Safety Features**
- Implement safety features such as an emergency stop button or a fail-safe mechanism to halt the AGV in case of unexpected behavior.

**Step 14: Documentation and Troubleshooting**
- Document your project, including wiring diagrams, code, and component specifications.
- Be prepared to troubleshoot any issues that may arise during testing and development.

**Step 15: Deployment and Continuous Improvement**
- Deploy the AGV in your desired environment for autonomous operation.
- Monitor the AGV through the MQTT dashboard app and make adjustments and improvements as necessary based on real-world testing and feedback.


