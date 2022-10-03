from socket import *
import json

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

username = input('Input username: ')
password = input('Input password: ')
message = {"username": username, "password": password}
clientSocket.sendto(json.dumps(message).encode(), (serverName, serverPort))

response, serverAddress = clientSocket.recvfrom(2048)
print("Response:", response.decode())

clientSocket.close()