import socket
import threading
import pickle

def main():
	HOST = 'localhost'    
	PORT = 9000             
	cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		cliente.connect((HOST,PORT))
		print("\nCliente do tipo gerente conectado.")
	except:
		print("\nNão foi possível se conectar.")

	cliente.sendall("Gerente".encode("utf-8"))
	resposta = cliente.recv(1024).decode("utf-8")

	if resposta == "OK":
		print("\nCliente do tipo gerente iniciado.")
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
  	| FIM    |           Encerrar o cliente                 | 
	---------------------------------------------------------
	Obs.: Utilizar letras maiúsculas para os códigos.
  	=========================================================
  	''')
	print("\nInforme o código da operação: ")
	operacao = input("\nCódigo > ")

	if operacao == "FIM":
		print("Você escolheu encerrar o cliente.")
		cliente.close()
		return

	if operacao == "OP002":
		solicitarTotalVendasVendedor(cliente)
	elif operacao == "OP003":
		solicitarTotalVendasLoja(cliente)
	elif operacao == "OP004":
		solicitarTotalVendasLojaPeriodo(cliente)
	elif operacao == "OP005":
		solicitarMelhorVendedor(cliente)
	elif operacao == "OP006":
		solicitarMelhorLoja(cliente)
	else:
		print("\nERRO. \nEsse código de operação não existe ou você não tem acesso ao mesmo. Tente novamente por favor...")
		enviarConsulta(cliente)

def solicitarTotalVendasVendedor(cliente):
	try:
		cliente.sendall("OP002".encode("utf-8"))
		respostaServidorOP = cliente.recv(1024).decode("utf-8")
		if respostaServidorOP == "OK_OP":
			print("\nInforme o nome do vendedor para a consulta: ")
			nomeVendedor = input("\nNome vendedor > ")

			cliente.sendall(nomeVendedor.encode("utf-8"))
			respostaServidor = cliente.recv(2048).decode("utf-8")

			if respostaServidor == "ERRO":
				print("\n ERRO. \n Aparetemente não existe vendedor com esse nome. Tente novamente por favor...")
				enviarConsulta(cliente)
			else:
				print(f"\n{respostaServidor}")
				print("\nOK. \nConsulta realizada com sucesso. Vamos fazer outra consulta? ")
				enviarConsulta(cliente)
		else:
			print("\nERRO. \nInesperado. Tente Novamente...")
			enviarConsulta(cliente)
	except:
		print("ERRO. \nTente novamente por favor...")
		enviarConsulta(cliente)

def solicitarTotalVendasLoja(cliente):
	try:
		cliente.sendall("OP003".encode("utf-8"))
		respostaServidorOP = cliente.recv(1024).decode("utf-8")
		if respostaServidorOP == "OK_OP":
			print("\nInforme o ID da loja para a consulta: ")
			idLoja = input("\nID Loja > ")

			cliente.sendall(idLoja.encode("utf-8"))
			respostaServidor = cliente.recv(2048).decode("utf-8")

			if respostaServidor == "ERRO":
				print("\n ERRO. \n Aparetemente não existe loja com esse ID. Tente novamente por favor...")
				enviarConsulta(cliente)
			else:
				print(f"\n{respostaServidor}")
				print("\nOK. \nConsulta realizada com sucesso. Vamos fazer outra consulta? ")
				enviarConsulta(cliente)
		else:
			print("\nERRO. \nInesperado. Tente Novamente...")
			enviarConsulta(cliente)
	except:
		print("ERRO. \nTente novamente por favor...")
		enviarConsulta(cliente)
    
def solicitarTotalVendasLojaPeriodo(cliente):
	try:
		cliente.sendall("OP004".encode("utf-8"))
		respostaServidorOP = cliente.recv(1024).decode("utf-8")

		if respostaServidorOP == "OK_OP":
			print("\nInforme o ID da loja: ")
			idLoja = input("\nID Loja > ")

			print("\nInforme a data inicial do período (Por favor, use o formato DD/MM/AAAA. Ex.: 11/12/2019): ")
			dataInicial = input("\nData Inicial > ")

			print("\nInforme a data final do período (Por favor, use o formato DD/MM/AAAA. Ex.: 11/12/2019):")
			dataFinal = input("\nData Final > ")

			buscarTotalVendas = {
				"idLoja": idLoja,
				"dataInicial": dataInicial,
				"dataFinal": dataFinal
			}

			dados = pickle.dumps(buscarTotalVendas)

			cliente.sendall(dados)

			respostaServidor = cliente.recv(2048).decode("utf-8")

			if respostaServidor == "ERRO":
				print("\n Talvez você tenha inserido um formato de data errado ou inserido letras no valor. Tente novamente por favor...")
				enviarConsulta(cliente)
			else:
				print(f"\n{respostaServidor}")
				print("\nOK. \nConsulta realizada com sucesso. Vamos fazer outra consulta? ")
				enviarConsulta(cliente)

		else:
			print("\nERRO. \nInesperado. Tente Novamente...")
			enviarConsulta(cliente)
	except:
		print("ERRO. \nTente novamente por favor...")
		enviarConsulta(cliente)

def solicitarMelhorVendedor(cliente):
	try:
		cliente.sendall("OP005".encode("utf-8"))
		melhorVendedor = cliente.recv(1024).decode("utf-8")

		if melhorVendedor == "ERRO":
			print("\n ERRO. \n Tente novamente por favor...")
			enviarConsulta(cliente)
		else:
			print(f"\n{melhorVendedor}")
			print("\nOK. \nConsulta realizada com sucesso. Vamos fazer outra consulta? ")
			enviarConsulta(cliente)
	except:
		print("ERRO. \nTente novamente por favor...")
		enviarConsulta(cliente)

def solicitarMelhorLoja(cliente):
	try:
		cliente.sendall("OP006".encode("utf-8"))
		melhorLoja = cliente.recv(1024).decode("utf-8")

		if melhorLoja == "ERRO":
			print("\n ERRO. \n Tente novamente por favor...")
			enviarConsulta(cliente)
		else:
			print(f"\n{melhorLoja}")
			print("\nOK. \nConsulta realizada com sucesso. Vamos fazer outra consulta? ")
			enviarConsulta(cliente)
	except:
		print("ERRO. \nTente novamente por favor...")
		enviarConsulta(cliente)

main()