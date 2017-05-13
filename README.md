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
