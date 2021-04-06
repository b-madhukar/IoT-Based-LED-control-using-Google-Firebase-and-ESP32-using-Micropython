import sys
import network
import ufirebase as firebase

def wlan_connect(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
    
wlan_connect('ssid', 'pwd')
while True:
    print(firebase.get('https://home-practice-rtdb.firebaseio.com/LED1'))
    
    
