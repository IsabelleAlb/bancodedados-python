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
            cpf = input ("CPF do aluno: ")
            telefone = input("Telefone para contato: ")
            email = input("Email do aluno: ")
            endereco = input("Endereço do aluno: ")
            inseriraluno(nome, cpf, telefone, email, endereco)

        if operacao == "2":
            matricula = int(input("Qual a matrícula do aluno? "))
            deletarAluno(matricula)

        if operacao == "3":
            mostrarAlunos()

        """if operacao == "Vv":"""



    while menu == "2":
        operacao = input("Qual operação você deseja realizar? \n"
                          "\n[1]Inserir modalidade \n[2]Deletar modalidade \n[3]Mostrar lista de modalidades \n[V]Voltar \n")
        if operacao == "1":
            nome = input("Digite o nome da modalidade: ")
            inserirmodalidade(nome)

        """if operacao == "2":"""
        if operacao == "3":
            mostrarModalidades()

        """if operacao == "Vv":"""



    while menu == "3":
        operacao = input("Qual operação você deseja realizar? \n"
                          "\n[1]Inserir um funcionário \n[2]Deletar um funcionário \n[3]Mostrar lista de funcionários \n[V]Voltar \n")
        if operacao == "1":
            nome = input("Digite o nome do funcionário: ")
            cpf = input("CPF do funcionário: ")
            depart = input("Em qual departamento ele irá trabalhar: ")
            salario = float(input("Qual será o salário do funcionário: "))
            filhos = int(input("O funcionário tem quantos filhos: "))
            inserirfuncionario(nome, cpf, depart, salario, filhos)

        """if operacao == "2":"""

        if operacao == "3":
            mostrarFuncionarios()


        """if operacao == "Vv":"""


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

        """if operacao == "2":"""

        if operacao == "3":
            mostrarPersonal()

        """if operacao == "Vv":"""