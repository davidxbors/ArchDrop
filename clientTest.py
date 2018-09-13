import pickle, socket, os, threading, _server

devs = []

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

def connDev(addr):
	print("Started connection protocol...")
	
	s = socket.socket()
	host, port = addr.split(':')[0], addr.split(':')[1]
	try:
		s.connect((host,int(port)))
	except:
		print("Connection failed...")
		input("Press any key to continue...")
		main()
		exit(0)

	print("Connection succeded...")
	msg = input("what message you have to transmit?")
	s.send(str.encode(msg))	
	rec = str(s.recv(1024)).split("'")[1]

	if str(rec) == "10Q":
		print("File sent!")
		input("Press any key to continue...")
		main()
		exit(0)
	else:
		print("There was an error :/")
		input("Press any key to continue...")
		main()
		exit(0)


def main():
	global devs
	readDevsList()
	i = 1
	
	#os.system("clear")
	if devs:
		for dev in devs:
			print("[{}] {} {}".format(i, dev["name"], dev["addr"]))
			i += 1

	print("[{}] Add new device".format(i))
	print("[{}] Exit the script".format(i+1))
	opt = input("Select option... ")

	if int(opt) == i:
		addNewDev()
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
	main1 = mainThread()
	server1 = serverThread(12348)

	main1.start()
	server1.start()
