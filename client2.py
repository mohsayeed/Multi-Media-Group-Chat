import socket
import sys
import threading
SIZE = 1024
clientSocket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket_2.connect((socket.gethostname(), 1024))


def receive_and_print():
	while True:
		message = clientSocket_2.recv(1024)
		message = message.decode("utf-8")
		if(message=="FILESEND"):
			print(message)
			file = open(("client2/_ss_"+"client2"+".jpg"),"wb")
			condition = True
			while condition:
				image = clientSocket_2.recv(SIZE)
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
		clientSocket_2.send(bytes(req,"utf-8"))
		print("tureasdjlfljksfdalkjfdsal;adfsl;k")
		file = open("data/ss.jpg","rb")
		data = file.read(SIZE)
		while data:
			clientSocket_2.send(data)
			data = file.read(SIZE)
		file.close()
		req = 'end'
		clientSocket_2.send(bytes(req,"utf-8"))
	else:
		clientSocket_2.send(bytes(req,"utf-8"))
