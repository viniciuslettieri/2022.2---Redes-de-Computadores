import json

def constroi_mensagem(string_msg, state):
    byte_msg = json.dumps({'msg': string_msg, 'state': state}).encode()
    msg = len(byte_msg).to_bytes(2, 'big')
    msg += byte_msg
    return msg

def reconstroi_mensagem(socket):
    msg = socket.recv(2)

    if not msg:
        return None
    
    length = int.from_bytes(msg[:2], 'big')
    full_msg = socket.recv(length)
    return json.loads(full_msg.decode())