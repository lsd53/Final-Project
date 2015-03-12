#! /usr/bin/env python
import SocketServer
import sys
import socket
import random
import time


data_list=[]
class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """
    
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
       	data_list.append(data)
       	socket.sendto(data.upper(), self.client_address)
        


def randguess():
	return str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

def giveHint(guess, answer):
        glist = list(str(guess))
        alist = list(str(answer))
        cows = 0
        bulls = 0
        for i in range(len(glist)):
                if glist[i] == alist[i]:
                        bulls += 1
                elif glist[i] in alist:
                        cows += 1
        return (bulls, cows)







HOST, PORT = "localhost", int(sys.argv[3])
socket.setdefaulttimeout(1)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print socket.getdefaulttimeout()
sock.sendto("Connection Established"+ "\n", (HOST, PORT))
try: 
	received = sock.recv(1024)
	server = SocketServer.UDPServer((HOST, int(sys.argv[2])), MyUDPHandler)
	i=0
	while True:
		numb=randguess()
		guess="GUESS:"+numb
		sock.sendto(guess,(HOST,int(sys.argv[3])))
		print "I guessed with "+numb
		
		
		while len(data_list)<i+1:
			server.handle_request()
			
		print "Opponenent guessed: " +data_list[i][6:]
		#time.sleep(.01)
		if data_list[i]=="WIN":
			print "I won!"
			break
		elif data_list[i]=="GUESS:"+sys.argv[1]:
			print "Opponent Won!"
			sock.sendto("WIN",(HOST,int(sys.argv[3])))
			break
		else:
			guess=data_list[i]
			guess_numb=guess[6:]
			
			s=giveHint(guess_numb,sys.argv[1])
			sock.sendto(str(s[0])+"B"+str(s[1])+"C",(HOST,int(sys.argv[3])))
		i=i+1
		while len(data_list)<i+1:
			server.handle_request()
		i=i+1









except socket.timeout:
	server = SocketServer.UDPServer((HOST, int(sys.argv[2])), MyUDPHandler)
	while len(data_list)<1:
		server.handle_request()
	i=1
	print data_list[0]
	
	while True:
		numb=randguess()
		guess="GUESS:"+numb
		sock.sendto(guess,(HOST,int(sys.argv[3])))
		print "I guessed with "+numb
		
		
		while len(data_list)<i+1:
			server.handle_request()
			
		print "Opponenent guessed: " +data_list[i][6:]
		#time.sleep(.01)
		if data_list[i]=="WIN":
			print "I won!"
			break
		elif data_list[i]=="GUESS:"+sys.argv[1]:
			print "Opponent Won!"
			sock.sendto("WIN",(HOST,int(sys.argv[3])))
			break
		else:
			guess=data_list[i]
			guess_numb=guess[6:]
			
			s=giveHint(guess_numb,sys.argv[1])
			sock.sendto(str(s[0])+"B"+str(s[1])+"C",(HOST,int(sys.argv[3])))
		i=i+1
		while len(data_list)<i+1:
			server.handle_request()
		i=i+1


				

		
    


