import random

def jogo_par_ou_impar():
    print("Bem-vindo ao Jogo Par ou Ímpar!")
    nome_jogador = input("Digite o seu nome: ")

    while True:
        try:
            numero_jogador = int(input("Digite um número: "))
            escolha_jogador = input("Escolha 'par' ou 'ímpar': ").lower()

            if escolha_jogador not in ['par', 'ímpar']:
                print("Escolha inválida. Digite 'par' ou 'ímpar'.")
                continue

            numero_computador = random.randint(1, 10)
            soma = numero_jogador + numero_computador
            resultado = "par" if soma % 2 == 0 else "ímpar"

            print(f"{nome_jogador} escolheu {numero_jogador} e o computador escolheu {numero_computador}.")
            print(f"A soma é {soma}, que é {resultado}.")

            if resultado == escolha_jogador:
                print(f"{nome_jogador} venceu!")
            else:
                print("O computador venceu!")

            continuar = input("Deseja jogar novamente? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_par_ou_impar()
