import pickle, socket, os, threading, ___server

devs = []

DATA_BUFFER = 1024

def printStatus(fn, already, size):
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

def saveDevsList():
	global devs
	with open("devsList.pkl", 'wb') as f:
		pickle.dump(devs, f, pickle.HIGHEST_PROTOCOL)	

def readDevsList():
	global devs
	with open("devsList.pkl", 'rb') as f:
		devs = pickle.load(f)

def addNewDev():
	global devs
	name = input("Type a friendly name for the device... ")
	addr = input("Type the address of the device... ")
	dct = {"name": name, "addr": addr}
	devs.append(dct)
	saveDevsList()
	main()
	exit(0)

def connDev(addr):
	print("Connection protocol started...")
	
	s = socket.socket()

	try:	
		host, port = addr.split(':')[0], addr.split(':')[1]
	except:
		print("Device not recognised... Try adding it again..")
		input("Press any key to continue...")
		main()
		exit(0)
	
	try:
		s.connect((host, int(port)))
	except:
		print("Connection failed...")	
		input("Press any key to continue...")
		main()
		exit(0)
	
	fn = str(input("What file you want to open?"))
	
	if(os.path.exists(fn)):
		try:
			name, ext, size = os.path.basename(fn).split(".")[0], os.path.basename(fn).split(".")[1], os.path.getsize(fn)
			print(name, ext, size)
		
			# send basic data to the server
			s.send(str.encode("{} {} {}".format(name, ext, size)))

			ack = str(s.recv(4096))
			if ack.split("'")[1] == "BOO":
				print("Connection not accepted...")
				input("Press any key to continue...")
				main()
				exit(0)
			else:
				pass
			
			# open the file
			f = open(fn, "rb")
			tmp_read = f.read(DATA_BUFFER)
			alr = 0
			while(tmp_read):
				printStatus(fn, alr, size)
				s.send(tmp_read)
				alr += DATA_BUFFER
				tmp_read = f.read(DATA_BUFFER)
			printStatus(fn, size, size)
			input("Press any key to continue...")			

			s.close()
		except:
			print("There was a connection problem...")
			input("Press any key to continue...")
		main()
		exit(0)
	else:
		print("Failed... File doesn't exist...")
		exit(0)

def main():
	global devs
	readDevsList()
	i = 1
	
	os.system("clear")
	if devs:
		for dev in devs:
			print("[{}] {} {}".format(i, dev["name"], dev["addr"]))
			i += 1

	print("[{}] Add new device".format(i))
	print("[{}] Exit the script".format(i+1))
	opt = input("Select option... ")

	if int(opt) == i:
		addNewDev()
	elif int(opt) == -1:
		pass
	elif int(opt) < i and int(opt) >=1:
		connDev(devs[int(opt)-1]["addr"])
	elif int(opt) == i + 1:
		exit(0)
	else:
		print("Option unavailable!")
		main()
		exit(0)

class mainThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		main()

class serverThread(threading.Thread):
	def __init__(self, port):
		threading.Thread.__init__(self)
		self.port = port

	def run(self):
		_server.server(self.port)


if __name__ == "__main__":
	tmp = str(input("Do you want to send or recieve a file? [s/r]"))
	if tmp == "s":
		main()
	elif tmp == "r":
		___server.server(12347)
	else:
		print("Option not existent... Exiting...")
		exit(0)
	
