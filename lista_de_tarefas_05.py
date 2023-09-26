import os


def exibir_tarefas(tarefas):
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa[1] else "Pendente"
        print(f"{i}. [{status}] {tarefa[0]}")


def adicionar_tarefa(tarefas, nova_tarefa):
    tarefas.append([nova_tarefa, False])
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")


def marcar_tarefa_concluida(tarefas, indice):
    if indice >= 1 and indice <= len(tarefas):
        tarefas[indice - 1][1] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")


def remover_tarefa(tarefas, indice):
    if indice >= 1 and indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f"Tarefa removida: {tarefa_removida[0]}")
    else:
        print("Índice inválido.")


def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa[0]},{tarefa[1]}\n")


def carregar_tarefas():
    tarefas = []
    if os.path.exists("tarefas.txt"):
        with open("tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                if len(partes) == 2:
                    tarefa = [partes[0], partes[1] == "True"]
                    tarefas.append(tarefa)
    return tarefas
def main():
    tarefas = carregar_tarefas()

    while True:
        exibir_tarefas(tarefas)

        print("\nOpções:")
        print("1. Adicionar nova tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Remover tarefa")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            nova_tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa)
        elif escolha == "2":
            indice = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(tarefas, indice)
        elif escolha == "3":
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
