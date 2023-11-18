from bibliotecabanco import *

meucursor = banco.cursor()

#inserir
def inseriraluno(nome, cpf, telefone, email, endereco):
    sqlAluno = "insert into alunos (nome,cpf, telefone, email, endereco) values (%s, %s, %s, %s, %s);"
    data = (nome, cpf, telefone, email, endereco)
    meucursor.execute(sqlAluno, data)
    banco.commit()


def inserirmodalidade(nome):
    sqlModalidade = "insert into modalidades (nome) values (%s);"
    data = [(nome)]
    meucursor.execute(sqlModalidade, data)
    banco.commit()
    print("Modalidade cadastrada!")


def inserirfuncionario(nome, cpf, departamento, salario, filhos_fun):
    sqlFunc = "insert into func (nome, cpf, departamento, salario, filhos_fun) values (%s, %s, %s, %s, %s)"
    data = (nome, cpf, departamento, salario, filhos_fun)
    meucursor.execute(sqlFunc, data)
    banco.commit()


def inserirpersonal(cpf, cref, nome, telefone, email):
    sqlPersonal = "insert into personal (cpf, cref, nome, telefone, email) values (%s, %s, %s, %s, %s)"
    data = (cpf, cref, nome, telefone, email)
    meucursor.execute(sqlPersonal, data)
    banco.commit()


# mostrar conteúdo das tabelas
def mostrarAlunos():
    pesquisa = "select * from alunos;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)


def mostrarModalidades():
    pesquisa = "select * from modalidades;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for a in resultado:
        print(a)


def mostrarFuncionarios():
    pesquisa = "select * from func;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for z in resultado:
        print(z)


def mostrarPersonal():
    pesquisa = "select * from personal;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for y in resultado:
        print(y)


# deletar
def deletarAluno(matricula):
    deleteAluno = f"delete from alunos where matricula = {matricula}"
    meucursor.execute(deleteAluno)
    banco.commit()


def deletarModalidade(id_modalidade):
    deleteModalidade = f"delete from modalidades where id_modalidade = {id_modalidade}"
    meucursor.execute(deleteModalidade)
    banco.commit()

def deletarFuncionario(id_funcionario):
    deletefunc = f"delete from func where id_funcionario = {id_funcionario}"
    meucursor.execute(deletefunc)
    banco.commit()

def deletarPersonal(cref):
    deletepersonal = f"delete from personal where cref = {cref}"
    meucursor.execute(deletepersonal)
    banco.commit()

meucursor.close()
banco.close()
