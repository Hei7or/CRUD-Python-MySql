import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdcrud'
)
cursor = conexao.cursor()

# CREATE
nome_produto = "snickers"
valor = 5
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

# READ
comando= f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() 
print(resultado)

# UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close
conexao.close









