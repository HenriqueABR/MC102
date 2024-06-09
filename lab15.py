###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Mansão Mal Assombrada II
# Nome: 
# RA: 
###################################################

'''
Função para encontrar um caminho até a saída, essa função deve ser implementada
de forma recursiva. A função recebe a matriz representando a mansão, um valor
booleano p, indicando se você já encontrou o escudo e está protegido dos
fantasmas, e valores inteiros a, l e c, representando o andar atual, a linha
atual e a coluna atual, respectivamente. A função deve retornar True, caso
exista uma saída, ou False, caso contrário.'''
posicoes = []
posicoes_fantasmas = []
def simula_caminho(mansao, p, a0, l0, c0):
    vizinho_baixo = False
    vizinho_cima = False
    vizinho_esquerda = False
    vizinho_direita = False
    vizinho_superior = False
    vizinho_inferior = False
    print(a0,l0,c0)


    if mansao[a0][l0][c0] == "@":
        p = True
        posicoes_fantasmas.clear
        [l_novo] = [l0+1]
        if int(l_novo) == len(mansao[0]) or [a0,l_novo,c0] in posicoes or [a0,l_novo,c0] in posicoes_fantasmas or mansao[a0][l_novo][c0] == "*":
            vizinho_baixo = False
            posicoes.append([a0,l_novo,c0])
        else:
            if mansao[a0][l_novo][c0] == "F":
                posicoes_fantasmas.append([a0,l_novo,c0])    
                if p == True:
                    vizinho_baixo == True
                    posicoes_fantasmas.clear
            else:    
                posicoes.append([a0,l_novo,c0])
                vizinho_baixo = simula_caminho(mansao, p, a0, l_novo,c0)
        [l_novo] = [l0-1]
        if int(l_novo) < 0 or [a0,l_novo,c0] in posicoes or [a0,l_novo,c0] in posicoes_fantasmas or mansao[a0][l_novo][c0] == "*":
            vizinho_cima = False
            posicoes.append([a0,l_novo,c0])
        else:
            if mansao[a0][l_novo][c0] == "F":
                posicoes_fantasmas.append([a0,l_novo,c0])
                if p == True:
                    vizinho_cima == True
            else:
                posicoes.append([a0,l_novo,c0])
                vizinho_cima = simula_caminho(mansao,p,a0,l_novo,c0)
        if vizinho_cima == True:
            return True
        if vizinho_baixo == True:
            return True
        [c_nova] = [c0+1]
        if int(c_nova) == (len(mansao[0][0])) or [a0,l0,c_nova] in posicoes or [a0,l0,c_nova] in posicoes_fantasmas or mansao[a0][l0][c_nova] == "*":
            vizinho_direita = False
            posicoes.append([a0,l0,c_nova])
        else:
            if mansao[a0][l_novo][c0] == "F" or mansao[a0][l0][c_nova] == "F":
                posicoes_fantasmas.append([a0,l0,c_nova])
                if p == True:
                    vizinho_direita == True
            else:
                posicoes.append([a0,l0,c_nova])
                vizinho_direita = simula_caminho(mansao,p,a0,l0,c_nova)
        [c_nova] = [c0-1]
        if int(c_nova) < 0 or [a0,l0,c_nova] in posicoes or [a0,l0,c_nova] in posicoes_fantasmas or mansao[a0][l0][c_nova] == "*":
            vizinho_esquerda = False
            posicoes.append([a0,l0,c_nova])
        else:
            if mansao[a0][l_novo][c0] == "F" or mansao[a0][l0][c_nova] == "F":
                posicoes_fantasmas.append([a0,l0,c_nova])
                if p == True:
                    vizinho_esquerda == True
            else:
                posicoes.append([a0,l0,c_nova])
                vizinho_esquerda = simula_caminho(mansao,p,a0,l0,c_nova)
        if vizinho_direita == True:
            return True
        if vizinho_esquerda == True:
            return True
        if vizinho_direita == False and vizinho_esquerda == False and vizinho_cima == False and vizinho_baixo == False:
            return False
    if mansao[a0][l0][c0] == "=":
        return True
    if mansao[a0][l0][c0] == ".":
        [l_novo] = [l0+1]
        if int(l_novo) == len(mansao[0]) or [a0,l_novo,c0] in posicoes or [a0,l_novo,c0] in posicoes_fantasmas or mansao[a0][l_novo][c0] == "*":
            vizinho_baixo = False
             posicoes.append([a0,l_novo,c0])
        else:
            if mansao[a0][l_novo][c0] == "F":
                posicoes_fantasmas.append([a0,l_novo,c0])    
                if p == True:
                    vizinho_baixo == True
                    posicoes_fantasmas.clear
            else:    
                posicoes.append([a0,l_novo,c0])
                vizinho_baixo = simula_caminho(mansao, p, a0, l_novo,c0)
        [l_novo] = [l0-1]
        if int(l_novo) < 0 or [a0,l_novo,c0] in posicoes or [a0,l_novo,c0] in posicoes_fantasmas or mansao[a0][l_novo][c0] == "*":
            vizinho_cima = False
            posicoes.append([a0,l_novo,c0])
        else:
            if mansao[a0][l_novo][c0] == "F":
                posicoes_fantasmas.append([a0,l_novo,c0])
                if p == True:
                    vizinho_cima == True
            else:
                posicoes.append([a0,l_novo,c0])
                vizinho_cima = simula_caminho(mansao,p,a0,l_novo,c0)
        if vizinho_cima == True:
            return True
        if vizinho_baixo == True:
            return True
        [c_nova] = [c0+1]
        if int(c_nova) == (len(mansao[0][0])) or [a0,l0,c_nova] in posicoes or [a0,l0,c_nova] in posicoes_fantasmas or mansao[a0][l0][c_nova] == "*":
            vizinho_direita = False
            posicoes.append([a0,l0,c_nova])
        else:
            if mansao[a0][l_novo][c0] == "F" or mansao[a0][l0][c_nova] == "F":
                posicoes_fantasmas.append([a0,l0,c_nova])
                if p == True:
                    vizinho_direita == True
            else:
                posicoes.append([a0,l0,c_nova])
                vizinho_direita = simula_caminho(mansao,p,a0,l0,c_nova)
        [c_nova] = [c0-1]
        if int(c_nova) < 0 or [a0,l0,c_nova] in posicoes or [a0,l0,c_nova] in posicoes_fantasmas or mansao[a0][l0][c_nova] == "*":
            vizinho_esquerda = False
            posicoes.append([a0,l0,c_nova])
        else:
            if mansao[a0][l_novo][c0] == "F" or mansao[a0][l0][c_nova] == "F":
                posicoes_fantasmas.append([a0,l0,c_nova])
                if p == True:
                    vizinho_esquerda == True
            else:
                posicoes.append([a0,l0,c_nova])
                vizinho_esquerda = simula_caminho(mansao,p,a0,l0,c_nova)
        if vizinho_direita == True:
            return True
        if vizinho_esquerda == True:
            return True
        if vizinho_direita == False and vizinho_esquerda == False and vizinho_cima == False and vizinho_baixo == False:
            return False

    if mansao[a0][l0][c0] == "#":
        [a_novo] = [a0+1]
        if int(a_novo) == A or [a_novo,l0,c0] in posicoes or [a_novo,l0,c0] in posicoes_fantasmas or mansao([a_novo][l0][c0]) == "*":
            vizinho_superior = False
            posicoes.append([a_novo,l0,c0])
        else:
                posicoes.append([a_novo,l0,c0])
                vizinho_superior = simula_caminho(mansao,p,a_novo,l0,c0)
        [a_novo] = [a0-1]
        if int(a_novo) < A or [a_novo,l0,c0] in posicoes or [a_novo,l0,c0] in posicoes_fantasmas or mansao([a_novo][l0][c0]) == "*":
            vizinho_inferior = False
            posicoes.append([a_novo,l0,c0])
        else:
                posicoes.append([a_novo,l0,c0])
                vizinho_inferior = simula_caminho(mansao,p,a_novo,l0,c0)
        if vizinho_superior == True:
            return True
        if vizinho_inferior == True:
            return True
        if vizinho_superior == False and vizinho_inferior == False:
            return False
















# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()

#a0, l0, c0 = [int(v) for v in input().split()]
# Simulação do caminho
a0 = 0
l0 = 4
c0 = 16




escapou = simula_caminho(mansao, False, a0, l0, c0)

# Impressão da saída
if escapou == True:
    print("Caminho para saida encontrado com sucesso.")
else:
    print("Nao existe caminho seguro para a saida.")