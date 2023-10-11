import requests

url = "http://192.168.3.111:5000/post_data"
obj = {'id': '2', 'val': '0'}
requests.post(url, data = obj)