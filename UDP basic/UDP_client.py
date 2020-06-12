from socket import *

#Create socket
serverName = gethostname()
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Send massage to the server
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))

#Receive response from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

#Close UDP client
clientSocket.close()