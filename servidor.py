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
    print("\nIniciando servidor")

    HOST = "localhost"
    PORT = 9000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.bind((HOST, PORT))
        servidor.listen()
    except:
        print("\n Não foi possível iniciar o servidor")

    while True:
        cliente, enderecoCliente = servidor.accept()
        tipoCliente = cliente.recv(1024).decode("utf-8")
        print(f"Cliente: {cliente} conectou.")
        iniciarVendedorOuGerente(tipoCliente, cliente)

        
def iniciarVendedorOuGerente(tipoCliente, cliente):
    if tipoCliente == "Vendedor":
        threadVendedor = threading.Thread(target=operacoesVendedor, args=[cliente])
        threadVendedor.start()
        print(f"Cliente: {cliente} é um vendedor.")
    elif tipoCliente == "Gerente":
        operacoesGerente(cliente)
        print(f"Cliente: {cliente} é um gerente.")
    else:
        cliente.sendall("Você não tem permissão para se conectar".encode("utf-08"))
        print("Você não tem permissão para se conectar.")
    
def operacoesVendedor(cliente):
    global vendasRealizadas
    codigoOperacao = cliente.recv(1024).decode("utf-8")
    if codigoOperacao == "OP001":
        print(f"Cliente: {cliente} escolheu OP001.")
        try:
            nomeVendedor = cliente.recv(2048).decode("utf-8")
            idLoja = cliente.recv(2048).decode("utf-8")
            dataVenda = cliente.recv(2048).decode("utf-8")
            formatarEmData = datetime.date(int(dataVenda[6:10]),int(dataVenda[3:5]),int(dataVenda[0:2]))
            valorVenda = float(cliente.recv(2048).decode("utf-8"))

            vendasRealizadas.append(Venda(nomeVendedor, idLoja, formatarEmData, valorVenda))
            cliente.sendall("OK".encode("utf-8"))

            print(vendasRealizadas[0].valoresObj())
            iniciarVendedorOuGerente("Vendedor", cliente)
        except:
            cliente.sendall("Erro".encode("utf-8"))
            print("Erro. Tente novamente")
            iniciarVendedorOuGerente("Vendedor", cliente)
    else:
        cliente.sendall("Esse código de operação não existe ou você não tem acesso ao mesmo".encode("utf-8"))
        print("Esse código de operação não existe ou você não tem acesso ao mesmo. Tente outro por favor...")
        iniciarVendedorOuGerente("Vendedor", cliente)

def operacoesGerente(cliente):
    pass

main()