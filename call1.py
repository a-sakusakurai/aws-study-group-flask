import requests,json
from flask import jsonify,request,Flask

url = 'http://ec2-3-112-227-108.ap-northeast-1.compute.amazonaws.com/'
data = {'type':'water','name':'sakata'}
headers = {'content-type':'application/json'}
response = requests.post(url,json.dumps(data),headers = headers)
print(response.text)



'''
url = 'http://<DNS>/item'
data = {'name': 'sofa', 'price':90000}
headers = {'content-type': 'application/json'}
response = requests.post(url, json.dumps(data), headers=headers)
print(response.text)
'''
