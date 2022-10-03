from socket import *
from threading import Thread

serverPort = 12000

def serve(idx):
    print(f"The server {idx} is ready to receive")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        print("Server", idx, ":", message.decode(), "->", modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    threads = []
    for i in range(5):
        serve_thread = Thread(target=serve, args=[i])
        serve_thread.start()
        threads.append(serve_thread)
    
    # Wait until all finished
    for t in threads:
        t.join()

