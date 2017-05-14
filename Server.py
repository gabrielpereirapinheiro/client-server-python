from socket import *

#SERVER
#Victor Araujo Vieira - 140032801
#Gabriel Pereira Pinheiro - 140020764


#Fuction to show how index was recived from Client.py
def show_index(message):
	print 'Was recived the index ->'
	print message[0]

def create_respost(message,valid):
	ack = message[0]+' '+valid

	return ack
def check_list_index(list,size):

	status = 0

	for i in range (0,size+1):
		if (i!= size):
			x = int(list[i])
			y = int(list[i+1])
			if (x+1 != y):
				status-1

	return status 

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print 'The server is ready to receive'

#Create a new list to save all message receved
list_of_message = []

#Create a new list to save the index
list_of_index = []

#Create a new list to save the acks was envied
list_of_ack = []

while 1:
	#Recive the message from cliente
    message, clientAddress = serverSocket.recvfrom(2048)
   	#Show on terminal the index
    show_index(message)

    #Save the index
    list_of_index.append(message[0])

    #Save the message
    list_of_message.append(message[2])

    #Create the answer to send to client
    respost = create_respost(message,'0')

    #Save the ack before is send
    list_of_ack.append(respost)

    #If was the last package
    if(message[len(message)-1] == '0'):
    	#Show the complete message
    	print list_of_message
    	last = int(message[0])
    	check =check_list_index(list_of_index,last)	
    	print 'status'
    	print check 
        	
    serverSocket.sendto(respost, clientAddress)

   	