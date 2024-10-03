import requests

url="https://jsonplaceholder.typicode.com/posts"

response=requests.get(url)

if response.status_code==200:
    data=response.json()
    first=data[0]
    id=first.get('id')
    print(id)

    for i in data:
        print(f"Post no :{i.get('id')}")
        
else:
    print("error")

