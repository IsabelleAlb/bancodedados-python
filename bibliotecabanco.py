import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "academiaturmad"
)
"""print (banco)
meucursor = banco.cursor()
pesquisa = "select * from alunos;"
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

nome1 = "menino ney"
telefone1 = "11111111"
sqlAluno = "insert into alunos (nome, telefone) values (%s,%s)"
data = (nome1, telefone1)
meucursor.execute(sqlAluno, data)
banco.commit()
meucursor.close()
banco.close()"""