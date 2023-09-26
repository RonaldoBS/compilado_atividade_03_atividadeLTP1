import random
import string
def gerar_senha(comprimento, num_letras, num_numeros, num_especiais):
    letras = string.ascii_letters
    numeros = string.digits
    especiais = string.punctuation
    num_letras = min(num_letras, comprimento - num_numeros - num_especiais)
    num_numeros = min(num_numeros, comprimento - num_letras - num_especiais)
    num_especiais = min(num_especiais, comprimento - num_letras - num_numeros)
    senha_chars = [random.choice(letras) for _ in range(num_letras)]
    senha_chars += [random.choice(numeros) for _ in range(num_numeros)]
    senha_chars += [random.choice(especiais) for _ in range(num_especiais)]
    senha_chars += [random.choice(letras + numeros + especiais) for _ in range(comprimento - len(senha_chars))]
    random.shuffle(senha_chars)
    senha = ''.join(senha_chars)
    return senha
comprimento_senha = int(input("Digite o comprimento da senha desejada: "))

num_letras = int(input("Digite a quantidade de letras na senha: "))
num_numeros = int(input("Digite a quantidade de números na senha: "))
num_especiais = int(input("Digite a quantidade de caracteres especiais na senha: "))

senha_gerada = gerar_senha(comprimento_senha, num_letras, num_numeros, num_especiais)
print("Senha gerada:", senha_gerada)
