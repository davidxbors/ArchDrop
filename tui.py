import npyscreen, ___server, time, pickle

version = 0.7
devs = []
ddevs = []

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
		print(sel2.get_selected_objects())
		time.sleep(5)

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
