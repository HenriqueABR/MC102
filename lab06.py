###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Nota de MC102
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura de dados
N = int(input())
Notas_Testes = []
Pesos_Testes = []
for X in range (N):
    Notas_Testes.append(float(input()))
for Y in range (N):
    Pesos_Testes.append(float(input()))

# Cálculo da média ponderada dos laboratórios
Notas_com_pesos = []
for Z in range (N):
    Notas = Notas_Testes[Z]*Pesos_Testes[Z]
    Notas_com_pesos.append(Notas)
media = 0
Peso_Total = 0
for K in range (N):
    media = (media + Notas_com_pesos[K])
    Peso_Total = Peso_Total + Pesos_Testes[K]
media = media/Peso_Total


print("Media laboratorios:", format(media, ".1f").replace(".", ","))


# Verificação da situação do aluno
print (Pesos_Testes)
if media >= 5 or media < 2.5:
    nota_final = media  
    if media >= 5:
        situacao = 0
    else:
        situacao = 1
else:
    M = int(input())
    Numero_Lab = []
    for J in range (M):
        Numero_Lab.append(int(input()))
    print (Numero_Lab)
    Notas_Exame = []
    for J in range (M):
        Notas_Exame.append(float(input()))

    Notas_com_peso_exame = []
    for J in range (M):
        Notas_com_peso_exame1 = Pesos_Testes[Numero_Lab[J]-1]*Notas_Exame[J]
        Notas_com_peso_exame.append(Notas_com_peso_exame1)
    media_final = 0
    Peso_total1 = 0
    for J in range (M):
        media_final = media_final + Notas_com_peso_exame[J]
        Peso_total1 = Peso_total1 + Pesos_Testes[Numero_Lab[J]-1]
    Nota_final_exame = media_final/Peso_total1
    nota_final = min(5, (media + Nota_final_exame)/2)
    if (media + Nota_final_exame)/2 < 5:
        situacao = 2
    else:
        situacao = 3

# Caso o aluno tenha sido aprovado por nota
if situacao == 0:
    print("Situacao: Aprovado por nota")

# Caso o aluno tenha sido reprovado por nota
if situacao == 1:
    print("Situacao: Reprovado por nota")

# Caso o aluno tenha sido aprovado no exame
if situacao == 3:
    print("Situacao: Aprovado no exame")

# Caso o aluno tenha sido repravado no exame
if situacao == 2:
    print("Situacao: Reprovado no exame")

# Saída de dados

print("Nota final:", format(nota_final, ".1f").replace(".", ","))