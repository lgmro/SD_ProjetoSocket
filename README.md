# Projeto Socket Cliente-Servidor

## Integrantes:
#### Adilson Lucas Nogueira Almeida - RA: 1272117609;
#### Gustavo Rafael Vieira Goes - RA: 1272117750;
#### Lucas Gabriel Maciel Marinho - RA: 1272115763;
#### Lucas Nery Moreno - RA: 1272121356;
#### Marina Fernandes Porto Leite - RA: 1272121593;

## Requisitos para instalação:
#### É necessário ter o Python 3 instalado. Testamos nas versões 3.10.6 e 3.11.0;
    Para instalar o python de acordo com seu SO acesse: https://www.python.org/downloads/
#### Caso você queira visualizar melhor o código, será necessário uma IDE, recomendamos usar Visual Studio Code;
    Para instalar o VSCode acesse: https://code.visualstudio.com/
#### Você pode usar um terminal para execucar a aplicação. Ex.: CMD, PowerShell, Shell;
#### Para o sistema operacional, pode-se usar o macOs, windows ou sistemas linux. Testamos no windows e no ubuntu.


## Instrução para instalação:
#### 1 - Baixe a pasta do projeto pelo GitHub ou clone o projeto com o git clone. A versão mais atualizada está disponível na branch main;
#### 2 - Caso você for usar a mesma máquina para executar os três códigos-fonte, não precisa realizar nenhuma alteração HOST(IP). Caso for máquinas diferente, substitua a string "localhost" dos códigos-fontes para o IP apropriado da máquina que você irá usar, lembre-se que os IP's dos clientes devem ser o mesmo do servidor;
    Alguns comando que você pode usar para descobrir seu ip: ipconfig (Windows) e ifconfig(Ubuntu).
#### 3 - Executando a aplicação na mesma máquina, você só precisar abrir três terminais na pasta do projeto onde está localizado os códigos fontes (esse detalhe é importate) e execute o código-fonte do "server.py" em um dos terminais primeiro. Segue abaixo alguns comandos que utilizamos, mas aconselhamos pesquisar o qual a sua máquina utiliza: 
    python servidor.py (Windows), py servidor.py (Windows) ou python3 servidor.py (Ubuntu);
#### 4 - Execute os clientes vendedor e gerente, seguindo o exemplo que você utilizou para executar o servidor, substituindo o nome do arquivo para o desejado. 
    Exemplos cliente vendedor:  python cliente_vendedor.py (Windows), py cliente_vendedor.py (Windows) ou python3 cliente_vendedor.py (Ubuntu);
    Exemplos cliente gerente: python cliente_gerente.py (Windows), py cliente_gerente.py (Windows) ou python3 cliente_gerente.py (Ubuntu);
    
#### 5 - Você verá que o terminal do servidor irá informar cada vez que um cliente se conectar, além do próprio cliente informar se ele conseguiu se conectar ou não.
#### 6 - Agora você tem as aplicações funcionando, pode executar as operações no cliente do vendedor e do gerente.
