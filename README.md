# crudTrabalhoAvaliativo

Trabalho Avaliativo Desenvolvimento Web e Banco de Dados M32

1. Criamos um ambiente virtual :

--> Para instalar nos computadores dos integrantes do grupo abrimos o terminal e criamos um ambiente virtual com os comandos : 'python -m venv venv ' 
--> Logo em seguida, para ativar o ambiente digitamos no windowns 'venv/Scripts/activate' e para os que usam Linux: " source venv/bin/activate" ;

2. Instalar a biblioteca :

--> Depois de aberto o ambiente virtual digitamos no terminal 'pip install sqlalchemy' e pronto.

3. Importar funções e classes da biblioteca :

--> Após  instalar a biblioteca importamos ela e suas funções - "create_engine,  declarative_base" - e as classes - " Column, Integer, String, Float, Date, ForeignKey, sessionmaker "- para o código usando: 

" from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey " e 
"from sqlalchemy.orm import sessionmaker, declarative_base "



Obs: Nomes de entidade em inglês para padronizar com resto do código.