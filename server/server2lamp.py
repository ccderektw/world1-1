import requests
import sys
import time
import RPi.GPIO as GPIO

class lamp:
    def __init__(self, id_num, onoff):
        self.id = id_num
        self.onoff = onoff
        self.pin = 0

# init connection
host = sys.argv[1]
targets = sys.argv[2:]
url = host + "/get_data_lamp"
lamp_list = []

for i in range(len(targets)):
    lamp_list.append(lamp(int(sys.argv[i+2]), 0))

# init board: hard-coded for now
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

lamp_list[0].pin = 26
lamp_list[1].pin = 20
lamp_list[2].pin = 21

for i in range(len(targets)):
    GPIO.setup(lamp_list[i].pin, GPIO.OUT)

print("init done")

# main loop
while(1):
    for i in range(len(lamp_list)):
        data = requests.get(url, params = {'id': str(lamp_list[i].id)} )
        print(str(lamp_list[i].id)  + " get: " + str(data.content))
        if(lamp_list[i].onoff != int(data.content)):
            lamp_list[i].onoff = int(data.content)
            print(str(lamp_list[i].id) + "status change to: " + str(lamp_list[i].onoff))
            if(lamp_list[i].onoff > 0):
                print("turn on..")
                GPIO.output(lamp_list[i].pin, GPIO.HIGH)
            else:
                print("turn off..")
                GPIO.output(lamp_list[i].pin, GPIO.LOW)
    time.sleep(0.5)
