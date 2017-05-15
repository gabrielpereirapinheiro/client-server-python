from socket import *
#CLIENT
#Victor Araujo Vieira - 140032801
#Gabriel Pereira Pinheiro - 140020764

#Funcao que dada a string que o usuario digitou e que vai ser enviada para o servidor, vai montar uma nova
#string com os a seguinte caracteristica: id caracter flag
#Vai retornar uma lista com todos as string montadas
def message_assembler(input_string, string_size):
	string_list = []

	#loop que vai criar a lista de messagens que serao enviadas para o servidor
	for i in range (0, string_size):
		if(i == string_size-1):
			new_string = `i` + ' ' + input_string[i] + ' ' + `0` # se for o ultimo pacote, vai ter a flag 0
		else:
			new_string = `i` + ' ' + input_string[i] + ' ' + `1` # se for qualquer pacote menos o ultimo, a flag eh 1
		
		string_list.append(new_string)

	return string_list # retorna a lista de strings geradas

#Funcao que vai retornar o valor do ACK e o valor da variavel de validacao do pacote
#Vai retornar o ack do pacote e o valor de validacao
def message_disassembler(received_message):
	list_substring = [] # vai receber todas as substring que tem na mensagem
	list_substring = received_message.split()
	print list_substring[0], list_substring[1]
	rcv_ack = int(list_substring[0]) # o primeiro elemento da mensagem eh o ack
	rcv_validation = int(list_substring[1]) # o ultimo elemento da mensagem eh o valor de validacao

	return rcv_ack, rcv_validation


def main():
	serverName = '' 
	serverPort = 12000
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	message = raw_input('Input lowercase sentence:')
	msg_size = len(message) # tamanho da string digitada

	# Declaracao das variaveis de controle do GBN
	window_size = 4
	seq_number = 0
	window_base = 0
	window_max = window_size
	ack = 0 # o ack sempre comeca com 0, na medida que o algoritmo roda, que ele sera incrementado
	nack = 0 # inicializando o nack como 0
	queue_ack = [] #vai ser a fila que contera os ACKs recebidos ate agora pelo cliente
	queue_nack = [] # vai ser a fila que contera os NACKS recebidos

	message_list = message_assembler(message, msg_size) # vai criar a lista de mensagens que serao enviadas
															# para o servidor
	#loop principal do cliente
	#Enquanto o ACK nao for o valor do ultimo indice da mensagem, envia a mensagem
	#Quando for, o loop para, e quer dizer que toda a mensagem foi enviada com sucesso
	while ack != msg_size - 1:
				
			if window_base == seq_number:
				#colocar aqui a logica do timeout
				for i in range(window_base, window_max):
					seq_number += 1 # sequence number eh incrementado a cada vez que eh enviado um pacote
					clientSocket.sendto(message_list[i],(serverName, serverPort)) 

			
			received_message, serverAddress = clientSocket.recvfrom(2048)
			#print received_message
			ack, rcv_validation = message_disassembler(received_message) # pega o ack recebido e se n teve erro
			#print ack
			#se tiver tido erro, coloca ack na fila de nacks, senao coloca ack na fila de ack
			if rcv_validation == -1:
				queue_nack.append(ack) # colocar na fila qualquer ack que nao foi recebido
			else:
				queue_ack.append(ack) # colocar na fila os acks que foram recebidos corretamente

			#se o ack for o sequencenumber - 1, quer dizer que o ultimo ack que deveria ser entregue chegou
			#if(ack == seq_number-1):

			#se a fila de nack nao for vazia, quer dizer que houve erro na transmissao
			if queue_nack != []:
				nack = queue_nack[0] # vai receber o primeiro elemento da lista, ou seja, o primeiro da fila
				queue_nack = []
				ack = nack
				window_base = ack
				window_max = ack + window_size
			else:
				window_max += (ack+1 - window_base)
				window_base = ack + 1

			if window_max > msg_size:
				window_max = msg_size

	

	clientSocket.close()
	#clientSocket.sendto(message,(serverName, serverPort)) 
	#modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
	#print modifiedMessage
	#print serverAddress
	


main()