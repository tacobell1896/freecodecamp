#!/usr/bin/python3

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

serverSocket.bind((host, port))

# specifies the amount of computers that can listen in
serverSocket.listen(3)

while True:
    clientsocket, address = serverSocket.accept()

    print("receive connection from " % str(address)) 

    message = 'Welcome, thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()