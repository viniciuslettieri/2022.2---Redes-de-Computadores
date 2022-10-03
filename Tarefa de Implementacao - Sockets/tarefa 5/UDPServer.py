from socket import *
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    request = json.loads(message.decode())

    if request.get("username") == "username" and request.get("password") == "password":
        serverSocket.sendto(("200 - Success").encode(), clientAddress)
    else:
        serverSocket.sendto(("401 - Unauthorized").encode(), clientAddress)
    
