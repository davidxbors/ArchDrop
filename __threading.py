import time, threading

class timeThread(threading.Thread):
	def __init__(self, tid, name, delay):
		threading.Thread.__init__(self)
		self.tid = tid
		self.name = name
		self.delay = delay

	def run(self):
		print("Starting {}...".format(self.tid))
		print_time(self.name, 5, self.delay)
		print("Exiting {}...".format(self.tid))

class echoThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		echo()

class helloThread(threading.Thread):
	def __init__(self, tid, name, delay):
		threading.Thread.__init__(self)
		self.tid = tid
		self.name = name
		self.delay = delay

	def run(self):
		print("Starting {}...".format(self.tid))
		print_hello(self.name, 5, self.delay)
		print("Exiting {}...".format(self.tid))


def print_time(name, counter, delay):
	while counter:
		time.sleep(delay)
		print("{}: {}".format(name, time.ctime(time.time())))
		counter -= 1

def print_hello(name, counter, delay):
	while counter:
		time.sleep(delay)
		print("{}: Hello!".format(name))
		counter -= 1

def echo():
	tmp = input("type smth... ")
	print(str(tmp))

t1 = timeThread(1, "t1", 1)
t2 = timeThread(2, "t2", 2)
t3 = helloThread(3, "t3", 2)
t4 = echoThread()

t1.start()
t2.start()
t3.start()
t4.start()

#print_time("procces1", 5, 1)
#print_time("procces2", 5, 2)
