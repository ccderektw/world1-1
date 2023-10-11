import requests
import sys
import time

url = "http://172.20.10.3:5000/get_data_lamp"
target_id = sys.argv[1]
onoff = b'0'

while(1):
    data = requests.get(url, params = {'id': target_id})
    print("get: "+str(data.content))
    if(onoff != data.content):
        onoff = data.content
        print("status change to: " + str(data.content))
        if(data.content == b'1'):
            print("turn on..")
            #TODO: turn on light/ record
        else:
            print("turn off..")
            #TODO: turn of light
    time.sleep(0.5)
