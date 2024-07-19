import socket
from questao4_handler import float_para_ieee754

def client(client_socket):
  numero_str = client_socket.recv(1024).decode('utf-8')
  bits, representacao_hex = float_para_ieee754(numero_str)
  
  resposta = f'A representação do número {numero_str} no padrão IEEE-754 é:\nEm binário: {bits}\nEm hexadecimal: {representacao_hex}'
  client_socket.send(resposta.encode('utf-8'))
  client_socket.close()
  
def iniciar_servidor():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('0.0.0.0', 9999))
  server.listen(5)
  print('Servidor iniciado na porta 9999')
  
  while True:
    client_socket, addr = server.accept()
    client(client_socket)

if __name__ == "__main__":
  iniciar_servidor()