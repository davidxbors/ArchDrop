from scapy.all import *

#def main():
#	pkts = sniff(iface="wlp3s0", count=3)
#	pkts[0].show()

def sendMessage(msg):
	send(IP(src="192.168.100.3", dst="7.7.7.7")/ICMP()/msg)

def main():
	sendMessage("Hello world!")

if __name__ == "__main__":
	main()
