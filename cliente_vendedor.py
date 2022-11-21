import socket
import threading
import pickle

def main():
	HOST = 'localhost'    
	PORT = 9000             
	cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		cliente.connect((HOST,PORT))
		print("\nIniciando cliente.")
	except:
		print("\nNão foi possível se conectar.")

	cliente.sendall("Vendedor".encode("utf-8"))
	resposta = cliente.recv(1024).decode("utf-8")

	if resposta == "OK":
		print("\nCliente do tipo vendedor iniciado.")
		startCliente(cliente)
	else:
		print("Algo deu errado. Talvez você não tenha permissão para se conectar.")
		cliente.close()

def startCliente(cliente):
	threadVendedor = threading.Thread(target=enviarVenda, args=[cliente])
	threadVendedor.start()

def enviarVenda(cliente):
	print('''
  	================================================
  	Operações permitidas para esse usuário:
    
	| Código |              Ação                   |
	|--------|-------------------------------------|
  	| OP001  |       Informar uma venda            |
  	| FIM    |       Encerrar o cliente            | 
	------------------------------------------------
	Obs.: Utilizar letras maiúsculas para os códigos.
  	================================================
  	''')
	
	try:
		print("\nInforme o código da operação: ")
		operacao = input("\nCódigo > ")

		if operacao == "FIM":
			print("Você escolheu encerrar o cliente.")
			cliente.close()
			return

		cliente.sendall(operacao.encode("utf-8"))
		respostaServidorOP = cliente.recv(1024).decode("utf-8")
		
		if respostaServidorOP == "OK_OP":
			print("\nInforme o nome do vendedor: ")
			nomeVendedor = input("\nNome > ")

			print("\nInforme o código de id da loja: ")
			idLoja = input("\nId > ")

			print("\nInforma a data da operação (Por favor, use o formato DD/MM/AAAA. Ex.: 11/12/2019):")
			dataOperacao = input("\nData > ")


			print("\nInforme o valor da operação (Por favor, use somente número, para número decimais use o ponto ao invés da vírgula): ")
			valorVenda = input("\nValor > ")
			
			informarVenda = {
				"nomeVendedor": nomeVendedor,
				"idLoja": idLoja,
				"dataOperacao": dataOperacao,
				"valorVenda": valorVenda
			}

			dados = pickle.dumps(informarVenda)

			cliente.sendall(dados)

			respostaServidor = cliente.recv(1024).decode("utf-8")

			if respostaServidor == "OK":
				print("\nOK. Venda cadastrada com sucesso. Vamos fazer outro cadastro? ")
				enviarVenda(cliente)
			elif respostaServidor == "ERRO_DADOS":
				print("\nERRO. Talvez você tenha inserido um formato de data errado ou inserido letras no valor. Tente novamente por favor...")
				enviarVenda(cliente)
			else:
				print("\nERRO. Tente novamente por favor...")
				enviarVenda(cliente)
		
		elif respostaServidorOP == "ERRO_OP":
			print("\nERRO. Esse código de operação não existe ou você não tem acesso ao mesmo. Tente novamente por favor...")
			enviarVenda(cliente)
		else:
			print("\nERRO. Inesperado.... Tente Novamente")
			enviarVenda(cliente)
	except:
		print("ERRO. Tente novamente por favor...")
		enviarVenda(cliente)

main()