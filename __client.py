import socket

print("Client started working...")

s = socket.socket()

host = '127.0.1.1'
port = 12347

s.connect((host, port))

s.send(str.encode("GET 4"))
print(s.recv(1024))
