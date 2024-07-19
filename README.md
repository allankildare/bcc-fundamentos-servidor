# Servidor Python
**Bacharelado em Ciência da Computação**

Este é um repositório que contém uma implementação simples de um programa utilizando **Python 3** e ***sockets*** para a criação de um cliente e servidor. No qual o cliente pode enviar um número decimal qualquer e receber do servidor este número convertido para o padrão IEEE-754 de precisão simples.

Esta implementação foi criada para avaliação no curso de **Fundamentos de Sistemas da Computação** da Universidade Federal do Rio de Janeiro.

#### Requisitos de instalação
- Python 3

Obs.: este programa foi feito com base na execução em sistemas Unix, como MacOS e distribuições Linux, ainda assim pode ser executado em diferentes versões do Windows.


#### Como executar esse projeto?
##### Passo 1: clonar o projeto
```shell
git clone https://github.com/allankildare/bcc-fundamentos-servidor.git
```

##### Passo 2: acessar o diretório raiz do projeto
```shell
cd ./bcc-fundamentos-servidor
```

##### Passo 3: iniciar o cliente e servidor
Abra dois terminais, ambos rodando na pasta raiz do projeto (siga o passo 2).

Para rodar o servidor:
```shell
python3 ./server.py
```

Para rodar o cliente:
```shell
python3 ./client.py
```

#### Passo 4: inserir um número
No terminal em que o cliente está sendo executado, insira um número decimal qualquer e veja o seu correspondente no padrão IEEE-754 sendo retornado.

