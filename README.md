# IoT-Based-LED-control-using-Google-Firebase-and-ESP32-with-Micropython


Step1:
- Gettin ESP32 board ready for MicroPython- https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/
- Follow the instructions to install Thonny IDE and Steps to run a simple blink application on ESP32

Step2: 
- Open Firebase 'https://firebase.google.com/'
- Create a Project 
- Open Project 
- Go to Realtime database 
- Create database 
- Add device 'LED1:ON'

Step3:
- Copy the github files to ESP32 using Thonny IDE

Step4:
- Open main.py and do the following changes


      1. change the ssid and pwd
      2. change the firebase link of real-time-database of your device
      ex:https://home-practice-rtdb.firebaseio.com/LED1
      
      
**Methods Information:**

To read data from firebase cloud use the following method:
- **firebase.get**('paste your realtime database device link')

To update data in the firebase cloud use the following method:
- **firebase.put**('paste your realtime database device link','Status -ON/OFF')
           
