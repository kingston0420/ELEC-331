#UDP Server
from socket import * 

#this makes the code run on other machines too
hostname = gethostname()  #Get the hostname
print(hostname)

#Create socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  #IPV4, UDP
serverSocket.bind((hostname, serverPort))
print("The server is ready to receive")

#Receive message and send response
while True:
	message, clientAddress = serverSocket.recvfrom(2048) #2048 is the buffer size
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)