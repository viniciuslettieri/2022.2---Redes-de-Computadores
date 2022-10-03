from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

N = 100
for numero in range(N):
    clientSocket.send(str(numero).encode())

clientSocket.close()