import socket
import sys
import threading

clientSocket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket_1.connect((socket.gethostname(), 1024))

def receive_and_print():
	for message in iter(lambda: clientSocket_1.recv(1024).decode("utf-8"), ''):
		print(message)

background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while True:
	req = input()
	clientSocket_1.send(bytes(req,"utf-8"))