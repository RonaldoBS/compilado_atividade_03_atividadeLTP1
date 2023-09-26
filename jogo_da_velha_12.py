def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(simbolo == jogador for simbolo in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    vitorias = {"X": 0, "O": 0}

    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f"Jogador {jogador_atual}, escolha a linha e coluna (1-3) para inserir '{jogador_atual}': ").split())
        linha -= 1
        coluna -= 1

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                vitorias[jogador_atual] += 1
                break
            jogador_atual = "X" if jogador_atual == "O" else "O"
        else:
            print("Posição ocupada. Tente novamente.")

    imprimir_tabuleiro(tabuleiro)
    print("Fim do jogo.")
    print(f"Vitórias - Jogador X: {vitorias['X']} Jogador O: {vitorias['O']}")

if __name__ == "__main__":
    jogar_jogo_da_velha()
