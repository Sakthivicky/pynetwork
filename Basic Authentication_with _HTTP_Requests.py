import requests
from requests.auth import HTTPBasicAuth

url=("https://httpbin.org/basic-auth/user/passswd")
response=requests.get(url,auth=HTTPBasicAuth('user','passswd'))

if response.status_code==200:
    print("successfull")
    print( response.json())
else:
    print("Authentication failed")