from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    
    while True:
        message = connectionSocket.recv(1024)
        
        if not message: 
            break

        print(message.decode())

    connectionSocket.close()

serverSocket.close()