import socket

def checkport(host,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0)
    result=s.connect_ex((host,port))

    return result==0

def scanports(host,ports):

    for port in ports:
        if checkport(host, port):
            print("yes")
        else:
            print("closed")


host="127.0.0.1"
ports=range(1,1024)
scanports(host,ports)