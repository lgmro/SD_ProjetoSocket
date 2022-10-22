import socket
import threading

def main():
	HOST = 'localhost'    
	PORT = 9000             
	cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		cliente.connect((HOST,PORT))
		print("\nCliente do tipo vendedor iniciado.")
	except:
		print("\nNão foi possível se conectar.")

	cliente.sendall("Vendedor".encode("utf-8"))

	startCliente(cliente)

def startCliente(cliente):
	threadVendedor = threading.Thread(target=enviarEscolhaOperação, args=[cliente])
	threadVendedor.start()


def enviarEscolhaOperação(cliente):
	print("\nInforme o código da operação: ")
	mensagem = input("\nCódigo > ")
	cliente.sendall(mensagem.encode("utf-8"))
	resposta = cliente.recv(1024).decode("utf-8")
	if resposta == "OK_OP":
		print("\nVocê escolheu a operação para cadastrar uma venda efetuada.")
		enviarVenda(cliente)
	elif resposta == "ERRO_OP":
		print("\nParece que você não tem permissão para executar essa operação ou informou um código de operação inexistente. Tente novamente")
		enviarEscolhaOperação(cliente)

def enviarVenda(cliente):
	try:
		print("\nInforme o nome do vendedor: ")
		mensagem = input("\nNome > ")
		cliente.sendall(mensagem.encode("utf-8"))

		print("\nInforme o código de id da loja: ")
		mensagem = input("\nId > ")
		cliente.sendall(mensagem.encode("utf-8"))
		
		print("\nInforma a data da operação (Por favor, use o formato DD/MM/AAAA. Ex.: 11/12/2019):")
		mensagemData = input("\nData > ")
		cliente.sendall(mensagemData.encode("utf-8"))
		respostaData = cliente.recv(1024).decode("utf-8")
		if respostaData == "Erro":
			print("\nAlguma coisa deu errado. Talvez você tenha inserido um formato de data errado. Tente novamente")
			enviarEscolhaOperação(cliente)
		else:
			print("\nInforme o valor da operação (Por favor, use somente número, para número decimais use o ponto ao invés da vírgula): ")
			mensagemValor = input("\nValor > ")
			cliente.sendall(mensagemValor.encode("utf-8"))
			respostaOP = cliente.recv(1024).decode("utf-8")
			if respostaOP == "Erro":
				print("\nAlguma coisa deu errado. Talvez você tenha inserido letras no valor da operação. Tente novamente")
				enviarEscolhaOperação(cliente)	
			else:
				if respostaOP == "OK":
					print(respostaOP)
					print("\nOK. Venda cadastrada com sucesso. Vamos fazer outro cadastro? ")
					enviarEscolhaOperação(cliente)
				else:
					print(respostaOP)
					print("\nAlguma coisa deu errado. Tente novamente")
					enviarEscolhaOperação(cliente)
	except:
		print("Erro")
		startCliente(cliente)

main()