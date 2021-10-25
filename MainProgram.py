import time
import serial
import RPi.GPIO as GPIO
import threading
from configparser import ConfigParser
import json
import requests
import pprint

cfg = ConfigParser() 
cfg.read('/home/pi/Documents/IGY/config.ini')

devUuid = cfg.get('device','uuid')

host = cfg.get('server','host')
port = cfg.get('server','port')
path = cfg.get('server','filepath')
key = cfg.get('auth','x_api_key')

api_url = host + path

headers = {'Content-Type': 'application/json'}
        
scanner = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.IN, GPIO.PUD_DOWN)

GPIO.output(20,True)

def readData():
    buffer = ""
    while True:
        oneByte = scanner.read(1)
        if oneByte == b"\r":    #method should returns bytes
            oneByte = scanner.read(1)
            if oneByte == b"\n":
                return buffer
        else:
            buffer += oneByte.decode("ascii")
def turnStiles(stat):
    if(stat == True):
        out=False
    else:
        out=True
        
    GPIO.output(20,out)
    
def handle(pin):
    if(pin == 21):
        turnStiles(False)
        
#GPIO.add_event_detect(21, GPIO.BOTH, handle)
    
while True:
    rcv = readData()
    body = {'device_id':devUuid,
            'passcode':rcv
            }
    if(rcv != ""):
        print("send request")
#        print(rcv)
#        print(body)
        conn = requests.post(api_url, headers=headers, json=body)
        print(conn.status_code)
        print(conn.url)
        pprint.pprint(body)
        resp = conn.json()
#        resp = conn.content.decode('utf-8')
        print(resp['status'])
        if(conn.status_code == 200 and resp['status'] == 4):
            turnStiles(True)
            print(rcv)
            time.sleep(1)
            turnStiles(False)
            
        