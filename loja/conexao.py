
import mysql.connector
from mysql.connector import errorcode
try:
	banco = mysql.connector.connect(host='172.20.0.2',port=3306, user='root', password='pets', database='pets')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)

cursor = banco.cursor()

#CREATE
def create(id,produto,valor,unidade):
	comando = f'INSERT INTO material(id,nome,valor,unidade) VALUES({id},"{produto}","{valor}","{unidade}")'
	cursor.execute(comando)
	banco.commit()
	
#READ
def read(escolha):
	comando = f'SELECT * FROM material'
	cursor.execute(comando)
	resposta = cursor.fetchall()
	print(resposta)
#UPDATE
def update(alterar,id):
	comando = f'UPDATE material SET id="{alterar}"WHERE id="{id}"'
	cursor.execute(comando)
	banco.commit()
	
#DELETE
def delete(id):
	comando = f'DELETE FROM material WHERE id= "{id}"'
	cursor.execute(comando)
	banco.commit()

