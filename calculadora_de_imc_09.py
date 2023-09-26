
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def avaliar_peso(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau I"
    elif imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = calcular_imc(peso, altura)
categoria_peso = avaliar_peso(imc)
print(f"Seu IMC é {imc:.2f}. Você está na categoria de peso: {categoria_peso}.")
