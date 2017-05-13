from socket import *
#CLIENT
#Victor Araujo Vieira - 140032801
#Gabriel Pereira Pinheiro - 140020764

#Funcao que dada a string que o usuario digitou e que vai ser enviada para o servidor, vai montar uma nova
#string com os a seguinte caracteristica: id caracter flag
#Vai retornar uma lista com todos as string montadas

#por que nao enviar palavras de uma frase digitada?
def message_assembler(input_string, string_size):
	string_list = []

	#loop que vai criar a lista de dicionarios com os pacotes
	for i in range (0, string_size):
		if(i == string_size-1):
			new_string = `i` + ' ' + input_string[i] + ' ' + `0` # se for o ultimo pacote, vai ter a flag 0
		else:
			new_string = `i` + ' ' + input_string[i] + ' ' + `1` # se for qualquer pacote menos o ultimo, a flag eh 1
		
		string_list.append(new_string)


	return string_list


serverName = '' 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')

string_list = message_assembler(message, len(message))
print string_list

for i in range(0,len(message)):
	clientSocket.sendto(string_list[i],(serverName,serverPort))

#clientSocket.sendto(message,(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print modifiedMessage
print serverAddress
clientSocket.close()