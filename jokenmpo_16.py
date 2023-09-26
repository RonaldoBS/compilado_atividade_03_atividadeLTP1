import random
def jogar_jogo():
    print("Bem-vindo ao Jogo Pedra, Papel e Tesoura!")
    while True:
        jogador = input("Escolha: pedra, papel ou tesoura (ou digite 'sair' para encerrar o jogo): ").lower()
        if jogador == 'sair':
            break

        if jogador not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Tente novamente.")
            continue

        escolhas = ['pedra', 'papel', 'tesoura']
        computador = random.choice(escolhas)

        print(f"Você escolheu: {jogador}")
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu!")
        else:
            print("Computador venceu!")

if __name__ == "__main__":
    jogar_jogo()
