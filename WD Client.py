#client side
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
print("client socket is connected to ", port)
print(s.recv(1024).decode("utf-16"))
s.send("thank you server".encode("utf-16"))

