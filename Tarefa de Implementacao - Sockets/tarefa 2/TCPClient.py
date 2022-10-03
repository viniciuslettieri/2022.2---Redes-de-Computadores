from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('Input lowercase sentence: ')
while message != 'end':
    clientSocket.send(message.encode())

    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode())

    message = input('Input lowercase sentence: ')

clientSocket.close()