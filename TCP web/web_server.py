#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
servePort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		message.decode()
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()

		#Send one GTTP header line into socket
		message0 = ('\nHTTP\1.1 200 OK\n')
		connectionSocket.send(message0.encode())
		
		#Send the content of the request file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close()


	except IOError:
		#send response message for file not found
		message1 = "\nHTTP\1.1 404 Not Found\n"
		connectionSocket.send(message1.encode())
		#Close client socket

		connectionSocket.close()
	
serverSocker.close()
		