import socket
import sys
import threading

SIZE = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname()
host_ip_addrss= socket.gethostbyname(hostName)
print("Server IP Address : " + host_ip_addrss)
port = 1024
serverSocket.bind((host_ip_addrss, port))

print("Hostname of server socket : " + hostName)
serverSocket.listen()

noOfClients = 3
clients = []
noOfClientsArrived = 0
clientAddresses = []
clientNames = []
threads = []
Send_string = "FILESEND"


def receiveAndSendMsg ( i,t ):
	while True:
		msg = clients[i].recv(1024)
		msg = msg.decode("utf-8")

		if (msg.find(Send_string) != -1):
			x = msg.split(" ")
			file = open(("server/"+x[1]),"wb")
			condition = True

			data = clients[i].recv(SIZE)
			file.write(data)
			while (len(data) >= SIZE ):
				data = clients[i].recv(SIZE)
				file.write(data)
			file.close()

			for j in range(noOfClientsArrived):
				if (i!=j):

					clients[j].send(bytes(msg, "utf-8"))
					file = open(("server/"+x[1]),"rb")
					
					data = file.read(SIZE)
					while data:
						clients[j].send(data)
						data = file.read(SIZE)
					file.close()
			
		else:
			msg = ("{} : ").format(clientNames[i]) + msg
			for j in range (noOfClientsArrived):
				if ( i != j ):
					clients[j].send(bytes(msg, "utf-8"))


for i in range(noOfClients):
	client, addr = serverSocket.accept()
	clients.append(client)
	clientAddresses.append(addr)
	clientNames.append(client.recv(SIZE).decode("utf-8"))
	
	noOfClientsArrived += 1
	for j in range(noOfClientsArrived):
		if ( i != j ):
			clients[j].send(bytes(clientNames[-1] + " has been added to the Chat", "utf-8"))
	
	threads.append(threading.Thread(target=receiveAndSendMsg,args=(i,6556)))
	threads[i].daemon = True
	threads[i].start()

for i in range(noOfClients):
	threads[i].join()