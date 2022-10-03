from socket import *
from threading import Thread

serverPort = 12000

def serve(idx, serverSocket):
    print(f"The server {idx} is ready to receive")

    while True:
        connectionSocket, addr = serverSocket.accept()
        
        print(f"Server {idx} Connection Accepted", addr)
        while True:
            message = connectionSocket.recv(1024)
            
            if not message: 
                break

            modifiedMessage = message.decode().upper()
            print(message.decode(), "->", modifiedMessage)
            connectionSocket.send(modifiedMessage.encode())

        print(f"Server {idx} Connection was Closed", addr)
        connectionSocket.close()

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(3)

    threads = []
    for i in range(5):
        serve_thread = Thread(target=serve, args=[i, serverSocket])
        serve_thread.start()
        threads.append(serve_thread)
    
    # Wait until all finished
    for t in threads:
        t.join()

    serverSocket.close()
