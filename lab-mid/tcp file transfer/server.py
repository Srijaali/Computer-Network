import socket

print("server starting")
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(('localhost' , 9990))
s.listen()
print("server listening")

while True:
    c,addr = s.accept()
    print(f"connected to: {addr}")

    filename =c.recv(1024).decode()
    print(f"recved filename: {filename}")
    file = open(filename , "w")
    c.send("filename recved successfully!".encode())

    data = c.recv(1024).decode()
    print("file data recieved.")
    file.write(data)
    c.send("fils data recvd".encode())

    file.close()
    c.close()
    print("disc")
