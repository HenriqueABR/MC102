###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Investimento em Renda Fixa
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# leitura de dados
M = int(input())
D = int(input())
JP1 = int(input())
JTN1 = int(input())
JP = float((JP1)/100)
JTN = float((JTN1)/100)

# cálculo dos rendimentos
jurostesouro = (M * JTN)
if D<=180:
    IR = float(0.225*jurostesouro)
else:
    if D>180 and D<=360:
        IR = float(0.2*jurostesouro)
    else: 
        if D>360 and D<=720:
            IR = float(0.175*jurostesouro)
        else:
            IR = float(0.15*jurostesouro)
poupanca = M * JP
tesouro = (jurostesouro - IR)

# Impressão da saída
print("Rendimento poupança: {:.2f}".format(poupanca))
print("Rendimento tesouro: {:.2f}".format(tesouro))

if poupanca > tesouro:
	print("Maior rendimento: poupança")
else:
	print("Maior rendimento: tesouro")