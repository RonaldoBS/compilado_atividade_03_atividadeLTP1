frase = input("Digite uma frase: ")
palavras = frase.split()
numero_palavras = len(palavras)
frase_maiusculas_sem_espacos = frase.upper().replace(" ", "")
print("Número de palavras na frase:", numero_palavras)
print("Frase em maiúsculas sem espaços em branco:", frase_maiusculas_sem_espacos)