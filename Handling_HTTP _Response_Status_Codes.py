import requests

url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)

print(response.json())


if response.status_code==200:
    print("success")
if response.status_code==404:
    print("internal error")
if response.status_code==500:
    print("server error")