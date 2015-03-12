#! /usr/bin/env python
import SocketServer
import sys
import socket
import random

class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """
    data_list=[]
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        self.data_list.append(data)
        print self.data_list
        socket.sendto(data.upper(), self.client_address)
        


def randguess():
	return str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

HOST, PORT = "localhost", int(sys.argv[3])
socket.setdefaulttimeout(1)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print socket.getdefaulttimeout()
sock.sendto("Connection Established"+ "\n", (HOST, PORT))
try: 
	received = sock.recv(1024)
	server = SocketServer.UDPServer((HOST, int(sys.argv[2])), MyUDPHandler)
		#while True:
		#server.handle_request()

except socket.timeout:
	server = SocketServer.UDPServer((HOST, int(sys.argv[2])), MyUDPHandler)
	while True:

		server.handle_request()
		
    


