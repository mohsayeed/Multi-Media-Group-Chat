import socket
import sys
import threading

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname()
port = 1024
serverSocket.bind((hostName, port))

print("Hostname of server socket : " + hostName)
# print(" server will start on host : ", host)

## Doubt --> ???
serverSocket.listen()

noOfClients = 3
clients = []
noOfClientsArrived = 0
clientAddresses = []
threads = []



# for i in range(noOfClients):
# 	clients[i].send(bytes("Welcome Client {} !!".format(i+1), "utf-8"))

# while True:
# 	client, addr = s.accept()
# 	print("Connection to {} established".format(addr))
# 	client.send(bytes("Socket Programming in Python", "utf-8"))
# # 	client.close()

def receive_and_print(i):
	while True:
		msg = clients[i].recv(1024)
		msg = msg.decode("utf-8")
		# if ( msg == "quit" ):
		# 	clients[0].close()
		# 	break
		msg = "\t\t\t\tClient {} : ".format(i) + msg
		for j in range (noOfClientsArrived):
			if ( i != j ):
				clients[j].send(bytes(msg, "utf-8") )
		# for message in iter(lambda: clientSocket_1.recv(1024).decode("utf-8"), ''):
		# 	print(":", message)
		# 	print("")


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


# background_thread = threading.Thread(target=receive_and_print,args=(1,))
# background_thread.daemon = True
# background_thread.start()

# while True:
# 	req = input("Please enter your message: ")
# 	clientSocket_1.send(bytes(req,"utf-8"))
#     # print("Sent")
#     # print("")


# while True:
# 	msg = clients[0].recv(1024)
# 	msg = msg.decode("utf-8")
# 	# if ( msg == "quit" ):
# 	# 	clients[0].close()
# 	# 	break
# 	msg = "\t\t\t\t" + msg
# 	# for i in range (noOfClients):
# 	clients[1].send(bytes(msg, "utf-8") )






# name = input(str("Please enter your username: "))
# print("")
# print("Server is waiting for incoming connections")
# print("")
# s.listen(1)
# conn, addr = s.accept()
# print("Recieved connection")
# print("")
# s_name = conn.recv(1024)
# s_name = s_name.decode()
# print(s_name, "has joined the chat room")

# def input_and_send():
#     while 1:
#         message = name+" : "+input(str("Please enter your message: "))
#         conn.send(message.encode())
#         print("Sent")
#         print("")
# import threading
# background_thread = threading.Thread(target=input_and_send)
# background_thread.daemon = True
# background_thread.start()

# for message in iter(lambda: conn.recv(1024).decode(), ''):
#     print(s_name, ":", message)
#     print("")