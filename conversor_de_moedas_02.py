moeda_origem = input("Digite a moeda de origem: ")
moeda_destino = input("Digite a moeda de destino: ")
quantidade = float(input("Digite a quantidade a ser convertida: "))
taxa_cambio = float(input("Digite a taxa de câmbio (1 {} = X {}): ".format(moeda_origem, moeda_destino)))
valor_convertido = quantidade * taxa_cambio
print("{} {} é igual a {} {}".format(quantidade, moeda_origem, valor_convertido, moeda_destino))
