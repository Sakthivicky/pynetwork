import requests

url="https://jsonplaceholder.typicode.com/posts"

data={
    "title":"vettaiyain",
    "body":"tollywood",
    "useId":2
}

response= requests.post(url,data)

if response.status_code==201:
    print("manasilaayo")
    print(response.json())
else:
    print("error")