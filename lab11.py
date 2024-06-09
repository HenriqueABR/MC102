###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Loteamento
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura de dados
t = 15
loteamento = []
ruas_horizontais = list(map(int, input().split()))
ruas_verticais = list(map(int, input().split()))
n = int(input())
lotes = []
for X in range (0,n):
    lotes.append(list(map(int, input().split())))
print(lotes)
print(ruas_horizontais)
print(ruas_verticais)

for X in range (t):
    linha = ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
    loteamento.append(linha)
    for Y in range (t):
        for Z in range (len(ruas_verticais)):
            if Y == ruas_verticais[Z]:
                loteamento[X][Y] = "."
for X in range (t):
    for Z in range (len(ruas_horizontais)):
        if X == ruas_horizontais[Z]:
            for Y in range (t):
                loteamento[X][Y] = "."
# Processamento
comprador = 0
for lote in lotes:
    numeros_x = []
    comprador+=1
    limite_sup_esq, limite_sup_dir, limite_inf_esq, limite_inf_dir = lote
    for X in range (limite_sup_esq, limite_inf_esq+1):
        for Y in range (limite_sup_dir, limite_inf_dir+1):
            if loteamento[X][Y] == "x":
                numeros_x.append("x")
    if len(numeros_x) == (limite_inf_esq+1 - limite_sup_esq)*(limite_inf_dir+1-limite_sup_dir):
        for X in range (limite_sup_esq, limite_inf_esq+1):
            for Y in range (limite_sup_dir, limite_inf_dir+1):
                loteamento[X][Y] = str(comprador)
# Impressão da saída
for linha in loteamento:
  print(" ".join(linha))