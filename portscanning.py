import socket

def scanport(ip,port):

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
        sock.settimeout(1)
        result=sock.connect_ex((ip,port))
    if result==0:
        print(f"portno:{port} ipno:{ip}")
    else:
        print("failed")
   


def main():
    ip="54.182.0.76"
    start=1
    end=200

    for port in range(start,end + 1):
        scanport(ip,port)

if __name__ == "__main__":
    main()