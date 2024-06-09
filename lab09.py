###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Criptografia Cíclica
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura da entrada
P = list(input())
frase = list(input())

# Decodificação da mensagem
for X in range(0, len(frase)):
    for Y in range(0, len(P)-1):
        if frase[X] == P[Y]:
            if Y == 0:
                frase[X] = P[-1]
            if Y > 0:
                frase[X] = P[Y-1]
        if frase[X] == (P[Y]).upper():
            if Y == 0:
                frase[X] = P[-1].upper()
            if Y > 0:
                frase[X] = P[Y-1].upper()
        else:
            frase[X] = frase[X]
final = ''.join(frase)

# Impressão da saída
print(final)