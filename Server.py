from socket import *

#SERVER
#Victor Araujo Vieira 
#Gabriel Pereira Pinheiro

#Funcao que mostra na tela o que foi recebido

def show_index(message,aux):
	print 'Foi recebido a mensagem-> ',message[len(message)-3]
	print 'index -> ',aux[0]
	if(len(aux)==3):
		print 'flag -> ',aux[2]
		if(aux[2]=='0'):
			print '------Ultimo pacote recebido------'
	if(len(aux)==2):
		print 'flag -> ',aux[1]
		if(aux[1]=='0'):
			print '------Ultumo pacote recebido------'		
	print ''
#Funcao que ira criar a respostaar(ACK)
#que e a concatenacao do indice + ' ' + validade
def create_resposta(message,list_msg,flag):

	#Lista vazia para usar split
	new_list = []

	#Inicialmente igual a 0
	valid = '0'

	#new_list com mensagem recebida do cliente
	new_list = message.split()

	#tamanho da listas com as mensagens ja recebidas
	size = len(list_msg)

	#Indice recevido
	valor = new_list[0]

	#Inteiro recebido
	valor = int(valor)

	#Caracter recebido
	retorno = new_list[0]

	#Se a lista nao e nula
	if(size>0):
		aux = int(list_msg[size-1])
		
		if(valor-1 != aux):
			valid = '-1'
			retorno=aux +1 
			retorno = str(retorno)
			if(flag==0):
				print '----- Mensagem do index',valor,'descartada-----'
				print ''

	ack = retorno+' '+valid

	return ack
#This fuction is going to look if the index exists in list
def check_index_recive(message,list):

	status = 0
	valor = -1
	
	list_aux =[]
	list_aux = message.split()

	if(len(list)!= 0):
		for i in range(0,len(list)):

			index=int(list[i])
			valor = list_aux[0]
			
			if(valor==index):
				status = -1

	return status

#This fuction is used to see the valid of index's list	
def check_list_index(list,size):

	#if dont have problems with the list, status=0
	status = 0
	# 0 means ok and -1 means erro			
	return status
def junta_messagem(lista_de_messagens):
	
	string = ' '

	for i in range (0,len(lista_de_messagens)):
		string = string + str(lista_de_messagens[i]) 
	return string

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print '-----O servidor esta pronto para receber -----\n'

list_of_message = []

list_of_index = []

#Create a new list to save the acks that were sent
list_of_ack = []

aux_list = []

while 1:
	#Recive the message from cliente
    message, clientAddress = serverSocket.recvfrom(2048)
   	#Show on terminal the index
    
   	
    present_in_list = check_index_recive(message,list_of_index)
    aux_list = message.split()
    show_index(message,aux_list)    
    #print aux_list[0]
    
    if(present_in_list==0):

	 
	    #Create the answer to send to client
	    resposta = create_resposta(message,list_of_index,0)

	    status_resposta = resposta[len(resposta)-1]

	    #Se for um ack
	    if(status_resposta== '0'):
		    

	       #Save the index
		    list_of_index.append(aux_list[0])

		    #Save the message
		    #-3 is to find the message in the vector based in the end.
		    list_of_message.append(message[len(message)-3])
		    
		    
		    #Save the ack before is send
		    list_of_ack.append(resposta)

		    #print 'valor --->'+ message[len(message)-1]

		    #last_index = message[0]

		    #If was the last package
		    if(message[len(message)-1] == '0'):
		    	#Show the complete message
		    	
		    	mensagem_completa=junta_messagem(list_of_message)
		    	print '\nA mensagem recebida foi ->',mensagem_completa,' <-'
		    	print '\n----- O servidor esta pronota para receber -----\n'
		    	

		    	last = int(message[0])

		    	#Check recive the value of status on fuction
		    	check =check_list_index(list_of_index,last)	
		    	
		    	#If the value is -1, show error to user
		    	if(check== -1):
		    		print 'Erro, the message is not completed'
		    	#clean_lists(list_of_index,list_of_message,list_of_ack)

		    	#Clean al lists
		 			
		    	list_of_message = []
		    	list_of_ack=[]
		    	list_of_index=[]
		# Se for um NACK    	
	    else:

	    	resposta = create_resposta(message,list_of_index,1)

	    	if(message[len(message)-1] == '0'):
		    	#Show the complete message
		    	last = int(message[0])

		    	#Check recive the value of status on fuction
		    	check =check_list_index(list_of_index,last)	
		    	
		    	#If the value is -1, show error to user
		    	if(check== -1):
		    		print 'Erro, the message is not completed'

		    	#clean_lists(list_of_index,list_of_message,list_of_ack)	

			   	list_of_message = []
		    	list_of_ack=[]
		    	list_of_index=[]

    serverSocket.sendto(resposta, clientAddress)	
    
   
