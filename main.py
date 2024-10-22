import time
import requests
from playsound import playsound

connected = None
delay = 30 # seconds

while True:
    try:
        requests.get('https://httpbin.org/ip')
        if connected is False:
            print("Internet is back")
        connected = True
    except requests.exceptions.ConnectionError:
        if connected is not False:
            playsound("./beep.mp3")
            print("Internet lost")
        connected = False
    time.sleep(delay)