import socket

def dnslookup(domain):
     try:
      ipaddress=socket.gethostbyname(domain)
      print('ipaddress',ipaddress)
     except socket.gaierror:
        print("error")

if __name__=="__main__":
   domain="happymonial.com"
   dnslookup(domain)