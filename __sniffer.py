from scapy.all import sniff

# pkts = sniff(iface="wlp3s0", count=10)
# pkts.show()
# chosen = input("Chose a packet to see better... ")
# pkts[int(chosen)].show()

counter = 0

def handlePackage(packet):
	global counter
	counter += 1
	return "{} {} => {} {}".format(counter, packet.src, \
		packet.dst, packet.getlayer(Raw).load)


sniff(iface="wlp3s0", prn=handlePackage)
