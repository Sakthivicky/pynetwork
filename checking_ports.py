import socket

def open_sockets(ip,start,end):
  openports=[]
  print(f"searching for ports in the ip {ip}")

  for port  in range(start,end +1 ):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((ip,port))


    if result==0:
      openports.append(port)
      print(openports)
    sock.close()

  if not openports:
      print("no results")

if __name__ == "__main__":
  ip="happymonial.com"
  start=1
  end=82
  open_sockets(ip,start,end)
 
 
 