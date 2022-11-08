import socket
import threading
import datetime
import pickle

vendasRealizadas = []
clientes = []

class Venda():
    def __init__(self, nomeVendedor, idLoja, dataVenda, valorVenda):
        self.nomeVendedor = nomeVendedor
        self.idLoja = idLoja
        self.dataVenda = dataVenda
        self.valorVenda = valorVenda

    def __str__(self):
        return "[Nome: " + self.nomeVendedor + " | Loja: " + self.idLoja + " | Data: " + str(self.dataVenda) + " | Valor: " + str(self.valorVenda) + "]"

def main():
    print("\nIniciando servidor.")

    HOST = "localhost"
    PORT = 9000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print("\nServidor esperando conexões.")
    except:
        print("\n Não foi possível iniciar o servidor.")

    while True:
        cliente, enderecoCliente = servidor.accept()
        clientes.append(cliente)
        tipoCliente = cliente.recv(1024).decode("utf-8")
        print(f"Quantidade de clientes conectados nesse servidor: {len(clientes)}.")
        threadVendedor = threading.Thread(target=iniciarVendedorOuGerente, args=[tipoCliente, cliente, enderecoCliente])
        threadVendedor.start()

def iniciarVendedorOuGerente(tipoCliente, cliente, enderecoCliente):
    if tipoCliente == "Vendedor":
        cliente.sendall("OK".encode("utf-8"))
        print(f"\nCliente: {enderecoCliente} é um vendedor.")
        operacoesVendedor(cliente, enderecoCliente)
    elif tipoCliente == "Gerente":
        cliente.sendall("OK".encode("utf-8"))
        print(f"\nCliente: {enderecoCliente} é um gerente.")
        operacoesGerente(cliente, enderecoCliente) 
    else:
        cliente.sendall("ERRO_IDENTIFICACAO".encode("utf-8"))
        print("\nCliente não é um vendedor ou gerente.")
    
def operacoesVendedor(cliente, enderecoCliente):
    global vendasRealizadas
    global clientes
    try:
        codigoOperacao = cliente.recv(1024).decode("utf-8")
        if codigoOperacao == "OP001":
            print(f"Cliente vendedor: {enderecoCliente} escolheu OP001.") 
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
                    print(vendas)

                operacoesVendedor(cliente, enderecoCliente)
            except:
                print("Erro. Tente novamente")
                cliente.sendall("ERRO_DADOS".encode("utf-8"))
                operacoesVendedor(cliente, enderecoCliente)
        else:
            cliente.sendall("ERRO_OP".encode("utf-8"))
            print("Esse código de operação não existe ou você não tem acesso ao mesmo. Tente novamente por favor...")
            operacoesVendedor(cliente, enderecoCliente)
    except:
        print(f"\nCliente vendedor: {enderecoCliente} desconectou.")
        deleteCliente(cliente)
        print(f"Quantidade de clientes conectados nesse servidor: {len(clientes)}.")
        return

def operacoesGerente(cliente, enderecoCliente):
    global clientes
    try:
        codigoOperacao = cliente.recv(1024).decode("utf-8")
        if codigoOperacao == "OP002":
            print(f"Cliente gerente: {enderecoCliente} escolheu OP002.") 
            totalVendasVendedor(cliente)
        elif codigoOperacao == "OP003":
            print(f"Cliente gerente: {enderecoCliente} escolheu OP003.") 
            totalVendasLoja(cliente, enderecoCliente)
        elif codigoOperacao == "OP004":
            print(f"Cliente gerente: {enderecoCliente} escolheu OP004.") 
            totalVendasLojaPeriodo(cliente, enderecoCliente)
        elif codigoOperacao == "OP005":
            print(f"Cliente gerente: {enderecoCliente} escolheu OP005.") 
            melhorVendedor(cliente, enderecoCliente)
        elif codigoOperacao == "OP006":
            print(f"Cliente gerente: {enderecoCliente} escolheu OP006.") 
            melhorLoja(cliente)
        else:
            cliente.sendall("ERRO_OP".encode("utf-8"))
            print("Esse código de operação não existe ou você não tem acesso ao mesmo. Tente outro por favor...")
            operacoesGerente(cliente, enderecoCliente)
    except:
        print(f"\nCliente gerente: {enderecoCliente} desconectou.")
        deleteCliente(cliente)
        print(f"Quantidade de clientes conectados nesse servidor: {len(clientes)}.")
        return

def totalVendasVendedor(cliente):
    pass

def totalVendasLoja(cliente, enderecoCliente):
    global vendasRealizadas
    try:
        cliente.sendall("OK_OP".encode("utf-8"))
        idLoja = cliente.recv(2048).decode("utf-8")

        somaTotalValor = 0
        contarVendas = 0

        listaLojaFiltrada = list(filter(lambda vendas: vendas if vendas.idLoja == idLoja else None, vendasRealizadas))

        for vendas in listaLojaFiltrada:
            somaTotalValor += vendas.valorVenda

        contarVendas = len(listaLojaFiltrada)

        print("\n Lista filtrada: ")
        for vendas in listaLojaFiltrada:
            print(vendas)

        if somaTotalValor == 0 and contarVendas == 0:
            print("\n Não existe loja com esse ID ou vendas cadastradas para a mesma.")
            cliente.sendall(f"--> Não existe loja com esse ID ou vendas cadastradas para a mesma.".encode("utf-8"))
            operacoesGerente(cliente, enderecoCliente)
            return

        print(f"Soma: {somaTotalValor}, Total Vendas: {contarVendas}")
        cliente.sendall(f"--> O valor total de vendas da loja [{idLoja}] foi: R$ {somaTotalValor} e o total de vendas realizadas por ela foi: {contarVendas}.".encode("utf-8"))
        operacoesGerente(cliente, enderecoCliente)
    except:
        cliente.sendall("ERRO".encode("utf-8"))
        print(f"ERRO. Erro na operação.")
        operacoesGerente(cliente, enderecoCliente)

def totalVendasLojaPeriodo(cliente, enderecoCliente):
    global vendasRealizadas
    try:
        cliente.sendall("OK_OP".encode("utf-8"))
        resposta = cliente.recv(2048)

        loadPeriodo = pickle.loads(resposta)
        idLoja = loadPeriodo["idLoja"]
        dataInicial = datetime.date(int(loadPeriodo["dataInicial"][6:10]),int(loadPeriodo["dataInicial"][3:5]),int(loadPeriodo["dataInicial"][0:2]))
        dataFinal = datetime.date(int(loadPeriodo["dataFinal"][6:10]),int(loadPeriodo["dataFinal"][3:5]),int(loadPeriodo["dataFinal"][0:2]))

        somaTotalValor = 0
        contarVendas = 0

        listaLojaFiltrada = list(filter(lambda vendas: vendas if vendas.idLoja == idLoja and vendas.dataVenda >= dataInicial and vendas.dataVenda <= dataFinal else None, vendasRealizadas))

        for vendas in listaLojaFiltrada:
            somaTotalValor += vendas.valorVenda

        contarVendas = len(listaLojaFiltrada)

        print("\n Lista filtrada: ")
        for vendas in listaLojaFiltrada:
            print(vendas)

        if somaTotalValor == 0 and contarVendas == 0:
            print("\n Não existe loja com esse ID ou vendas cadastradas para a mesma nesse período.")
            cliente.sendall(f"--> Não existe loja com esse ID ou vendas cadastradas para a mesma nesse período.".encode("utf-8"))
            operacoesGerente(cliente, enderecoCliente)
            return

        print(f"Soma: {somaTotalValor}, Total Vendas: {contarVendas}")
        cliente.sendall(f"--> O valor total de vendas da loja nesse período foi: R$ {somaTotalValor} e o total de vendas realizadas foi: {contarVendas}.".encode("utf-8"))
        operacoesGerente(cliente, enderecoCliente)
    except:
        cliente.sendall("ERRO".encode("utf-8"))
        print(f"ERRO. Erro na operação.")
        operacoesGerente(cliente, enderecoCliente)

def melhorVendedor(cliente, enderecoCliente):
    global vendasRealizadas
    try:
        vendedores = {}
        for vendas in vendasRealizadas:
            vendedor = vendas.nomeVendedor
            somaVendedor = 0
            for vend in vendasRealizadas:
                if vend.nomeVendedor == vendedor:
                    somaVendedor += vend.valorVenda

            vendedores[vendedor] = somaVendedor
            somaVendedor = 0

        print(vendedores)
        maiorValor = max(vendedores.values())
        melhoresVendedores = []
        for vend, valor in vendedores.items():
            if valor == maiorValor:
                melhoresVendedores.append(vend)

        print(f"Melhor Vendedor(a): {melhoresVendedores} | Valor acumulado: {maiorValor}")

        if len(melhoresVendedores) > 1:
            cliente.sendall(f"--> Tivemos empate. Os melhores vendedores foram: {melhoresVendedores} e o valor total das vendas realizadas por cada um foi: R$ {maiorValor}.".encode("utf-8"))
            operacoesGerente(cliente, enderecoCliente)
        else:
            cliente.sendall(f"--> O(A) melhor vendedor(a) foi: {melhoresVendedores[0]} e o valor total das vendas realizadas foi: R$ {maiorValor}.".encode("utf-8"))
    except Exception as e:
        cliente.sendall("ERRO".encode("utf-8"))
        print(f"ERRO. Erro na operação. {e}")
        operacoesGerente(cliente, enderecoCliente)

def melhorLoja(cliente, enderecoCliente):
    pass

def deleteCliente(cliente):
    clientes.remove(cliente)

main()