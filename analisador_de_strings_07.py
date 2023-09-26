
def contar_estatisticas(texto):
    maiusculas = 0
    minusculas = 0
    digitos = 0
    especiais = 0
    palavras = len(texto.split())

    for caractere in texto:
        if caractere.isupper():
            maiusculas += 1
        elif caractere.islower():
            minusculas += 1
        elif caractere.isdigit():
            digitos += 1
        else:
            especiais += 1

    return maiusculas, minusculas, digitos, especiais, palavras

texto = input("Digite uma string: ")

maiusculas, minusculas, digitos, especiais, palavras = contar_estatisticas(texto)

print("Letras maiúsculas:", maiusculas)
print("Letras minúsculas:", minusculas)
print("Dígitos:", digitos)
print("Caracteres especiais:", especiais)
print("Palavras:", palavras)
