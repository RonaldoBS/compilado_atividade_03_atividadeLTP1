def calcular_total_com_imposto(valor_compra, taxa_imposto):
    total = valor_compra + (valor_compra * (taxa_imposto / 100))
    return total
def main():
    print("Calculadora de Impostos")
    while True:
        print("\nOpções:")
        print("1. Calcular total com imposto padrão")
        print("2. Calcular total com imposto personalizado")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            valor_compra = float(input("Digite o valor da compra: R$ "))
            taxa_imposto = 10  # Imposto padrão de 10%
            total = calcular_total_com_imposto(valor_compra, taxa_imposto)
            print(f"O total da compra com imposto padrão é: R$ {total:.2f}")
        elif escolha == "2":
            valor_compra = float(input("Digite o valor da compra: R$ "))
            taxa_imposto = float(input("Digite a taxa de imposto (em %): "))
            total = calcular_total_com_imposto(valor_compra, taxa_imposto)
            print(f"O total da compra com imposto personalizado é: R$ {total:.2f}")
        elif escolha == "0":
            print("Obrigado por usar a calculadora de impostos. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
