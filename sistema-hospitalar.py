from operacoesbd import *

opcao = -1
# Iniciando conexão com o Banco De Dados
con = criarConexao("localhost", "root", "124578", "trabalho")


def adicionar_paciente(con):
    cpf = input("CPF: ")
    sql = "SELECT cpf FROM pacientes WHERE cpf = %s"
    dados = (cpf,)
    resultado = listarBancoDados(con, sql, dados)
    if resultado:
        print("Operação falhou: paciente já cadastrado.")
        return

    nome = input("Nome: ")
    idade = input("Idade: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")

    if not all([cpf, nome, idade, endereco, telefone]):
        print("Por favor, preencha todos os campos obrigatórios.")
        return

    sql = "INSERT INTO pacientes (cpf, nome, idade, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
    dados = (cpf, nome, idade, endereco, telefone)
    insertNoBancoDados(con, sql, dados)
    print("Novo paciente cadastrado com sucesso!")


def adicionar_medico(con):
    crm = input("CRM: ")
    sql = "SELECT crm FROM medicos WHERE crm = %s"
    dados = (crm,)
    resultado = listarBancoDados(con, sql, dados)
    if resultado:
        print("Operação falhou: médico já cadastrado.")
        return

    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")

    if not all([crm, nome, especialidade, telefone]):
        print("Por favor, preencha todos os campos obrigatórios.")
        return

    sql = "INSERT INTO medicos (crm, nome, especialidade, telefone) VALUES (%s, %s, %s, %s)"
    dados = (crm, nome, especialidade, telefone)
    insertNoBancoDados(con, sql, dados)
    print("Novo médico cadastrado com sucesso!")


def pesquisar_paciente(con):
    cpf = input("CPF: ")
    sql = "SELECT * FROM pacientes WHERE cpf = %s"
    dados = (cpf,)
    paciente = listarBancoDados(con, sql, dados)
    if paciente:
        print(f"Paciente encontrado: {paciente}")
    else:
        print("Operação falhou: paciente não encontrado.")


def pesquisar_medico(con):
    crm = input("CRM: ")
    sql = "SELECT * FROM medicos WHERE crm = %s"
    dados = (crm,)
    medico = listarBancoDados(con, sql, dados)
    if medico:
        print(f"Médico encontrado: {medico}")
    else:
        print("Operação falhou: médico não encontrado.")


def excluir_paciente(con):
    cpf = input("CPF: ")
    sql = "DELETE FROM pacientes WHERE cpf = %s"
    dados = (cpf,)
    linhas_afetadas = excluirBancoDados(con, sql, dados)
    if linhas_afetadas:
        print("Paciente excluído com sucesso!")
    else:
        print("Operação falhou: paciente não encontrado.")


def excluir_medico(con):
    crm = input("CRM: ")
    sql = "DELETE FROM medicos WHERE crm = %s"
    dados = (crm,)
    linhas_afetadas = excluirBancoDados(con, sql, dados)
    if linhas_afetadas:
        print("Médico excluído com sucesso!")
    else:
        print("Operação falhou: médico não encontrado.")


while True:
    print("\nMenu do Sistema")
    print("1. Adicionar Novo Paciente")
    print("2. Adicionar Novo Médico")
    print("3. Pesquisar Paciente por CPF")
    print("4. Pesquisar Médico por CRM")
    print("5. Excluir Paciente pelo CPF")
    print("6. Excluir Médico pelo CRM")
    print("7. Sair do Sistema")

    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        adicionar_paciente(con)
    elif escolha == "2":
        adicionar_medico(con)
    elif escolha == "3":
        pesquisar_paciente(con)
    elif escolha == "4":
        pesquisar_medico(con)
    elif escolha == "5":
        excluir_paciente(con)
    elif escolha == "6":
        excluir_medico(con)
    elif escolha == "7":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

encerrarBancoDados(con)
