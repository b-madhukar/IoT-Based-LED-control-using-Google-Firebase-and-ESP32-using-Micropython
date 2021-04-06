# IoT-Based-LED-control-using-Google-Firebase-and-ESP32-using-Micropython


Step1:
Gettin ESP32 board ready for MicroPython- https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/
Follow the instructions to install Thonny IDE and Steps to run a simple blink application on ESP32

step2: Open Firebase
       - Create a Project 
       - Open Project 
       - Go to Realtime database 
       - Create database 
       - Add device 'LED1:ON'

Step2:Copy the github files to ESP32 using Thonny IDE

Step3:Open main.py and do the following changes
      - change the ssid and pwd
      - change the link of firebase real time database of your device
      
      
**Methods Information:**

To read data from firebase cloud use the following method:
firebase.get('paste your realtime database device link')

To update data in the firebase cloud use the following method:
firebase.put('paste your realtime database device link','Status -ON/OFF')
           
