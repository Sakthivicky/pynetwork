import socket

def server():
    serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip='localhost'
    port=65432
    address=(ip,port)
    serversocket.bind(address)
     
    serversocket.listen(1)
    print("succefully running")

    while True:
        clientsocket,addr=serversocket.accept()
        try:
         data=clientsocket.recv(1024)
         print(f'data:{ data.decode()}')
         if not data:
            break
         response="this works !"
         clientsocket.sendall(response.encode())

        finally:
         clientsocket.close()

if __name__=='__main__':
   server()