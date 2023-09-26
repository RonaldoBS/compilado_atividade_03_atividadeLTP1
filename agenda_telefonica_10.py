import os
import json

def exibir_agenda(agenda):
    print("Agenda Telefônica:")
    for i, contato in enumerate(agenda, start=1):
        print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def adicionar_contato(agenda, nome, telefone):
    novo_contato = {"nome": nome, "telefone": telefone}
    agenda.append(novo_contato)
    salvar_agenda(agenda)
    print("Contato adicionado!")

def pesquisar_contato(agenda, nome):
    contatos_encontrados = [contato for contato in agenda if nome.lower() in contato['nome'].lower()]
    if contatos_encontrados:
        exibir_agenda(contatos_encontrados)
    else:
        print("Nenhum contato encontrado com esse nome.")

def editar_contato(agenda, nome, novo_nome, novo_telefone):
    for contato in agenda:
        if nome.lower() == contato['nome'].lower():
            contato['nome'] = novo_nome
            contato['telefone'] = novo_telefone
            salvar_agenda(agenda)
            print("Contato editado com sucesso!")
            return
    print("Nenhum contato encontrado com esse nome.")

def excluir_contato(agenda, nome):
    for contato in agenda:
        if nome.lower() == contato['nome'].lower():
            agenda.remove(contato)
            salvar_agenda(agenda)
            print("Contato excluído com sucesso!")
            return
    print("Nenhum contato encontrado com esse nome.")

def salvar_agenda(agenda):
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo)
def carregar_agenda():
    agenda = []
    if os.path.exists("agenda.json"):
        with open("agenda.json", "r") as arquivo:
            agenda = json.load(arquivo)
    return agenda

def main():
    agenda = carregar_agenda()

    while True:
        print("\nOpções:")
        print("1. Exibir agenda")
        print("2. Adicionar contato")
        print("3. Pesquisar contato")
        print("4. Editar contato")
        print("5. Excluir contato")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            exibir_agenda(agenda)
        elif escolha == "2":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(agenda, nome, telefone)
        elif escolha == "3":
            nome = input("Digite o nome do contato a ser pesquisado: ")
            pesquisar_contato(agenda, nome)
        elif escolha == "4":
            nome = input("Digite o nome do contato a ser editado: ")
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            editar_contato(agenda, nome, novo_nome, novo_telefone)
        elif escolha == "5":
            nome = input("Digite o nome do contato a ser excluído: ")
            excluir_contato(agenda, nome)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
