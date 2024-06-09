#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caçadores de Tesouros
# Nome: Henrique Allan Borges Ribeiro
# RA: Henrique Allan Borges Ribeiro
#####################################################

# Leitura do mapa
n, m = [int(i) for i in input().split()]

mapa = []
for _ in range(n):
  linha = [int(i) for i in input().split()]
  mapa.append(linha)
# Leitura e processamento dos movimentos dos personagens
q = int(input())

posicao_personagem_inicial = []
movimentos_personagem = []
for X in range (0, q):
    L, C = [int(i) for i in input().split()]
    posicao = [L,C]
    posicao_personagem_inicial.append(posicao)
    movimentos = list(input())
    movimentos_personagem.append(movimentos)

for X in range (0,q):
  i, j = posicao_personagem_inicial[X]
  direcoes = movimentos_personagem[X]
  tesouro_inicial = mapa[i][j]
  
  for Y in range(0,len(direcoes)):
    if direcoes[Y] == "S":
       i = i+1
    if direcoes[Y] == "N":
       i = i-1
    if direcoes[Y] == "L":
       j = j+1
    if direcoes[Y] == "O":
       j= j-1
    tesouro_pos = mapa[i][j]
    if tesouro_pos > tesouro_inicial:
       mapa[i][j] = tesouro_inicial
       tesouro_inicial = tesouro_pos
  
# Impressão da saída
  print("Caçador ",X+1,": ",(tesouro_inicial),sep="")