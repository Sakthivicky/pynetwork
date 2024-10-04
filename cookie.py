import requests

response = requests.get('https://httpbin.org/cookies/set?name=value')


cookies=response.cookies

for cookie in cookies:
 
    print(f"cookie: {cookie.name}") 

result=response.json()
print("finshed:",result)


session=requests.session()

session.cookies.set('names',"values")

response =session.get('https://happymonial.com/')
print(response.text)