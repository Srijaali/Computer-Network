import socket
import threading

#ip = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9999))
s.listen()
print("server waitning for connction")

while True:
    c,addr = s.accept()
    print(f"[new client] {addr} connected!")

    filename = c.recv(1024).decode()
    print(filename)

    c.close()
