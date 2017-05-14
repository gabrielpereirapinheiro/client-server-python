from socket import *

#SERVER
#Victor Araujo Vieira - 140032801
#Gabriel Pereira Pinheiro - 140020764


#Fuction to show how index was recived from Client.py
def show_index(message):
	print 'Was recived the index ->'
	print message[0]

#This fuction going to create the ack + valid
def create_respost(message,valid):
	ack = message[0]+' '+valid

	return ack

#This fuction is used to see the valid of index's list	
def check_list_index(list,size):

	#if dont have problems with the list, status=0
	status = 0

	#all vector
	for i in range (0,size+1):
		#to see if not the last one
		if (i!= size):
			#convert char to int
			x = int(list[i])
			y = int(list[i+1])
			#if the actual + 1 not is the next
			if(x+1 != y):
				#define status = -1 to report erro
				status= -1

	# 0 means ok and -1 means erro			
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

    	#Check recive the value of status on fuction
    	check =check_list_index(list_of_index,last)	
    	
    	#If the value is -1, show error to user
    	if(check== -1):
    		print 'Erro, the message is not completed'
        	
    serverSocket.sendto(respost, clientAddress)