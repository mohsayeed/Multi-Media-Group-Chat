import socket
import sys
import threading

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname()
port = 1024
serverSocket.bind((hostName, port))

print("Hostname of server socket : " + hostName)
serverSocket.listen()

noOfClients = 3
clients = []
noOfClientsArrived = 0
clientAddresses = []
threads = []

def receive_and_print(i):
	while True:
		msg = clients[i].recv(1024)
		msg = msg.decode("utf-8")
		msg = "\t\t\t\tClient {} : ".format(i) + msg
		for j in range (noOfClientsArrived):
			if ( i != j ):
				clients[j].send(bytes(msg, "utf-8") )


for i in range(noOfClients):
	client, addr = serverSocket.accept()
	clients.append(client)
	clientAddresses.append(addr)
	noOfClientsArrived += 1
	threads.append(threading.Thread(target=receive_and_print,args=(i,)))
	threads[i].daemon = True
	threads[i].start()

for i in range(noOfClients):
	threads[i].join()