import random

numero_secreto = random.randint(1, 100)

tentativas = 0

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    try:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa < 1 or tentativa > 100:
            print("Por favor, digite um número entre 1 e 100.")
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
            break
    except ValueError:
        print("Por favor, digite um número válido.")

print("Fim do Jogo!")
