import os
import time
import threading
import requests

Timer = 3

StartSpace = {"type":"flexiDesk","title":"One Day Pass","coin":50,"credit":10,"price":0,"user_id":165,"full_name":"rezayanti novia putrika dewi","phone_number":"+62 ","flexy_package_id":1}
def init_timer():
    return

def servoClose():
    os.system("python /home/pi/Documents/Igy/servo.py")
    time.sleep(1)
    print("request")
    os.system("sudo python /home/pi/Documents/Igy/request.py")
    timer.cancel()
    
timer = threading.Timer(Timer, init_timer)
timer.cancel()

while True:
    
    try:
        code = input("Scan: ")
#        print(code)
        if(str(code) == str(StartSpace)):
            os.system("sudo python /home/pi/Documents/Igy/servoOpen.py")
            os.system("sudo python /home/pi/Documents/Igy/takePic.py")
            timer = threading.Timer(Timer, servoClose)
            timer.start();
        
    except KeyboardInterrupt:
        print("\nExit")
    
