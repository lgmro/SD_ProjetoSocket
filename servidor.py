import socket
import threading
import datetime
import pickle

vendasRealizadas = []

class Venda():
    def __init__(self, nomeVendedor, idLoja, dataVenda, valorVenda):
        self.nomeVendedor = nomeVendedor
        self.idLoja = idLoja
        self.dataVenda = dataVenda
        self.valorVenda = valorVenda

    def valoresObj(self):
        return self.nomeVendedor + " " + self.idLoja + " " + str(self.dataVenda) + " " + str(self.valorVenda)

def main():
    print("\nIniciando servidor.")

    HOST = "localhost"
    PORT = 9000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print("\nServidor iniciado.")
    except:
        print("\n Não foi possível iniciar o servidor.")

    i = 0
    while True:
        i += 1
        cliente, enderecoCliente = servidor.accept()
        tipoCliente = cliente.recv(1024).decode("utf-8")
        print(f"Quantidade de clientes que já se conectou nesse servidor: {i}.")
        threadVendedor = threading.Thread(target=iniciarVendedorOuGerente, args=[tipoCliente, cliente])
        threadVendedor.start()

def iniciarVendedorOuGerente(tipoCliente, cliente):
    if tipoCliente == "Vendedor":
        cliente.sendall("OK".encode("utf-8"))
        print(f"\nCliente: {cliente} é um vendedor. Sua thread é: {threading.enumerate()}")
        operacoesVendedor(cliente)
    elif tipoCliente == "Gerente":
        cliente.sendall("OK".encode("utf-8"))
        print(f"\nCliente: {cliente} é um gerente. Sua thread é: {threading.enumerate()}")
        operacoesGerente(cliente) 
    else:
        cliente.sendall("ERRO_IDENTIFICACAO".encode("utf-8"))
        print("\nCliente não é um vendedor ou gerente.")
    
def operacoesVendedor(cliente):
    global vendasRealizadas
    codigoOperacao = cliente.recv(1024).decode("utf-8")
    if codigoOperacao == "OP001":
        print(f"Cliente: {cliente} escolheu OP001.") 
        cliente.sendall("OK_OP".encode("utf-8"))
        try:
            respostaVenda = cliente.recv(4096)
            loadResposta = pickle.loads(respostaVenda)
            nomeVendedor = loadResposta["nomeVendedor"]
            idLoja = loadResposta["idLoja"]
            dataVenda = loadResposta["dataOperacao"]
            formatarEmData = datetime.date(int(dataVenda[6:10]),int(dataVenda[3:5]),int(dataVenda[0:2]))
            valorVenda = float(loadResposta["valorVenda"])

            vendasRealizadas.append(Venda(nomeVendedor, idLoja, formatarEmData, valorVenda))
            cliente.sendall("OK".encode("utf-8"))

            print(f"Inclusão de venda efetuada.") 
            for vendas in vendasRealizadas:
                print(vendas.valoresObj())

            operacoesVendedor(cliente)
        except:
            print("Erro. Tente novamente")
            cliente.sendall("ERRO_DADOS".encode("utf-8"))
            operacoesVendedor(cliente)
    else:
        cliente.sendall("ERRO_OP".encode("utf-8"))
        print("Esse código de operação não existe ou você não tem acesso ao mesmo. Tente novamente por favor...")
        operacoesVendedor(cliente)

def operacoesGerente(cliente):
    codigoOperacao = cliente.recv(1024).decode("utf-8")
    if codigoOperacao == "OP002":
        totalVendasVendedor(cliente)
    elif codigoOperacao == "OP003":
        totalVendasLoja(cliente)
    elif codigoOperacao == "OP004":
        totalVendasLojaPeriodo(cliente)
    elif codigoOperacao == "OP005":
        melhorVendedor(cliente)
    elif codigoOperacao == "OP006":
        melhorLoja(cliente)
    else:
        cliente.sendall("ERRO_OP".encode("utf-8"))
        print("Esse código de operação não existe ou você não tem acesso ao mesmo. Tente outro por favor...")
        iniciarVendedorOuGerente("Gerente", cliente)

def totalVendasVendedor(cliente):
    pass

def totalVendasLoja(cliente):
    pass

def totalVendasLojaPeriodo(cliente):
    cliente.sendall("OK_OP".encode("utf-8"))
    try:
        resposta = cliente.recv(2048)
        loadPeriodo = pickle.loads(resposta)
        idLoja = loadPeriodo["idLoja"]
        dataInicial = datetime.date(int(loadPeriodo["dataInicial"][6:10]),int(loadPeriodo["dataInicial"][3:5]),int(loadPeriodo["dataInicial"][0:2]))
        dataFinal = datetime.date(int(loadPeriodo["dataFinal"][6:10]),int(loadPeriodo["dataFinal"][3:5]),int(loadPeriodo["dataFinal"][0:2]))
        somaTotalValor = 0
        contarVendas = 0
        for vendas in vendasRealizadas:
            if(vendas.idLoja == idLoja):
                if(vendas.dataVenda >= dataInicial and vendas.dataVenda <= dataFinal):
                    somaTotalValor += vendas.valorVenda
                    contarVendas += 1

        print(f"Soma: {somaTotalValor}, Total Vendas: {contarVendas}")
        cliente.sendall(f"O valor total de vendas da loja nesse período foi: {somaTotalValor} e o total vendas realizadas foi: {contarVendas}".encode("utf-8"))
    except:
        cliente.sendall("ERRO".encode("utf-8"))
        print(f"ERRO. Erro na operação.")

def melhorVendedor(cliente):
    pass

def melhorLoja(cliente):
    pass

main()