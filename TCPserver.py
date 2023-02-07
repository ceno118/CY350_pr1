import socket

serverPort = 13000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    capitalizedMessage = message.upper()
    connectionSocket.send(capitalizedMessage.encode())
    connectionSocket.close()
