import socket, os

DATA_BUFFER = 1024

def pick_fn(n, e):
	fn = "./downloads/{}.{}".format(n, e)
	if(os.path.exists(fn)):
		i = 1
		while os.path.exists(fn):
			fn = "./downloads/{}{}.{}".format(n, i, e)
			i = i + 1
	return fn

def printStatus(fn, already, size):
	fn = os.path.basename(fn)
	os.system("clear")
	procent = int(already)/int(size) * 100
	statusBarA = '#' * int(procent)
	statusBarB = '.' * (100 - int(procent))
	statusBar = statusBarA + statusBarB
	if procent < 100:
		prompt = "Downloading {} {}% {} out of {} [{}]".format(fn,\
		int(procent), already, size, statusBar)
	else:
		prompt = "Downloaded {} {}% {} out of {} [{}]".format(fn,\
		int(procent), already, size, statusBar)	

	print(prompt)

def server(port):	
	s = socket.socket()
	s.bind(("localhost", port))
	
	s.listen(5)
	
	#print("Server listenin'...")
	
	while True:
		conn, addr = s.accept()
	
		metadata = str(conn.recv(4096))
		if metadata != "b''":
			tmp = input("Accept files from {}:{}?[y/n] ".format(addr[0],addr[1]))
			if tmp == "y":
				metadata = metadata.split("'")[1]
			
				name, ext, size = metadata.split(" ")[0], metadata.split(" ")[1], metadata.split(" ")[2]
				
				fn = pick_fn(name, ext)
				f = open(fn, "wb")
				
				alr = 0	
				tmp_get = conn.recv(DATA_BUFFER)
				while tmp_get:
					printStatus(fn, alr, size)
					f.write(tmp_get)
					alr += DATA_BUFFER
					tmp_get = conn.recv(DATA_BUFFER)
				printStatus(fn, size, size)
			
				f.close()
			else:
				pass
		conn.close()
	
	s.close()

#server(13347)		
