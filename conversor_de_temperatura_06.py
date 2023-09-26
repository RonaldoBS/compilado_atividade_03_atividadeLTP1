
def celsius_para_fahrenheit(celsius, casas_decimais=2):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, casas_decimais)


def fahrenheit_para_celsius(fahrenheit, casas_decimais=2):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, casas_decimais)


print("Escolha uma opção:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = input("Digite o número da opção desejada: ")


if opcao == "1":
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    casas_decimais = int(input("Digite o número de casas decimais desejado: "))
    fahrenheit = celsius_para_fahrenheit(celsius, casas_decimais)
    print(f"{celsius} graus Celsius são {fahrenheit} graus Fahrenheit.")
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    casas_decimais = int(input("Digite o número de casas decimais desejado: "))
    celsius = fahrenheit_para_celsius(fahrenheit, casas_decimais)
    print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
else:
    print("Opção inválida. Tente novamente.")
