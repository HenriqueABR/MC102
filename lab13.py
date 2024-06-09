###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Amigos do 495
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura da sequência
numeros = [int(i) for i in input().split()]

# Ordenação dos amigos do 495
iteracoes_lista = []
for X in range(len(numeros)):
    numero_crescente = sorted(str(numeros[X]))
    numero_crescente_str = int("".join(numero_crescente))
    numero_decrescente = [numero_crescente[2],numero_crescente[1],numero_crescente[0]]
    numero_decrescente_str = int("".join(numero_decrescente))
    iteracoes = 0
    numero = 0
    numero_certo = int(495)
        
    while numero != 495:
        numero = numero_decrescente_str - numero_crescente_str

        numero_crescente = sorted(str(numero))
        numero_crescente_str = int("".join(numero_crescente))
        numero_decrescente = [numero_crescente[2],numero_crescente[1],numero_crescente[0]]
        numero_decrescente_str = int("".join(numero_decrescente))

        iteracoes = iteracoes + 1
        if numero == 0:
            break
    iteracoes_lista.append(iteracoes)




    


# Impressão da resposta
conjunto_completo = []
for X in range (len(iteracoes_lista)):
    conjunto = [iteracoes_lista[X], numeros[X]]
    conjunto_completo.append(conjunto)
conjunto_completo.sort()

for X in range (len(conjunto_completo)):
    if X < len(conjunto_completo):
        print(conjunto_completo[X][1], end= " ") 
    else:
        print(conjunto_completo[X][1])
