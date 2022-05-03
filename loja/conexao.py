
from gzip import READ
import mysql.connector
from mysql.connector import errorcode
try:
	banco = mysql.connector.connect(host='127.0.0.2',port=8081, user='root', password='pets', database='pets')
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
def create(id,produto,valor):
	comando = f'INSERT INTO material(nome,valor) VALUES("{produto}",{valor})'
	cursor.execute(comando)
	banco.commit()
	return "deu bom"
#READ
def read():
	comando = 'SELECT * FROM material'
	cursor.execute(comando)
	resposta = cursor.fetchall()
	for rep in resposta:
		print(rep)
	return 
#UPDATE
def update(valor,nome_produto):
	comando = f'UPDATE material SET valor="{valor}"WHERE nome="{nome_produto}"'
	cursor.execute(comando)
	banco.commit()
	return "deu bom"
read()
update(10,'OSSO 1kg ')
read()