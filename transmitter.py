import base64
import requests
import json
from configparser import ConfigParser

with open("output/output.png", 'rb') as img:
    img_to_base64 = base64.b64encode(img.read())
    raw_data = {'output':img_to_base64.decode('utf-8')}
    json_data = raw_data 
    print(json_data)

    config = ConfigParser()
    config.read('transmitter_config.ini')
    return_url = config['DEFAULT']['return_url']
    print(return_url)
    res = requests.post(return_url, json=json_data)
    if res.ok:
        print(res.json)


