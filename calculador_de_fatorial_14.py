def calcular_fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

try:
    numero = int(input("Digite um número para calcular o fatorial: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
except ValueError as e:
    print(e)
