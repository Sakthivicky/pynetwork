import requests

def fetchip(ip_address):
        try:
         url = f"https://ipinfo.io/{ip_address}/json"
         response=requests.get(url)
         if response.status_code==200:
           data=response.json()
           print(data)
           print("geolocation")
           print(f"location:{data.get('hostname')}")
           print(f"ipaddress:{data.get('ipaddress')}")
           print(f"location:{data.get('loc')}")
           print(f"location:{data.get('country')}")
         else:
           print("error")

        except Exception as e:
         print("errror ")
       
if __name__=="__main__":
   fetchip("8.8.8.8")