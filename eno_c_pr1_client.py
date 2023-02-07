import socket
import time
import random

serverName = input("Enter server name: ")
serverPort = int(input("Enter server port: "))

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.connect((serverName, serverPort))

for i in range(1,11):
    message = 'ping'
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024).decode()
    print('From Server: ', modifiedMessage)
    clientSocket.close()