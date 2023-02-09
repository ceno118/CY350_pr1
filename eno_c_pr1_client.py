# MY ONLY REFERENCES USED WERE PYTHON DOCUMENTATION AND CLASS NOTES WHICH ARE COMMON KNOWLEDGE

import socket
import time

serverName = input("Enter server name or IP: ")
serverPort = int(input("Enter server port: "))

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
clientSocket.settimeout(1) # sets 1 second timeout

def getMonth(mon):
    if mon == 1:
        return "Jan"
    elif mon == 2:
        return "Feb"
    elif mon == 3:
        return "Mar"
    elif mon == 4:
        return "Apr"
    elif mon == 5:
        return "May"
    elif mon == 6:
        return "Jun"
    elif mon == 7:
        return "Jul"
    elif mon == 8:
        return "Aug"
    elif mon == 9:
        return "Sep"
    elif mon == 10:
        return "Oct"
    elif mon == 11:
        return "Nov"
    else:
        return "Dec"

msg = input("What message would you like to send?: ") #should be "ping", but other inputs demonstrate server's error checking

sent = 0
received = 0
dropped = 0
RTTs = []

for i in range(1,11):
    seq_number = i
    cur_time = time.localtime()
    month = cur_time.tm_mon
    timestring = str(cur_time.tm_mday) + " " + str(cur_time.tm_hour)+":"+str(cur_time.tm_min)+":"+str(cur_time.tm_sec)+" " + getMonth(month) + " " + str(cur_time.tm_year)
    message = msg + " " + str(seq_number) + " " + timestring
    clientSocket.send(message.encode())
    sent += 1
    send_time = time.time()
    try:
        modifiedMessage = clientSocket.recv(1024).decode()
        rtt = (time.time() - send_time) * 1000 # converts time to milliseconds
        RTTs.append(rtt)
        if modifiedMessage[:8] == "pong "+ message[5:8]: #makes sure the response message and seq number are correct
            print('From Server: ' + modifiedMessage + " RTT: " + str(rtt) + " seconds")
        else:
            print("Incorrect response from server: ", modifiedMessage)
        received += 1
        
    except:
        print("No response received for ping " + str(seq_number))
        dropped += 1

clientSocket.close()
print("")
print("Packets Sent: " + str(sent))
print("Packets Received: " + str(received))
print("Success Rate: " + str(int((received/sent) * 100)) + "%")
print("Minimum RTT: " + str(min(RTTs)) + " milliseconds")
print("Maximum RTT: " + str(max(RTTs)) + " milliseconds")
print("Average RTT: " + str(sum(RTTs) / len(RTTs)) + " milliseconds")
print("")