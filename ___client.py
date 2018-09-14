import socket, os

DATA_BUFFER = 1024

def printStatus(fn, already):
	global size
	fn = os.path.basename(fn)
	os.system("clear")
	procent = int(already)/int(size) * 100
	statusBarA = '#' * int(procent)
	statusBarB = '.' * (100 - int(procent))
	statusBar = statusBarA + statusBarB
	if procent < 100:
		prompt = "Transfering {} {}% {} out of {} [{}]".format(fn,\
		int(procent), already, size, statusBar)
	else:
		prompt = "Transfering {} {}% {} out of {} [{}]".format(fn,\
		int(procent), already, size, statusBar)	

	print(prompt)

print("Client started working...")

s = socket.socket()

host = 'localhost'
port = 13347

s.connect((host, port))

fn = str(input("What file you want to open?"))

if(os.path.exists(fn)):
	name, ext, size = os.path.basename(fn).split(".")[0], os.path.basename(fn).split(".")[1], os.path.getsize(fn)
	print(name, ext, size)

	# send basic data to the server
	s.send(str.encode("{} {} {}".format(name, ext, size)))
	
	# open the file
	f = open(fn, "rb")
	tmp_read = f.read(DATA_BUFFER)
	alr = 0
	while(tmp_read):
		printStatus(fn, alr)
		s.send(tmp_read)
		alr += DATA_BUFFER
		tmp_read = f.read(DATA_BUFFER)
	printStatus(fn, size)
	
	s.close()
else:
	print("Failed... File doesn't exist...")
	exit(0)
