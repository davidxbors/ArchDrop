import npyscreen, ___server, time, pickle, socket, os

version = 0.7
devs = []
ddevs = []

class FileDialog(npyscreen.Form):
	def create(self):
	        key_of_choice = 'p'
        	what_to_display = 'Press {} for popup \n Press escape key to quit'.format(key_of_choice)

	        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application
        	self.add_handlers({key_of_choice: self.spawn_file_dialog})
        	self.add(npyscreen.FixedText, value=what_to_display)	

	def spawn_file_dialog(self, ckp):
		selF = npyscreen.selectFile()
		npyscreen.notify_wait("ret: {}".format(selF), title="ret")

def conn(sel):
#	cmd = "notify-send '{}'".format(sel)
#	os.system(cmd)

	if sel.split(" ")[0] == "Add":
#		os.system("notify-send 'not a dev'")
		print("Not a dev...")
		exit(0)

	if sel.split(" ")[0] == "Exit":
#		os.system("notify-send 'not a dev'")
		print("Not a dev...")
		exit(0)

	
#	os.system("notify-send 'Got b4 ss!'")

	s = socket.socket()
	
#	os.system("notify-send 'Got a ss!'")
	
	try:
		addr = sel.split(" ")[1]
		host, port = addr.split(":")[0], int(addr.split(":")[1])
	except:
		print("Device not recognised... Try adding it again...")
		exit(0)

	try:
		s.connect((host, port))

		os.system("notify-send 'Got b4 fd!'")
		fd = FileDialog()
		fd.run()
	except:
		print("Connection failed...")
		exit(0)

def readDevsList():
	global devs
	with open("devsList.pkl", 'rb') as f:
		devs = pickle.load(f)

class selAddr(npyscreen.NPSApp):
	def main(self):
		global ddevs

		F = npyscreen.Form(name = "ArchDrop {}".format(version),)
	
		sel2 = F.add(npyscreen.TitleSelectOne, max_height=4, value=[1,], name = "Select a device to send data to or an option from below:", values = ddevs, scroll_exit=True)

		F.edit()
		conn(sel2.get_selected_objects()[0])

def manageDialog(opt):
	if "Recieve" == str(opt):
		___server.server(12347)
	elif "Send" == str(opt):
		readDevsList()
		
		print(devs)

		for dev in devs:
			tmp = "{} {}".format(dev["name"], dev["addr"])
			ddevs.append(tmp)

		ddevs.append("Add new device")
		ddevs.append("Exit the script")
	
		sa = selAddr()
		sa.run()

class D1(npyscreen.NPSApp):
	def main(self):
		F = npyscreen.Form(name = "ArchDrop {}".format(version),)
		sel1 = F.add(npyscreen.TitleSelectOne, max_height=4, value=[1,], name="Do you want to send or recieve?", values = ["Send", "Recieve"], scroll_exit=True)
		
		# let the user interact with the form
		F.edit()

		# print(sel1.get_selected_objects())
		manageDialog(sel1.get_selected_objects()[0])

MyApp = D1()
MyApp.run()
