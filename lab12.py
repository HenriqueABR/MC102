###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Mansão Mal Assombrada I
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()

# Leitura das posições de cada fantasma e de cada caçador

N = int(input())
posicoes_fantasmas = []
for X in range (N):
   a, l, c = input().split()
   Y = [a,l,c]
   posicoes_fantasmas.append(Y)

M = int(input())
posicoes_cacadores = []
for X in range (M):
   a, l, c = input().split()
   Y = [a,l,c]
   posicoes_cacadores.append(Y)


# Simulação do movimento dos fantasmas
FC = 0
CC = 0

for X in range (N):
   posicao_f = posicoes_fantasmas[X]
   a,l,c = posicao_f
   Z = True
   a = int(a)
   l = int(l)
   c = int(c)
   while Z:
      if (a < 0 or a >= A) or (l < 0 or l >= L) or (c < 0 or c >= len(mansao[0][0])):
         break
      posicao_f_inicial = mansao[a][l][c]
      if posicao_f_inicial == "N":
         l+=-1 
      if posicao_f_inicial == "S":
         l+=1
      if posicao_f_inicial == "O":
         c+=-1
      if posicao_f_inicial == "L":
         c+=1 
      if posicao_f_inicial == "C":
         a+=1 
      if posicao_f_inicial == "B":
         a+=-1 
      if posicao_f_inicial == "X":
         FC+=1
         break
      for C in range (M):
         if a == int(posicoes_cacadores[C][0]) and l == int(posicoes_cacadores[C][1]) and c == int(posicoes_cacadores[C][2]):   
            del posicoes_cacadores[C]
            M+=-1
            CC+=1
            break

# Impressão da saída
print("fantasmas capturados:", FC)
print("caçadores capturados:", CC)