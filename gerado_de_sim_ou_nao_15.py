import random
def gerar_resposta():
    respostas = ["Sim", "Não", "Talvez"]
    return random.choice(respostas)
while True:
    pergunta = input("Faça uma pergunta (ou digite 'sair' para encerrar): ")
    if pergunta.lower() == 'sair':
        print("Obrigado por jogar!")
        break

    resposta = gerar_resposta()
    print(f"Resposta: {resposta}")
