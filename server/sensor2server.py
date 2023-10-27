import requests
import sys
import time
import RPi.GPIO as GPIO

class sensor:
    def __init__(self, id_num, onoff):
        self.id = id_num
        self.onoff = onoff
        self.pin = 0

# init connection
host = sys.argv[1]
targets = sys.argv[2:]
url = host + "/post_data"
sensor_list = []

for i in range(len(targets)):
    sensor_list.append(sensor(int(sys.argv[i+2]), 0))

# init board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

sensor_list[0].pin = 23
sensor_list[1].pin = 24
sensor_list[2].pin = 25

for i in range(len(targets)):
    GPIO.setup(sensor_list[i].pin, GPIO.IN)

print("init done")

# main loop
while(1):
    for i in range(len(sensor_list)):
        data = GPIO.input(sensor_list[i].pin)
        if(data != sensor_list[i].onoff):
            sensor_list[i].onoff = data
            obj = {'id': int(sensor_list[i].id), 'val': int(sensor_list[i].onoff)}
            requests.post(url, data = obj)
    time.sleep(0.5) 
            #post
        #obj = {'id': '2', 'val': '0'}
        #print(GPIO.input(sensor_pin))
