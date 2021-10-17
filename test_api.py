import requests

localhost = 'http://127.0.0.1:5000/'

#res = requests.post(localhost + '/users', {"name": "PewDewPie", "views": 12, "uploader": "1", "likes": 0})
#print(res.json())

# Create new uploader and print response
#res = requests.post(localhost + '/uploaders', {"uploader_name": "PweDiePie", "uploader_email": "uploader@pewdiepie.sw", "uploader_password": "123456"})
#print(res.json())

res = requests.get(localhost + '/uploaders')
print(res.json())

# Wrong uploader name; edit it
res = requests.put(localhost + '/uploader/1', {"uploader_name": "PewDiePie"})
print(res.json())

#res = requests.post(localhost + '/uploaders', {"uploader_name": "Maniya", "uploader_email": "kapilau@maniya.lk", "uploader_password": "piefm"})
#print(res.json())

# Make sure everything worked
#res = requests.get(localhost + '/uploader/1')
#print(res.json())

res = requests.delete(localhost + '/uploader/3')
#print(res.json())

res = requests.get(localhost + '/uploaders')