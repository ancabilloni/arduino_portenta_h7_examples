# Importing the neccessary libraries
import network, time, usocket

# Setup static ip address and masknet

lan = network.LAN()
lan.active(True)
lan.ifconfig(('192.168.1.177', '255.255.255.0', '192.168.1.1', '192.168.1.1'))

# Create socket and bind to port
s = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
s.bind(("192.168.1.177", 8888))

# Loop indefinitely. Print any received datagram and send a reply
while (True):
    # Nothing else to do.
    data, addr = s.recvfrom(1024)
    print("From {}, port {}".format(addr[0], addr[1]))
    print("Content: {}".format(data))
    reply = b'reply: ' + data
    s.sendto(reply, addr)
