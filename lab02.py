###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Um Lanche Antes da Aula
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura da entrada
T = int(input())
L1 = int(input())
L2 = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())
T1 = P1 + P2 + T
T2 = T + P3
C1 = 12 + L1
C2 = 6 + L2

# Comparação entre as opções e impressão da saída
if T1<=45 and T2<=45 and C1<=C2:
    print (True)
else:
    if T1<=45 and T2>45:
        print (True)
    else:
        if T2<=45 and T1>45:
            print (False)
        else:  
            if T1>45 and T2>45 and T1<=T2:
                print (True)
            else:
                print (False)