import requests

url = "https://jsonplaceholder.typicode.com/posts"

headers={
"User-agents":"Myapp/1.0",
"content-type":"application/json",
"authentication":"bearer",
"accept":"application/json"
}
response=requests.get(url,headers)
if response.status_code==200:
    print(response.json())
else:
    print("error")