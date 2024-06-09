###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Pulo do Gato
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################
'''
Função recursiva para simular o caminho do gato. A função recebe
uma matriz representando o mapa do circuito, a posição (linha,coluna)
do gato e a posição (linha, coluna) do petisco. A função deve retornar 
se o gato consegue capturar o petisco.
'''
posicoes = []
def pulo_do_gato(mapa, linha_gato, coluna_gato, linha_petisco, coluna_petisco):
  vizinho_direita = False
  vizinho_esquerda = False
  vizinho_baixo = False
  vizinho_cima = False
  print(linha_gato,coluna_gato)
  if [linha_gato, coluna_gato] == [linha_petisco, coluna_petisco]:
    return True
  if mapa[linha_gato][coluna_gato] == "H":
    [nova_coluna_gato] = [coluna_gato+1]
    if int(nova_coluna_gato) == (len(mapa[0])) or [linha_gato, nova_coluna_gato] in posicoes:
      vizinho_direita = False
      posicoes.append([linha_gato, nova_coluna_gato])
    else:
      posicoes.append([linha_gato, nova_coluna_gato])
      vizinho_direita = pulo_do_gato(mapa, linha_gato, nova_coluna_gato, linha_petisco, coluna_petisco)
    [nova_coluna_gato] = [coluna_gato-1]
    if int(nova_coluna_gato) < 0 or [linha_gato, nova_coluna_gato] in posicoes:
      vizinho_esquerda = False
      posicoes.append([linha_gato, nova_coluna_gato])      
    else:
      posicoes.append([linha_gato, nova_coluna_gato])
      vizinho_esquerda = pulo_do_gato(mapa, linha_gato, nova_coluna_gato, linha_petisco, coluna_petisco)
    if vizinho_direita == True:
      return True
    if vizinho_esquerda == True:
      return True
    if vizinho_direita == False and vizinho_esquerda == False:
      return False
  if mapa[linha_gato][coluna_gato] == "V":
    [nova_linha_gato] = [linha_gato+1]
    if int(nova_linha_gato) == (len(mapa)) or [nova_linha_gato, coluna_gato] in posicoes:
      vizinho_baixo = False
      posicoes.append([nova_linha_gato, coluna_gato])
    else:
      posicoes.append([nova_linha_gato, coluna_gato])
      vizinho_baixo = pulo_do_gato(mapa, nova_linha_gato, coluna_gato, linha_petisco, coluna_petisco)
    [nova_linha_gato] = [linha_gato-1]
    if int(nova_linha_gato) < 0 or [nova_linha_gato, coluna_gato] in posicoes:
      vizinho_cima = False
      posicoes.append([nova_linha_gato, coluna_gato])
    else:
      posicoes.append([nova_linha_gato, coluna_gato])      
      vizinho_cima = pulo_do_gato(mapa, nova_linha_gato, coluna_gato, linha_petisco, coluna_petisco)
    if vizinho_cima == True:
      return True
    if vizinho_baixo == True:
      return True
    if vizinho_cima == False and vizinho_baixo == False:
      return False





# Leitura de dados
n = int(input())

mapa = []
for _ in range(n):
  mapa.append(list(input()))

linha_gato, coluna_gato = input().split()
posicao_inicial = [linha_gato,coluna_gato]
for X in range (len(mapa)):
  for Y in range (len(mapa[0])):
    if mapa[X][Y] == "*":
      linha_petisco,coluna_petisco = X,Y
linha_gato = int(linha_gato)
coluna_gato = int(coluna_gato)
linha_petisco = int(linha_petisco)
coluna_petisco = int(coluna_petisco)

# Impressão da resposta
if pulo_do_gato(mapa, linha_gato, coluna_gato, linha_petisco, coluna_petisco) == True:
    print("Petisco capturado")
else:
    print("Petisco não capturado")