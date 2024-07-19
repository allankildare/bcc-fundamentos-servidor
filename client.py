import socket

def iniciar_client():
  print("Olá pessoa usuária!\nSou um programa feito usando socket e Python 3\nque faz a conversão de números decimais em sua representação no padrão IEEE-754\n")
  numero_str = input("Digite aqui o número: ")
  
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(('127.0.0.1', 9999))
  client.send(numero_str.encode('utf-8'))
  
  resposta = client.recv(4096).decode('utf-8')
  print(f'Servidor respondeu:\n{resposta}')
  
  print('\nVisite o Github do autor em:\nhttps://github.com/allankildare')
  
  client.close()

if __name__ == "__main__":
  iniciar_client()