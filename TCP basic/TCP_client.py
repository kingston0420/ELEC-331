from socket import*

hostname = gethostname()

#Create socket and establish connection
s = socket(AF_INET, SOCK_STREAM)

#Send encoded message to the server
s.connect((hostname, 12000))	#establish connection with the server
message = input('Input lowercase sentence:')
s.sendall(message.encode())

#check the data received from the TCP server before decoding 
data = s.recv(4096)
print('Received data before decoding:' data)
print(type(data))

#check the data after decoding
data = data.decode()
print ('Received data after decoding:', data)
print(type(data))

#close
s.close