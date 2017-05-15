# tr2_socket
Trabalho da disciplina de Teleinformatica e Redes 2 - SOCKET

Alunos : GABRIEL PEREIRA PINHEIRO   
         VICTOR ARAUJO VIEIRA

Os sites abaixo possuem pseudocodigos do funcionamento do GBN
Sites de apoio: https://gist.github.com/Rinnejade/60b876c6b1eda277fa205e1237eb9032
				https://en.wikipedia.org/wiki/Go-Back-N_ARQ


O site abaixo possui como usar os metodos settimeout e gettimeout do socket:
https://docs.python.org/2/library/socket.html

Baseado nos slides do Kurose, capitulo 3. Mais especificamente, as FSM, nos slides 47 e 48.

Tem outras funcoes auxiliares a serem definidas. Ou seja, essas especificacoes sao para o funcionamento geral do GO-BACK-N

CLIENT/SENDER
3 funcoes irao ditar o funcionamento do sender, que sao:

rdt_send(): Funcao que vai ficar responsavel por validar e criar os pacotes para o servidor/receiver e vai ativar o timer

timer(): Funcao que vai ser ativada pelo sender para enviar os pacotes criados. Se por um acaso ocorrer timeout, deve retornar essa informacao para o sender.

rdt_rcv(): Funcao vai receber os pacotes do servidor/receiver, se nao tiverem erro e os vai validar. Vai pegar o numero atrelado a esse ack, e vai verificar se houve ou nao perda no envio dos pacotes. Se houver, reenvia todos a partir desse que nao chegou. Senao, continua execucao e desloca a janela.


SERVER/RECEIVER

rdt_rcv(): Funcao que vai receber o pacote, verificar se nao tem erro e verificar se o sequence number eh valido. Se tudo estiver OK, vai montar o pacote ACK, com o numero do pacote que recebeu e o numero do pacote que espera. Envia esse pacote para o SENDER.


__________________________________________________________________________________________
RElatório:

Teleinformática e redes 2 


Implementação do Servidor



	A implementação do servidor consistiu em adapatar o exemplo dado pelo professor para atender os requistios pedidos.
	Primeiramente foram  criadas 3 ( três ) listas que irão salvar as partes da mensagem que for recebida, o index recebido da mensagem e a ultima lista é gerada a partir das respostas que o servidor está enviado para o cliente.
	É verificado se o index recebido não está presente na lista de index para saber se não é apenas o cliente forçando o servidor a reenviar o index caso o ack não tenha chegado a ele. O ack é gerado pela função “create_respost”.
	Essa resposta é gerada com a funçaõ “create_repost” que possui como parametros a mensagem completa que foi enviada pelo servidor e a validade dela que é gerada pela funçaõ de validae. A função concatena o index recebido com um espaço ‘ ’ e mais um bit de validade para inforamar se houve erro no envio da mensagem, isto é, se caso ela tenha chegado com um valor inválido, diferente do que deveria ser.
	É enviado ao cliente o ack , quando o servidor receber uma mensagem e na flag dela estiver 0, indicará que é a ultima mensagem do cliente para o servidor, com isso o servidor faz uma verificação na lista de index recebido para conferir que todos tenham sidos recebidos e imprime na tela a mensagem que foi recebida, isto é, o que cada pacote possuia.
