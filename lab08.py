###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Anagramas
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura das palavras
N = int(input())
palavras = []
for X in range(N):
    palavras.append((input()))

# Agrupamento dos anagramas
lista = []
for X in range(N):
    anagramas = []
    sorted(palavras[X])
    for Y in range(N):
        if sorted(palavras[X]) == sorted(palavras[Y]):
            anagramas.append(palavras[Y])
    if (anagramas in lista) == False:
        lista.append(anagramas)

# Impressão da saída
for anagramas in lista:
    for Z in range (len(anagramas)):
        if Z < len(anagramas)-1:
            print(anagramas[Z] , end="-")
        else:
            print(anagramas[Z])