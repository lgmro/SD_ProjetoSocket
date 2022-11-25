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
#### 3 - Executando a aplicação na mesma máquina, você só precisar abrir três terminais na pasta do projeto onde está localizado os códigos fontes (esse detalhe é importate) e execute o código-fonte do "servidor.py" em um dos terminais primeiro. Segue abaixo alguns comandos que utilizamos, mas aconselhamos pesquisar o qual a sua máquina utiliza: 
    python servidor.py (Windows), py servidor.py (Windows) ou python3 servidor.py (Ubuntu);
#### 4 - Execute os clientes vendedor e gerente, seguindo o exemplo que você utilizou para executar o servidor, substituindo o nome do arquivo para o desejado. 
    Exemplos cliente vendedor:  python cliente_vendedor.py (Windows), py cliente_vendedor.py (Windows) ou python3 cliente_vendedor.py (Ubuntu);
    Exemplos cliente gerente: python cliente_gerente.py (Windows), py cliente_gerente.py (Windows) ou python3 cliente_gerente.py (Ubuntu);
    
#### 5 - Você verá que o terminal do servidor irá informar cada vez que um cliente se conectar, além do próprio cliente informar se ele conseguiu se conectar ou não.
#### 6 - Agora você tem as aplicações funcionando, pode executar as operações no cliente do vendedor e do gerente. 

#### Importante: Nosso sistema é Case-sensitive, isto é, o aplicativo distingue letras maiúsculas de minúsculas. Ex.: A palavra "Maria" é diferente da palavra "maria".

## Tutorial de uso das aplicações:
#### 1 - Vamos executar o servidor.py; 

<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203658772-d4cf5858-ca88-4b54-9033-680f1b346cdd.png" width = "800px"/>
</div>

#### 2 - Agora vamos executar o cliente_vendedor.py e o cliente_gerente.py. Você verá que o servidor irá informa que os clientes foram conectados;
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203659355-013d1611-cf3a-41fb-ab17-fd219bb4e323.png" width = "800px"/>
</div>

#### 3 - O vendedor pode cadastrar uma compra escrevendo o código da operação "OP001" e encerrar a aplicação escrevendo "FIM" no código. Vamos cadastrar uma venda na aplicação do vendedor:
    3.1 - Informe o código "OP001";
    3.2 - Informe o nome do vendedor. Ex: Maria;
    3.3 - Informe o ID da loja. Ex: LOJA55;
    3.4 - Informe a data da venda. Ex: 05/11/2022 (Use esse padrão (DD/MM/AAAA), lembre-se de usar as barras);
    3.5 - Informe o valor da venda. Ex: 1000.50 (Para informar decimais, não use vírgula (,) use o ponto (.);
    3.6 - Você verá uma mensagem informando que a venda foi cadastrada. Perceba que a aplicação do servidor mostra os dados da venda cadastrada;
    3.7 - Caso queira cadastrar outra venda, é só repetir os mesmos passos.
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203659719-008ea609-1b6a-44f5-a283-761e77818172.png" width = "800px"/>
</div>

#### 4 - Vamos verificar as ações do gerente. Por gentileza, efetue mais do que um cadastro de venda na aplicação, para se ter uma melhor consulta. O gerente pode executar 6 operações, que são:
4.1 - OP002: Faz uma consulta e retorna o total de vendas de um vendedor, através de um nome informado. No nosso exemplo pesquisamos por Maria, ela efetuou 2 vendas com um somatório de vendas de R$ 1201.00:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203663111-0ababc60-1a64-4365-8727-7faf812da825.png" width = "800px"/>
</div>
4.2 - OP003: Faz uma consulta e retorna o total de vendas de uma loja, através do ID de loja informado. No nosso exemplo pesquisamos por "LOJA90", que nos informa que a loja efetuou 2 vendas com um somatório das vendas de R$ 1800.50:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203663474-1a4c0752-daef-47cc-a875-8ded71f721b5.png" width = "800px"/>
</div>
4.3 - OP004: Faz uma consulta e retorna o total de vendas da rede lojas  cadastradas na aplicação dentro de um período informado. Precisa informar a data inicial  e a data final. No exemplo solicitamos uma consulta para data inicial: 09/11/2022 e data final: 20/11/2022. No nosso exemplo, a aplicação informa que nesse período teve 2 vendas com um somatório de R$ 1800.50:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203663471-b06c1e7c-df87-47a1-960f-f4987a14e16f.png" width = "800px"/>
</div>
4.5 - OP005: Faz uma consulta e informar o nome do vendedor que mais vendeu (aquele que tem o maior valor acumulado de vendas) entre as vendas cadastradas. Nosso exemplo foi a Maria com total acumulado de R$ 1201.00:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203663470-515c082a-17f8-4eeb-bfc3-b7d0ef178b31.png" width = "800px"/>
</div>
4.6 - OP006: Faz uma consulta e informar o ID da loja que mais vendeu (aquela que tem o maior valor acumulado de vendas) entre as vendas cadastradas. Nosso exemplo foi a LOJA90 com um total acumulado de R$ 1800.50:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203663468-f4184619-0353-4332-96f9-00e34452a531.png" width = "800px"/>
</div>
4.7 - FIM: Finaliza a aplicação do gerente:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203665349-1922aaaa-943c-46aa-9543-524ce33ba067.png" width = "800px"/>
</div>

#### Obs.: Para finalizar o servidor, você pode usar o comando "CTRL + C". Lembre-se de finalizar o cliente do vendedor e do gerente primeiro.

