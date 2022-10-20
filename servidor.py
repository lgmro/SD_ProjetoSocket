from http import client
import socket
import threading

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

        if tipoCliente == "Vendedor":
            operacoesVendedor(cliente)
        elif tipoCliente == "Gerente":
            operacoesGerente(cliente)
        else:
            print("Você não tem permissão para se conectar.")
    
def operacoesVendedor(cliente):
    pass

def operacoesGerente(cliente):
    pass

main()