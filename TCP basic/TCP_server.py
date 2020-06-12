from socket import*

#This makes the code competable for all the end system
hostname = gethostname()

#Creat socket and listen for request
s = socket(AF_INET, SOCK_STREAM) #IPv4, TCP
s.bind((hostname, 12000))
s.listen(1)
print("The server is ready to receive")

while True:
	#Accept incoming request
	conn, addr = s.accept()   #accept the request and teturn a new socket 'conn', conn refer to the connection socket
	
	#Decode the received message and print it out
	recv_data = conn.recv(4096).decode()
	print('The data received by the server:', str(recv_data))
	print('Type:', type(recv_data))

	#Generate, encode, and send the response 
	capitalizedSentence = recv_data.upper()
	conn.sendall(capitalizedSentence.encode())

	#Close TCP connection
	conn.close()
	print("Connection closed")	