# file transfer tcp
import socket

c = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
c.connect(('localhost',9990))

file = open("test.txt" ,"r")
data = file.read()

c.send("test.txt".encode())

print(f"serever: {c.recv(1024).decode()}")

c.send(data.encode())

print(f"server: {c.recv(1024).decode()}")

file.close()
c.close()
