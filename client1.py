import socket
import sys
import threading

clientSocket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket_1.connect((socket.gethostname(), 1024))

# completeMsg = ""

# while True:
# 	msg = clientSocket_1.recv(7)
# 	if len(msg) == 0: break
# 	completeMsg += msg.decode("utf-8")
	
# print(completeMsg)

# name = input(str("Please enter your username : "))
# print(" Connected to chat server")
# s.send(name.encode())

def receive_and_print():
	for message in iter(lambda: clientSocket_1.recv(1024).decode("utf-8"), ''):
		print(message)

background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while True:
	req = input()
	clientSocket_1.send(bytes(req,"utf-8"))
    # print("Sent")
    # print("")