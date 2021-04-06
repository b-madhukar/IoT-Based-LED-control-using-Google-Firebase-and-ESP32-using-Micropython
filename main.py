import sys,time
import network
import ufirebase as firebase
from machine import Pin

def wlan_connect(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
    
wlan_connect('ssid', 'pwd')
led=Pin(14,Pin.OUT)
while True:
    value=firebase.get('https://home-practice-rtdb.firebaseio.com/LED1')
    print(value)
    if(value=='ON')
    led.on()
    if(value=='OFF')
    led.off()
    
    

