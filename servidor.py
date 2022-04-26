import socket

HOST = 'localhost'
PORT = 50000


# Objeto 's' que é um socket
# O método socket.socket recebe a família de endereço e o tipo
# Família: "AF_INET" utiliza ipv4
# Tipo: "SOCKE_STREAM" utiliza protocolo TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o host e porta ao socket
# O método bind recebe apenas um parâmetro mas que está dividido em duas partes
s.bind((HOST,PORT))

# Escuta pedidos de conexão de clientes
s.listen()
print('Aguardando conexão de um cliente')

# Aceitar o pedido de conexão do cliente
conn, ender = s.accept()
print('Conectado em', ender)

while True:

    # Tamanho máximo dos dados que queremos receber
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    # Enviando novamento os dados para o cliente.
    conn.sendall(data)
