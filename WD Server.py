#Serverside
import socket
s=socket.socket()  #to make communication
host =socket.gethostname()
port=12345
s.bind((host,port))  # to start the server
print("socket is binded to",port)
s.listen(5)
print("socket is listening")
while True:
    a,b=s.accept()
    print("got a connection from ",b)
    a.send("hi....client good  morning".encode("utf-16"))
    print(a.recv(1024).decode("utf-16"))
    a.close()

