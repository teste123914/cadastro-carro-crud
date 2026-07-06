from marca import *
from modelo import *
from carro import *

# ==========================================
# UTILITÁRIOSSSSSS
# ==========================================

def cabecalho(titulo):
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60)


# ==========================================
# MENU MARCAS
# ==========================================

def menu_marcas():

    while True:

        cabecalho("GERENCIAR MARCAS")

        print("1 - Cadastrar Marca")
        print("2 - Listar Marcas")
        print("3 - Atualizar Marca")
        print("4 - Excluir Marca")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            nome = input("Nome da marca: ")

            criar_marca(nome)

            print("\nMarca cadastrada com sucesso!")

        elif opcao == "2":

            marcas = listar_marcas()

            cabecalho("MARCAS")

            print(f"{'ID':<5}{'NOME'}")
            print("-" * 60)

            for id, nome in marcas:
                print(f"{id:<5}{nome}")

            print("-" * 60)

        elif opcao == "3":

            id = int(input("ID da marca: "))
            nome = input("Novo nome: ")

            atualizar_marca(id, nome)

            print("\nMarca atualizada!")

        elif opcao == "4":

            id = int(input("ID da marca: "))

            excluir_marca(id)

            print("\nMarca excluída!")

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")


# ==========================================
# MENU MODELOS
# ==========================================

def menu_modelos():

    while True:

        cabecalho("GERENCIAR MODELOS")

        print("1 - Cadastrar Modelo")
        print("2 - Listar Modelos")
        print("3 - Atualizar Modelo")
        print("4 - Excluir Modelo")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            nome = input("Nome do modelo: ")
            id_marca = int(input("ID da marca: "))

            criar_modelo(nome, id_marca)

            print("\nModelo cadastrado!")

        elif opcao == "2":

            modelos = listar_modelos()

            cabecalho("MODELOS")

            print(f"{'ID':<5}{'MODELO':<20}{'MARCA'}")
            print("-" * 60)

            for id, modelo, marca in modelos:

                print(
                    f"{id:<5}"
                    f"{modelo:<20}"
                    f"{marca}"
                )

            print("-" * 60)

        elif opcao == "3":

            id = int(input("ID do modelo: "))
            nome = input("Novo nome: ")
            id_marca = int(input("Novo ID da marca: "))

            atualizar_modelo(id, nome, id_marca)

            print("\nModelo atualizado!")

        elif opcao == "4":

            id = int(input("ID do modelo: "))

            excluir_modelo(id)

            print("\nModelo excluído!")

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")


# ==========================================
# MENU CARROS
# ==========================================

def menu_carros():

    while True:

        cabecalho("GERENCIAR CARROS")

        print("1 - Cadastrar Carro")
        print("2 - Listar Carros")
        print("3 - Atualizar Carro")
        print("4 - Excluir Carro")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            nome = input("Nome do carro: ")
            id_modelo = int(input("ID do modelo: "))
            renavam = input("Renavam: ")
            placa = input("Placa: ")
            valor = float(input("Valor: "))
            ano = int(input("Ano: "))

            criar_carro(
                id_modelo,
                nome,
                renavam,
                placa,
                valor,
                ano
            )

            print("\nCarro cadastrado!")

        elif opcao == "2":

            carros = listar_carros()

            cabecalho("CARROS")

            print(
                f"{'ID':<5}"
                f"{'CARRO':<20}"
                f"{'MODELO':<15}"
                f"{'PLACA':<12}"
                f"{'VALOR':<12}"
                f"{'ANO'}"
            )

            print("-" * 90)

            for id, carro, modelo, placa, valor, ano in carros:

                print(
                    f"{id:<5}"
                    f"{carro:<20}"
                    f"{modelo:<15}"
                    f"{placa:<12}"
                    f"{str(valor):<12}"
                    f"{ano}"
                )

            print("-" * 90)

        elif opcao == "3":

            id = int(input("ID do carro: "))
            nome = input("Nome: ")
            id_modelo = int(input("ID do modelo: "))
            renavam = input("Renavam: ")
            placa = input("Placa: ")
            valor = float(input("Valor: "))
            ano = int(input("Ano: "))

            atualizar_carro(
                id,
                id_modelo,
                nome,
                renavam,
                placa,
                valor,
                ano
            )

            print("\nCarro atualizado!")

        elif opcao == "4":

            id = int(input("ID do carro: "))

            excluir_carro(id)

            print("\nCarro excluído!")

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    cabecalho("SISTEMA DE CONCESSIONÁRIA")

    print("1 - Gerenciar Marcas")
    print("2 - Gerenciar Modelos")
    print("3 - Gerenciar Carros")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        menu_marcas()

    elif opcao == "2":

        menu_modelos()

    elif opcao == "3":

        menu_carros()

    elif opcao == "0":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida!")