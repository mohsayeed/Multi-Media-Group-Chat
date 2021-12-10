import socket
import sys
import threading
SIZE = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname()
host_ip_addrss= socket.gethostbyname(hostName)
print(host_ip_addrss)
port = 1024
serverSocket.bind((host_ip_addrss, port))

print("Hostname of server socket : " + hostName)
serverSocket.listen()

noOfClients = 3
clients = []
noOfClientsArrived = 0
clientAddresses = []
threads = []
Send_string = "FILESEND"


def receive_and_print(i,t):
	while True:
		msg = clients[i].recv(1024)
		msg = msg.decode("utf-8")
		if(msg.find(Send_string)!=-1):
			x = msg.split(" ")
			file = open(("server/"+x[1]),"wb")
			condition = True
			while condition:
				image = clients[i].recv(SIZE)
				s= str(image)
				if s[len(s)-4:len(s)-1] == "end":
					condition = False
				file.write(image)				
			file.close()
			print("closecd")
			for j in range(noOfClientsArrived):
				if (i!=j):
					clients[j].send(bytes(msg, "utf-8"))
					file = open(("server/"+x[1]),"rb")
					data = file.read(SIZE)
					while data:
						clients[j].send(data)
						data = file.read(SIZE)
					file.close()
					req = 'end'
					clients[j].send(bytes(req,"utf-8"))
					
			
		else:
			msg = "\t\t\t\tClient {} : ".format(i) + msg
			for j in range (noOfClientsArrived):
				if ( i != j ):
					clients[j].send(bytes(msg, "utf-8"))


for i in range(noOfClients):
	client, addr = serverSocket.accept()
	clients.append(client)
	clientAddresses.append(addr)
	print("one client added")
	noOfClientsArrived += 1
	threads.append(threading.Thread(target=receive_and_print,args=(i,6556)))
	threads[i].daemon = True
	threads[i].start()

for i in range(noOfClients):
	threads[i].join()