import os
import requests
from datetime import datetime

host = "https://api.thebigbox.id/sms-notification/1.0.0/messages"


time = datetime.now()

msisdn = "081314808351"
content = "Suspected at: " + str(time) 

apiKey = "C8TtJOGBD22jGIvuP9k2UGqp15llNnOv"

contentType = "application/x-www-form-urlencoded"

#curl -X POST "https://api.thebigbox.id/sms-notification/1.0.0/messages" -H "accept: application/x-www-form-urlencoded" -H
#"x-api-key: bPlP94sDkbThSOFk7uMyt9O92ifg2DnF" -H "Content-Type: application/x-www-form-urlencoded" -d "msisdn=081314808351&content=test%20F%26B"
print("curl -X POST \""+ str(host) + "\" -H \"accept: "+ str(contentType) + "\" -H \"x-api-key: "+ str(apiKey) +"\" -H \"Content-Type: " + str(contentType) + "\" -d \"msisdn=" + str(msisdn) + "&content="+str(content) + "\"")

os.system("curl -X POST \""+ str(host) + "\" -H \"accept: "+ str(contentType) + "\" -H \"x-api-key: "+ str(apiKey) +"\" -H \"Content-Type: " + str(contentType) + "\" -d \"msisdn=" + str(msisdn) + "&content="+str(content) + "\"")
#response = requests.post(host, data = data, headers = apiKey)
#postReq = response.text
r = requests.post(host)
#print(r.text)
print(r.status_code)
