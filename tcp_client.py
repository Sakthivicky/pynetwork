import socket

def client():

    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address=('localhost',65432)
    clientsocket.connect(address)

    try:
        statement="Hi ! mr sakthi & vicky"
        clientsocket.sendall(statement.encode())
        
        data=clientsocket.recv(1024)
        print(f'recieving: {data.decode()}')
    finally:
        clientsocket.close()

if  __name__=="__main__":
   client()