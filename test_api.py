import requests

localhost = 'http://127.0.0.1:5000/'

# Create new video and print response
res = requests.put(localhost + '/video/1', {"name": "In the zoo", "uploader": "zooman"})
print(res.json())

# Get the new video added and print response
res = requests.get(localhost + '/video/1')
print(res.json())