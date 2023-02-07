import socket
import time
import random

print("hello")

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

# he doesn't want more than 30% packet loss, so make it random unless 3 have already been dropped

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message from: ", clientAddress, ": ", message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)


