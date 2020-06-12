# UDPPingClient.py
#Declare the modules
import socket
from socket import AF_INET, SOCK_DGRAM
import time

# Address of UDP IP
# server set as localhost

UDP_IP_ADDRESS = '127.0.0.1'

# Declare UDP port number
UDP_PORT_NO = 12000

# Display the message
print('Pinging',UDP_IP_ADDRESS,UDP_PORT_NO)

#create the socket
clientSocket = socket.socket(AF_INET,SOCK_DGRAM)

#sets the timeout at 1 second for a reply from the server.
clientSocket.settimeout(1)
#variable to keep track of the sequence count
sequenceCount = 1

# Create list to store the Round Trip Time(Round_Trip_Time) values
Round_Trip_Time =[]

# Create a while loop to repeat the process continously
while sequenceCount<=10:
	#the current time
	start=time.time()
	# Assign sequence count in the variable named 'message'
	message = str(sequenceCount)

   	#client sends a message to the server
	clientSocket.sendto(message.encode('utf-8'),(UDP_IP_ADDRESS, UDP_PORT_NO))

    	#Declaration of try and catch
	#handle exceptions
	try:
		# recieves message from server
		message, address = clientSocket.recvfrom(1024)

        	# calculates the Round Trip Time
		elapsedTime = (time.time()-start)

        	Round_Trip_Time.append(elapsedTime)

        	print( 'Ping message number '+str(sequenceCount)+' Round_Trip_Time:' + str(elapsedTime) + ' secs')

    		#if no reply within 1 second then it
		#ping message as timed out

    		except socket.timeout:      
			print( 'Ping message number '+str(sequenceCount)+' timed out')

    	#incremented sequenceCount by 1
	sequenceCount+=1
	print( '')

    	# Create an 'if-statement' to check the sequence count is 10 or not
	if sequenceCount > 10:
		#Display message
		print('Number of packets sent:',sequenceCount-1)
		print('Number of packets received:',len(Round_Trip_Time))

        	#calculate loss rate and convert into string
		LossRate = str((10-len(Round_Trip_Time))*10)

        	print( 'Packet loss rate is:' + LossRate + ' %')

		#calculate the mean value
		mean = sum(Round_Trip_Time, 0.0)/ len(Round_Trip_Time)

        	#Display message for Maximum Round Trip Time(RTT)
		print( 'Maximum Round Trip Time(RTT) is:' + str(max(Round_Trip_Time)) + ' seconds')

        	#Display message for Minimum Round Trip Time(RTT)
		print( 'Minimum Round Trip Time(RTT) is:' + str(min(Round_Trip_Time)) + ' seconds')

        	#Display message for Average Round Trip Time(RTT)
		print( 'Average Round Trip Time(RTT) is:' + str(mean)+ ' seconds')

        	#closes the client socket after 10 packets
		clientSocket.close()