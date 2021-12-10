import socket
import sys
import threading

clientSocket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostIpAddr = input("Please Give the Ip Address")
clientSocket_1.connect((hostIpAddr, 1024))
SIZE=1024
Send_string = "FILESEND"

def receive_and_print():
	while True:
		message = clientSocket_1.recv(1024)
		message = message.decode("utf-8")
		if(message.find(Send_string)!=-1):
			print(message)
			x = message.split(" ")
			file = open(("client1/"+x[1]),"wb")
			condition = True
			while condition:
				image = clientSocket_1.recv(SIZE)
				s= str(image)
				if s[len(s)-4:len(s)-1] == "end":
					condition = False
				file.write(image)				
			file.close()
		else:
			print(message)

background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while True:
	req = input()
	if (req.count("FILESEND")>0):
		clientSocket_1.send(bytes(req,"utf-8"))
		x = req.split(" ")
		file = open("data/"+x[1],"rb")
		data = file.read(SIZE)
		while data:
			clientSocket_1.send(data)
			data = file.read(SIZE)
		file.close()
		req = 'end'
		clientSocket_1.send(bytes(req,"utf-8"))
	else:
		clientSocket_1.send(bytes(req,"utf-8"))