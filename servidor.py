import socket
import threading
import datetime

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
        print("\n Não foi possível iniciar o servidor")

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
        operacoesVendedor(cliente)
        print(f"Cliente: {cliente} é um vendedor. Sua thread é: {threading.enumerate()}")
    elif tipoCliente == "Gerente":
        operacoesGerente(cliente)
        print(f"Cliente: {cliente} é um gerente. Sua thread é: {threading.enumerate()}")
    else:
        print("Cliente não é um vendedor ou gerente.")
    
def operacoesVendedor(cliente):
    global vendasRealizadas
    codigoOperacao = cliente.recv(1024).decode("utf-8")
    if codigoOperacao == "OP001":
        cliente.sendall("OK_OP".encode("utf-8"))
        print(f"Cliente: {cliente} escolheu OP001.") 
        try:
            nomeVendedor = cliente.recv(2048).decode("utf-8")
            idLoja = cliente.recv(2048).decode("utf-8")
            dataVenda = cliente.recv(2048).decode("utf-8")
            formatarEmData = datetime.date(int(dataVenda[6:10]),int(dataVenda[3:5]),int(dataVenda[0:2]))
            cliente.sendall("OK".encode("utf-8"))

            valorVenda = float(cliente.recv(2048).decode("utf-8"))
            cliente.sendall("OK".encode("utf-8"))

            vendasRealizadas.append(Venda(nomeVendedor, idLoja, formatarEmData, valorVenda))

            for vendas in vendasRealizadas:
                print(vendas.valoresObj())
            iniciarVendedorOuGerente("Vendedor", cliente)
        except:
            print("Erro. Tente novamente")
            cliente.sendall("Erro".encode("utf-8"))
            iniciarVendedorOuGerente("Vendedor", cliente)
    else:
        cliente.sendall("ERRO_OP".encode("utf-8"))
        print("Esse código de operação não existe ou você não tem acesso ao mesmo. Tente outro por favor...")
        iniciarVendedorOuGerente("Vendedor", cliente)

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
    cliente.sendall("OK_OP".encode("utf-8"))
    pass

def totalVendasLoja(cliente):
    cliente.sendall("OK_OP".encode("utf-8"))
    pass

def totalVendasLojaPeriodo(cliente):
    cliente.sendall("OK_OP".encode("utf-8"))
    pass

def melhorVendedor(cliente):
    cliente.sendall("OK_OP".encode("utf-8"))
    pass

def melhorLoja(cliente):
    cliente.sendall("OK_OP".encode("utf-8"))
    pass

main()