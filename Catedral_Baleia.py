print('Cadastro de Igrejas do Campo da Catedral Baleia CONAMAD!')
id = int(input('Digite o ID da Igreja: '))
regiao = input('Qual é a região da área da igreja? ')
endereco = input('Digite o endereço e a cidade da sua igreja: ')
nome = input('Qual é o nome da igreja? ')
pastor = input('Qual é o Pastor(a) da igreja? ')

import sqlite3

conexao = sqlite3.connect('baleia.db')
cursor = conexao.cursor()
#cursor.execute("CREATE TABLE Catedral_Baleia (id integer, Regiao varchar(250), Endereco varchar(250), Nome varchar(25), Pastor varchar(25))")
sql = ('INSERT INTO Catedral_Baleia (id, regiao, endereco, nome, pastor) VALUES (?, ?, ?, ?, ?)')
valores = [id, regiao, endereco, nome, pastor]

cursor.execute(sql, valores)
conexao.commit()
print('Dados inseridos com sucesso!')
conexao.close
