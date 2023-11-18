from bibliotecafuncoes import *

while True:
    menu = input("Em qual tabela você deseja realizar uma operação? \n"
                 "\n[1]Alunos \n[2]Modalidades \n[3]Funcionários \n[4]Personal \n[s]Sair \n")

    while menu not in "1234Ss":
        menu = (input("OPÇÃO INVÁLIDA! Em qual tabela você deseja realizar uma operação? \n"
                      "\n[1]Alunos \n[2]Modalidades \n[3]Funcionários \n[4]Personal \n[s]Sair: "))

    while menu == "1":
        operacao = input("Qual operação você deseja realizar? \n"
                         "\n[1]Inserir um aluno \n[2]Deletar um aluno \n[3]Mostrar lista de alunos \n[V]Voltar \n")
        if operacao == "1":
            nome = input("Nome do aluno: ")
            cpf = input("CPF do aluno: ")
            telefone = input("Telefone para contato: ")
            email = input("Email do aluno: ")
            endereco = input("Endereço do aluno: ")
            inseriraluno(nome, cpf, telefone, email, endereco)
            print("Aluno cadastrado com sucesso!")

        elif operacao == "2":
            matricula = int(input("Qual a matrícula do aluno? "))
            deletarAluno(matricula)
            print("Aluno removido!")

        elif operacao == "3":
            mostrarAlunos()

        else:
            break

    while menu == "2":
        operacao = input("Qual operação você deseja realizar? \n"
                         "\n[1]Inserir modalidade \n[2]Deletar modalidade \n[3]Mostrar lista de modalidades \n["
                         "V]Voltar \n")
        if operacao == "1":
            nome = input("Digite o nome da modalidade: ")
            inserirmodalidade(nome)
            print("Modalidade cadastrada!")

        elif operacao == "2":
            id_modalidade = int(input("Qual o id da modalidade que você deseja deletar? "))
            deletarModalidade(id_modalidade)
            print("Modalidade removida")

        elif operacao == "3":
            mostrarModalidades()

        else:
            break

    while menu == "3":
        operacao = input("Qual operação você deseja realizar? \n"
                         "\n[1]Inserir um funcionário \n[2]Deletar um funcionário \n[3]Mostrar lista de funcionários \n["
                         "V]Voltar \n")
        if operacao == "1":
            nome = input("Digite o nome do funcionário: ")
            cpf = input("CPF do funcionário: ")
            depart = input("Em qual departamento ele irá trabalhar: ")
            salario = float(input("Qual será o salário do funcionário: "))
            filhos = int(input("O funcionário tem quantos filhos: "))
            inserirfuncionario(nome, cpf, depart, salario, filhos)
            print("Funcionário cadastrado!")

        elif operacao == "2":
            id_funcionario = int(input("Qual o id do funcionário que você deseja deletar? "))
            deletarFuncionario(id_funcionario)
            print("Funcionário removido!")


        elif operacao == "3":
            mostrarFuncionarios()

        else:
            break

    while menu == "4":
        operacao = input("Qual operação você deseja realizar? \n"
                         "\n[1]Inserir um Personal \n[2]Deletar um Personal \n[3]Mostrar lista de Personal \n[V]Voltar \n")
        if operacao == "1":
            cpf = input("CPF do personal: ")
            cref = input("Qual o CREF do personal: ")
            nome = input("Digite o nome do personal: ")
            telefone = input("Qual o telefone para contato: ")
            email = input("Email do personal: ")
            inserirpersonal(cpf, cref, nome, telefone, email)
            print("Personal cadastrado!")

        elif operacao == "2":
            cref = int(input("Qual o CREF do personal que você deseja deletar? "))
            deletarPersonal(cref)
            print("Personal removido!")


        elif operacao == "3":
            mostrarPersonal()

        else:
            break
