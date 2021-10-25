import http.client
import json

conn = http.client.HTTPSConnection('igy-vision.cognitiveservices.azure.com')
basepath = '/customvision/v3.0/Prediction/29c96f94-ec0d-406c-9598-cdf46cf63106/classify/iterations/IgyIteration1/image'

headers = {'Prediction-Key': '15f7651278414504be4b0253b6e055fb',
    'Content-Type': 'application/octet-stream'}

f=open("/home/pi/Documents/Igy/pic/1575574938.739525.jpeg","rb") #3.7kiB in same folder
fileContent = f.read()
#pubImg(base64.b64encode(fileContent), int(now))
                
foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)

conn.request('POST', basepath, fileContent, headers)

response = conn.getresponse()
print(response.read().decode())
