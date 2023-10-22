import RPi.GPIO as GPIO
import time
import requests
import sys

# init connection
host = sys.argv[1]
targets = sys.argv[2]
url = host + "/post_data"
lamp_list = []
status = 0

# init board
sensor_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

# main loop
while(1):
    data = GPIO.input(sensor_pin)
    if(data != status):
        print(data)
        status = data
        obj = {'id': targets, 'val': int(status)}
        requests.post(url, data = obj)
        time.sleep(0.5) 
        #post
    #obj = {'id': '2', 'val': '0'}
    #print(GPIO.input(sensor_pin))
