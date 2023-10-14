import requests
import sys

# init connection
host = sys.argv[1]
targets = sys.argv[2]
url = host + "/post_data"

# init board

# main loop
obj = {'id': str(targets), 'val': '0'}
requests.post(url, data = obj)