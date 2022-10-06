from socket import *

serverName = 'localhost'
serverPort = 12000

# CASO NAO PERSISTENTE

N = 100
for numero in range(N):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(str(numero).encode())
    clientSocket.close()