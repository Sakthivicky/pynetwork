import requests

url = "https://self-signed.badssl.com/"

response = requests.get(url, verify=False)

if response.status_code == 200:
    print("successful!")
else:
    print(f"Failed  {response.status_code}")
