import os
import requests

host = "https://api.thebigbox.id/sms-notification/1.0.0/messages"

msisdn = "081314808351"
content = "30 menit lagi voucher Food %26 Beverages Anda akan hangus, tukarkan sekarang juga."

apiKey = "C8TtJOGBD22jGIvuP9k2UGqp15llNnOv"

data = {'msisdn' : '081314808351','content' : 'Masa Berlaku Voucher F&B anda 10 menit lagi Habis'}
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