# MY ONLY REFERENCES USED WERE PYTHON DOCUMENTATION AND CLASS NOTES WHICH ARE COMMON KNOWLEDGE

import socket
import random

serverPort = int(input("Enter server port: "))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

# he doesn't want more than 30% packet loss, so make it random unless 3 have already been dropped

dropped = 0

def decideLoss(): # this simulates up to 30% packet loss
    check = random.choice(range(100))
    if check < 30:
        global dropped
        dropped += 1
        return True
    else:
        return False


while True:

    message, clientAddress = serverSocket.recvfrom(2048)
    decoded = message.decode()
    print("Message from: ", clientAddress, ": ", decoded)

    if dropped < 3 and decideLoss(): # checks if we've hit 30% loss
        print("drop") # not necessary, but helps the user see when things are dropped

    elif decoded[:4] == "ping":
        modifiedMessage = "pong" + message[4:].decode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    else:
        dropped += 1


