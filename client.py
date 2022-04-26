import socket

HOST = '127.0.0.1'
PORT = 50000

# Objeto 's' que é um socket
# O método socket.socket recebe a família de endereço e o tipo
# Família: "AF_INET" utiliza ipv4
# Tipo: "SOCKE_STREAM" utiliza protocolo TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Pedido para se conectar ao servidor
# O método connect recebe apenas um parâmetro mas que está dividido em duas partes
s.connect((HOST,PORT))

# Enviar dados
# "str.encode" Garante que vai enviar em formato de string para o servidor
s.sendall(str.encode('Hello world!'))

# Tamanho máximo dos dados que queremos receber
data = s.recv(1024)

# Exibir a mensagem que o servidor retornou.
print('Mensagem ecoada!:',data.decode())