from datetime import datetime


def calcular_idade_em_meses(data_nascimento, data_atual):
    meses = (data_atual.year - data_nascimento.year) * 12 + (data_atual.month - data_nascimento.month)
    return meses


def calcular_idade_em_dias(data_nascimento, data_atual):
    diferenca = data_atual - data_nascimento
    return diferenca.days


def calcular_idade_em_horas(data_nascimento, data_atual):
    diferenca = data_atual - data_nascimento
    horas = diferenca.days * 24 + diferenca.seconds // 3600
    return horas


def calcular_idade_em_minutos(data_nascimento, data_atual):
    diferenca = data_atual - data_nascimento
    minutos = diferenca.days * 24 * 60 + diferenca.seconds // 60
    return minutos


def calcular_idade_em_segundos(data_nascimento, data_atual):
    diferenca = data_atual - data_nascimento
    segundos = diferenca.days * 24 * 3600 + diferenca.seconds
    return segundos


def main():
    print("Calculadora de Idade")
    while True:
        print("\nOpções:")
        print("1. Calcular idade em meses")
        print("2. Calcular idade em dias")
        print("3. Calcular idade em horas")
        print("4. Calcular idade em minutos")
        print("5. Calcular idade em segundos")
        print("6. Sair do programa")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            data_nascimento = datetime.strptime(input("Digite a data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d")
            data_atual = datetime.strptime(input("Digite a data atual (AAAA-MM-DD): "), "%Y-%m-%d")
            meses = calcular_idade_em_meses(data_nascimento, data_atual)
            print(f"Sua idade em meses é: {meses} meses")
        elif escolha == "2":
            data_nascimento = datetime.strptime(input("Digite a data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d")
            data_atual = datetime.strptime(input("Digite a data atual (AAAA-MM-DD): "), "%Y-%m-%d")
            dias = calcular_idade_em_dias(data_nascimento, data_atual)
            print(f"Sua idade em dias é: {dias} dias")
        elif escolha == "3":
            data_nascimento = datetime.strptime(input("Digite a data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d")
            data_atual = datetime.strptime(input("Digite a data atual (AAAA-MM-DD): "), "%Y-%m-%d")
            horas = calcular_idade_em_horas(data_nascimento, data_atual)
            print(f"Sua idade em horas é: {horas} horas")
        elif escolha == "4":
            data_nascimento = datetime.strptime(input("Digite a data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d")
            data_atual = datetime.strptime(input("Digite a data atual (AAAA-MM-DD): "), "%Y-%m-%d")
            minutos = calcular_idade_em_minutos(data_nascimento, data_atual)
            print(f"Sua idade em minutos é: {minutos} minutos")
        elif escolha == "5":
            data_nascimento = datetime.strptime(input("Digite a data de nascimento (AAAA-MM-DD): "), "%Y-%m-%d")
            data_atual = datetime.strptime(input("Digite a data atual (AAAA-MM-DD): "), "%Y-%m-%d")
            segundos = calcular_idade_em_segundos(data_nascimento, data_atual)
            print(f"Sua idade em segundos é: {segundos} segundos")
        elif escolha == "6":
            print("Obrigado por usar a calculadora de idade. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
