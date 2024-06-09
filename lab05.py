###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - A Última Rodada
# Nome: Henrique Allan Borges Ribeiro  
# RA: 261100
###################################################

# Leitura da primeira linha
N, V, P = input().split()
N = int(N)
V = float(V)
P = float(P)

# Leitura da roleta
Resultados = []
for X in range (N):
    Sinal, Valor, Tipo = input().split()
    Valor = float(Valor)
    if Sinal == "+":
        if Tipo == "Reais":
            Final =  P + Valor
        if Tipo == "%":
            Final = P + P*Valor/100

    if Sinal == "-":
        if Tipo == "Reais":
            if Valor >= P:
                Final = 0
            else:
                Final = P - Valor

        if Tipo == "%":
            if P*Valor/100 >= P:
                Final = 0
            else:
                Final = P - P*Valor/100
    Resultados.append(Final)

# Calculo da probabilidade
Probabilidade = 0
for Y in Resultados:
    if Y >= V:
        Probabilidade = Probabilidade + 1
Probabilidade_Final = Probabilidade*100/N

# Calculo do valor médio
Valor_Final = 0
for Z in range(N):
    Valor_Final = (Valor_Final + Resultados[Z])
Valor_Final = Valor_Final/N

# Imprime a probabilidade do premio final ser suficiente para a viagem
print("{:.2f}%".format(Probabilidade_Final))

# Imprime o valor médio do premio final a ser recebido
print("R$ {:.2f}".format(Valor_Final))