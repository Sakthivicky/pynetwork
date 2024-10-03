import requests
from bs4 import BeautifulSoup

url = "https://happymonial.com/" 

response=requests.get(url)

if response.status_code==200:
    print(response)
    soap=BeautifulSoup(response.content,'html.parser')
 
    headings=soap.find_all('p')
    
    for heading in headings:
        print(heading.get_text())


else:
    print("failed")


