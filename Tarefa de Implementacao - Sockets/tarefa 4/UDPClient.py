from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

N = 10000
for numero in range(N):
    clientSocket.sendto(str(numero).encode(), (serverName, serverPort))

clientSocket.close()