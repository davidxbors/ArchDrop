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

def printStatus(fn, already):
	global size
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

s = socket.socket()
s.bind(("localhost", 13347))

s.listen(5)

print("Server listenin'...")

while True:
	conn, addr = s.accept()

	metadata = str(conn.recv(4096))
	print(metadata)
	if metadata != "b''":
		metadata = metadata.split("'")[1]
	
		name, ext, size = metadata.split(" ")[0], metadata.split(" ")[1], metadata.split(" ")[2]
		
		fn = pick_fn(name, ext)
		f = open(fn, "wb")
		
		alr = 0	
		tmp_get = conn.recv(DATA_BUFFER)
		while tmp_get:
			printStatus(fn, alr)
			f.write(tmp_get)
			alr += DATA_BUFFER
			tmp_get = conn.recv(DATA_BUFFER)
		printStatus(fn, size)
	
		f.close()
	conn.close()

s.close()
	
