import socket, os

def server(port):
#	print("Server started....")
	
	s = socket.socket()
	
	host = socket.gethostname()
	h = socket.gethostbyname(host)
	
#	print(h)
	
	s.bind((h, port))
	
	s.listen(5)
	
#	print("Listening for connections...")
	
	while True:
		conn, addr = s.accept()
		os.system("clear")
#		print("{}:{} connected to the server...".format(addr[0], addr[1]))
		acc = str(input("{}:{} wants to send you a file...[y/n]"))
		if acc == "n":
			conn.close()
		elif acc == "y":
			data = str(conn.recv(4096))
			print(data)
			ack = input("is the message corrupted? [y/n]")
			if str(ack) == "n":
				conn.send(str.encode("10Q"))
			else:
				conn.send(str.encode("NEY"))
			conn.close()
		else:
			print("Option not supported, connection refused...")

server(12346)
