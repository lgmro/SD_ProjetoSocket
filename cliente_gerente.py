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

	startCliente(cliente)

def startCliente(cliente):
	threadVendedor = threading.Thread(target=enviarEscolhaOperação, args=[cliente])
	threadVendedor.start()

def enviarEscolhaOperação(cliente):
	print("\nInforme o código da operação: ")
	mensagem = input("\nCódigo > ")
	cliente.sendall(mensagem.encode("utf-8"))
	resposta = cliente.recv(1024).decode("utf-8")
    
    # TODO: Verifica qual informação deve solicitar ao usuário