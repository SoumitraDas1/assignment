def calculatesum(message,k):		#function to Calculate the sum of packets in the Message
	i= Sum = 0
	totalbits = len(message)	#Calculating total no of bits in the message
	while i<=totalbits - k:			#while loop runs upto last packet
		packet = message[i:i+k]	# Dividing sent message in packets of k bits.
		Sum = Sum + int(packet, 2)	# Converting the packet string to int and Calculating the sum of packets
		i = i + k					#increase the value of i to k bits
	return Sum
def findChecksum(SentMessage, k):	# Function to find the Checksum of Sent Message
	checksum = calculatesum(SentMessage,k)	#Calling calculatesum() function
	return checksum*(-1)					#return the negetive value of Sum	
	
def checkReceiverChecksum(ReceivedMessage, k, Checksum):
	rec_Sum = calculatesum(ReceivedMessage,k)	#calculating revived sum by Calling calculatesum() function
	ReceiverChecksum = rec_Sum + Checksum		#Calculating ReceiverChecksum by adding Received sum + checksum
	if ReceiverChecksum==0:						#if ReceiverChecksum is equal to 0 then no error
		print("Receiver Checksum is equal to 0. Therefore,")
		print("STATUS: ACCEPTED")
	else:										#if ReceiverChecksum is not equal to 0 then error detected 
		print("Receiver Checksum is not equal to 0. Therefore,")
		print("STATUS: ERROR DETECTED")
# Driver Code
if __name__=="__main__":
	SentMessage =     "10010101011000111001010011101100"
	k = 8
	ReceivedMessage = "10010101011000111001010011101100"
	Checksum = findChecksum(SentMessage, k)		# Calling the findChecksum() function
	ReceiverChecksum = checkReceiverChecksum(ReceivedMessage, k, Checksum) # Calling the checkReceiverChecksum() function