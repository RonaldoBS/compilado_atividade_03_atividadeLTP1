import datetime

# Função para calcular a idade com base no ano de nascimento
def calcular_idade(ano_nascimento):
    data_atual = datetime.datetime.now()
    ano_atual = data_atual.year
    idade = ano_atual - ano_nascimento
    return idade

# Função para determinar o signo com base na data de nascimento
def determinar_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    else:
        return "Peixes"

# Solicita ao usuário o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade atual
idade = calcular_idade(ano_nascimento)

# Solicita o mês e o dia de nascimento
mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
dia_nascimento = int(input("Digite o dia de nascimento: "))

# Determina o signo com base na data de nascimento
signo = determinar_signo(dia_nascimento, mes_nascimento)

# Imprime a idade e o signo no console
print("Sua idade atual é:", idade, "anos")
print("Seu signo é:", signo)
