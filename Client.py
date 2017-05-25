from socket import *
import time
import timeit
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
	rcv_ack = int(list_substring[0]) # o primeiro elemento da mensagem eh o ack
	rcv_validation = int(list_substring[1]) # o ultimo elemento da mensagem eh o valor de validacao

	return rcv_ack, rcv_validation

def mostra_recebido(lista):
	if(lista[1]=='-1'):
		print 'Foi recebido o NACK do indice ',lista[0]
	else:
		print 'Foi recebido o ACK do indice  ',lista[0]


def main():
	serverName = '' 
	serverPort = 12000
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	message = raw_input('Digite a mensagem a ser enviada: ')
	msg_size = len(message) # tamanho da string digitada
	print '\nEscolha uma mensagem para ser destruida antes do envio ( de 0 a',len(message)-1,')	'
	print '** Digite -1 para nao destruir nenhuma **'
	escolha = raw_input('->')
	print '\n Escolha o tamanho da janela ( de 0 a ',len(message),')'
	print '** Digite -1 para tamanho padrao (4) **'
	tamanho_janela = raw_input('->')
	if(int(tamanho_janela)==-1):
		tamanho_janela = 4
	else:
		tamanho_janela = int(tamanho_janela)
	
	# Declaracao das variaveis de controle do GBN
	window_size = tamanho_janela # o tamanho da janela eh variavel, precisa mudar o valor aqui
	seq_number = 0
	window_base = 0
	#se o tamanho da mensagem for menor que o tamanho da janela, o tamanho maximo da janela deve ser o tamanho da mensagem

	if msg_size > window_size:
		window_max = window_size
	else:
		window_max = msg_size - 1
		
	ack = 0 # o ack sempre comeca com 0, na medida que o algoritmo roda, que ele sera incrementado
	nack = 0 # inicializando o nack como 0
	queue_nack = [] # vai ser a fila que contera os NACKS recebidos
	
	#Variavel que vai 'destruir' a mensagem criada, ou seja, vai fazer com que nao seja entregue ao servidor, 
	#para testar casos de perda
	destroy_message = int(escolha)  #inicializa a variavel de destruir a mensagem como -1. Se quiser destruir alguma, 
						 #deve mudar aqui

	message_list = message_assembler(message, msg_size) # vai criar a lista de mensagens que serao enviadas
															# para o servidor
	#loop principal do cliente
	#Enquanto o ACK nao for o valor do ultimo indice da mensagem, envia a mensagem
	#Quando for, o loop para, e quer dizer que toda a mensagem foi enviada com sucesso
	while ack != msg_size - 1:
			
			if window_base == seq_number:
				#colocar aqui a logica do timeout
				print '\n--------------------------------------------'
				for i in range(window_base, window_max):
					# se o i for igual a mensagem que quer ser destruida, continua o loop, assim n executa o
					#envio da mensagem
					
					if i == destroy_message:
					
						if destroy_message == window_max-1:
							print 'Timeout excedido!'
						destroy_message = -1
					else:
						seq_number += 1 # sequence number eh incrementado a cada vez que eh enviado um pacote
						print 'Esta sendo enviado o pacote:', message_list[i]
						start = timeit.default_timer()
						time.sleep(1)
						clientSocket.sendto(message_list[i],(serverName, serverPort))

				print 'Pacotes de', window_base, 'ao', window_max-1, 'enviados'

			received_message, serverAddress = clientSocket.recvfrom(2048)

			lista = []

			lista = received_message.split()

			mostra_recebido(lista)

			#print 'Mensagem recebida do servidor:', received_message
			stop = timeit.default_timer()
			ack, rcv_validation = message_disassembler(received_message) # pega o ack recebido e se n teve erro
			#print stop - start
			#se tiver tido erro, coloca ack na fila de nacks
			if rcv_validation == -1:
				queue_nack.append(ack) # colocar na fila qualquer ack que nao foi recebido

			#se a fila de nack nao for vazia, quer dizer que houve erro na transmissao
			if queue_nack != []:
				print 'Foi perdido o pacote:', queue_nack[0]
				print 'Reenviando'
				nack = queue_nack[0] # vai receber o primeiro elemento da lista, ou seja, o primeiro da fila
				queue_nack = []
				ack = nack
				seq_number = ack # sequence number tambem recebe o ack que foi perdido
				window_base = ack
				window_max = ack + window_size
			else:
				window_max += (ack+1 - window_base)
				window_base = ack + 1

			if window_max > msg_size:
				window_max = msg_size

	print '\n\nMensagem', message, 'enviada com sucesso'
	clientSocket.close()
	


main()