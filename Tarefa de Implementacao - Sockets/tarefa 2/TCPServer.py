from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    
    print("Connection Accepted", addr)
    while True:
        message = connectionSocket.recv(1024)
        
        if not message: 
            break

        modifiedMessage = message.decode().upper()
        print(message.decode(), "->", modifiedMessage)
        connectionSocket.send(modifiedMessage.encode())

    print("Connection was Closed", addr)
    connectionSocket.close()

serverSocket.close()