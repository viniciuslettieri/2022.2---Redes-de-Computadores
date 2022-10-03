from socket import *
from utils import reconstroi_mensagem, constroi_mensagem

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

msg = input('Inicie uma conversa: ')
message = constroi_mensagem(msg, None)
clientSocket.send(message)

while True:
    response = reconstroi_mensagem(clientSocket)
    if response is None: 
        break

    print(response["msg"])

    if response["state"] >= 0 and response["state"] < 2: 
        msg = input('Escreva sua resposta: ')
        message = constroi_mensagem(msg, None)
        clientSocket.send(message)

clientSocket.close()