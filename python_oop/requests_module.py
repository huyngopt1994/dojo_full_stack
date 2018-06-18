import requests
import json

print("Start an example with get Request")
r =requests.get('https://github.com/timeline.json')
#body in text , it was decoded automatically based on HTTP headers
print(r.text)
# get encoding of request
print (r.encoding)
# get response body as bytes, for non text- requests:
print(r.content)

# get object in python when we deserialize json data
print(r.json)

print (r.status_code)
# post method with custom headers
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
# talk to server that we need a json format in response
headers = {'content-type': 'application/json'}

print("Start an example with Post request")
r =requests.post(url,data= json.dumps(payload), headers=headers)

print (r.status_code)


