from socket import *
#SERVER
#Victor Araujo Vieira - 140032801
#Gabriel Pereira Pinheiro - 140020764

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print 'The server is ready to receive'
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print message
    if(message[len(message)-1] == '0'):
    	print 'fim da mensagem!'
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
