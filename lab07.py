###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Gráfico de Recorrência
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura de dados
N = int(input())
serie_temporal = []
for X in range(N):
    valor_serie = int(input())
    serie_temporal.append(valor_serie)
L = int(input())

lista_binária = []
for X in range(N):
    lista_parcial = []
    for Y in range(N):
        valor_absoluto = abs(serie_temporal[Y] - serie_temporal[X])
        if valor_absoluto <= L:
            lista_parcial.append("0")
        else:
            lista_parcial.append("1")
    lista_binária.append(lista_parcial)

for linha in lista_binária:
    for X in range(N):
        if X < N-1:
            print(linha[X]+" ", end="")
        else:  
            print(linha[X])









# Impressão do gráfico de recorrência