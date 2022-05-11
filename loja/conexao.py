
from telnetlib import DO
import mysql.connector
banco = mysql.connector.connect(host='bdapp', user='root', password='root',port=3306)
cursor = banco.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS pets')
cursor.execute('USE pets')
cursor.execute('CREATE TABLE IF NOT EXISTS material(id VARCHAR(50) NOT NULL, nome VARCHAR(50), valor VARCHAR(50),unidade VARCHAR(50))ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;')

#CREATE
def create(id,produto,valor,unidade):
	comando = f'INSERT INTO material(id,nome,valor,unidade) VALUES({id},"{produto}","{valor}","{unidade}")'
	cursor.execute(comando)
	banco.commit()
	
#READ
def read():
	comando = f'SELECT * FROM material'
	cursor.execute(comando)
	resposta = cursor.fetchall()
	for resp in resposta:
		print(resp)
#UPDATE
def update(alterar,id):
	comando = f'UPDATE material SET id="{id}" WHERE id="{alterar}"'
	cursor.execute(comando)
	banco.commit()
	
#DELETE
def delete(id):
	comando = f'DELETE FROM material WHERE id= "{id}"'
	cursor.execute(comando)
	banco.commit()
