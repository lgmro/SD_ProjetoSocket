import socket
import threading

def main():
	HOST = 'localhost'    
	PORT = 9000             
	cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		cliente.connect((HOST,PORT))
		print("\nCliente do tipo gerente iniciado.")
	except:
		print("\nNão foi possível se conectar.")

	cliente.sendall("Gerente".encode("utf-8"))
	resposta = cliente.recv(1024).decode("utf-8")

	if resposta == "OK":
		print("\nCliente do tipo vendedor iniciado.")
		startCliente(cliente)
	else:
		print("Algo deu errado. Talvez você não tenha permissão para se conectar.")
		cliente.close()

def startCliente(cliente):
	threadVendedor = threading.Thread(target=enviarConsulta, args=[cliente])
	threadVendedor.start()

def enviarConsulta(cliente):
	print('''
  	=========================================================
  	Operações permitidas para esse usuário:
    
	| Código |               Ação                           |
	|--------|----------------------------------------------|
  	| OP002  |    Consultar total de vendas vendedor        | 
	| OP003  |      Consultar total de vendas loja          | 
	| OP004  |  Consultar total de vendas loja por período  | 
	| OP005  |             Melhor vendedor                  | 
	| OP006  |               Melhor loja                    | 
  	| FIM    |       Encerrar o cliente                     | 
	---------------------------------------------------------
	Obs.: Utilizar letras maiúsculas para os códigos.
  	=========================================================
  	''')
    