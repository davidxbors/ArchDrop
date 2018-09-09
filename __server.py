import socket

arr = ["david", "thomas", "yt", "test"]

def handleRecv(data, conn, addr):
	if "GET" in data:
		print(data)
		sendData = arr[int(data.split(' ')[1].strip("'"))]
		conn.send(str.encode(sendData))
	elif "POST" in data:
		getData = data.split(' ')[1].strip("'")
		arr.append(str(getData))
		conn.send(str.encode(str(len(arr) - 1)))
		

print("Server started....")

s = socket.socket()

host = socket.gethostname()
h = socket.gethostbyname(host)

print(h)

port = 12347

s.bind((h, port))

s.listen(5)

print("Listening for connections...")

while True:
	conn, addr = s.accept()
	print("{}:{} connected to the server...".format(addr[0], addr[1]))
	data = str(conn.recv(4096))
	handleRecv(data, conn, addr)
	conn.send(str.encode("Thomas thanks you for connecting"))
	conn.close()
