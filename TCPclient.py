import socket

serverName = 'localhost'
serverPort = 14000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence: ')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024).decode()
print('From Server: ', modifiedMessage)
clientSocket.close()
