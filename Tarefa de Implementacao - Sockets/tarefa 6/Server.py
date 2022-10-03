from socket import *
from threading import Thread

from utils import constroi_mensagem, reconstroi_mensagem

serverPort = 12000      

def response_welcome(state_info, connectionSocket):
    reconstroi_mensagem(connectionSocket)
    message = constroi_mensagem("\nOlá! Bem-vindo! Qual o seu nome?", state_info["state"])
    connectionSocket.send(message)
    
    state_info["name"] = reconstroi_mensagem(connectionSocket)["msg"]
    state_info["state"] = 1

def response_services(state_info, connectionSocket):
    message = constroi_mensagem(
    f"""\nCerto, {state_info['name']}! Como posso te ajudar? Digite o numero que corresponde a opção desejada:
    1- Agendar um horário de monitoria
    2- Listar as próximas atividades da disciplina
    3- Email do professor""", state_info["state"]
    )
    connectionSocket.send(message)

    state_info["action"] = reconstroi_mensagem(connectionSocket)["msg"]
    state_info["state"] = 2

def response_actions(state_info, connectionSocket):
    if state_info["action"] == "1":
        message = constroi_mensagem(
        f"""\nPara agendar uma monitoria, basta enviar um email para calinafigueiredo@poli.ufrj.br""", state_info["state"]
        )
        connectionSocket.send(message)

    elif state_info["action"] == "2":
        message = constroi_mensagem(
        f"""\nFique atento para as datas das próximas atividades. Confira o que vem por ai!
        P1: 26 de maio de 2022
        Lista 3: 29 de maio de 2022""", state_info["state"]
        )
        connectionSocket.send(message)

    elif state_info["action"] == "3":
        message = constroi_mensagem(
        f"""\nQuer falar com o professor? O email dele é sadoc@dcc.ufrj.br""", state_info["state"]
        )
        connectionSocket.send(message)
    
    state_info["state"] = 3

def response_finalize(state_info, connectionSocket):
    message = constroi_mensagem(
    f"""\nObrigado por utilizar nossos serviços! Até logo!""", -1
    )
    connectionSocket.send(message)
    print("end")
    
    state_info["state"] = -1

def correct_response(state_info, connectionSocket):
    if state_info["state"] == 0:
        response_welcome(state_info, connectionSocket)
    elif state_info["state"] == 1:
        response_services(state_info, connectionSocket)
    elif state_info["state"] == 2:
        response_actions(state_info, connectionSocket)
    elif state_info["state"] == 3:
        response_finalize(state_info, connectionSocket)

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(3)

    print(f"Waiting for connections")

    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"Server Connection Accepted", addr)

        state_info = {}
        state_info["state"] = 0
            
        while state_info["state"] != -1:
            correct_response(state_info, connectionSocket)

        print(f"Server Connection was Closed", addr)
        connectionSocket.close()

    serverSocket.close()
