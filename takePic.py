import time
import os
#import http.client
import httplib
import json


def takePic(now):
    ssDir = "/home/pi/Documents/Igy/pic/" + str(now) + ".jpeg"
    os.system( "fswebcam -r 1280x720 " + ssDir)
    
now = time.time()
takePic(now)

conn = httplib.HTTPSConnection('igy-vision.cognitiveservices.azure.com')
basepath = '/customvision/v3.0/Prediction/29c96f94-ec0d-406c-9598-cdf46cf63106/classify/iterations/Iteration3/image'

headers = {'Prediction-Key': '15f7651278414504be4b0253b6e055fb',
    'Content-Type': 'application/octet-stream'}

f=open("/home/pi/Documents/Igy/pic/"+str(now)+".jpeg","rb") #3.7kiB in same folder
fileContent = f.read()
#pubImg(base64.b64encode(fileContent), int(now))
                
foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)

conn.request('POST', basepath, fileContent, headers)

response = conn.getresponse()
json_data = response.read().decode()
data = json.loads(json_data)

print(str(data))

tagname = data['predictions'][0]['tagName']
#print(tagname)


if(str(tagname) ==  "fauzan"):
    probability = data['predictions'][0]['probability'] * 100
    if(probability > 70):
        print("send SMS")
        os.system("sudo python /home/pi/Documents/Igy/requestInt.py")
    