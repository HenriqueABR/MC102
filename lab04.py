###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Batalha Pokémon
# Nome: Henrique Allan Borges Ribeiro
# RA: 261100
###################################################

# Leitura do hp e velocidade dos pokémons
HPIvy = int(input())
HPPika = int(input())
SPDIvy = int(input())
SPDPika = int(input())

# Leitura dos ataques dos turnos
if SPDIvy > SPDPika:
    while HPIvy > 0 and HPPika > 0:
        HPPika = HPPika - int(float(input())*float(input()))
        if HPPika <= 0:
            PokemonVencedor = "Ivysaur"
            HPPokemonVencedor = HPIvy
            HPPika = 0
            break
        HPIvy = HPIvy - int(float(input())*float(input()))
        if HPIvy <= 0:
            PokemonVencedor = "Pikachu"
            HPPokemonVencedor = HPPika
            HPIvy = 0
            break
        print("HP Ivysaur = {:.0f}".format(HPIvy))
        print("HP Pikachu = {:.0f}".format(HPPika))
    print("HP Ivysaur = {:.0f}".format(HPIvy))
    print("HP Pikachu = {:.0f}".format(HPPika))

if SPDPika > SPDIvy:
    while HPIvy > 0 and HPPika > 0:
        HPIvy = HPIvy - int(float(input())*float(input()))
        if HPIvy <= 0:
            PokemonVencedor = "Pikachu"
            HPPokemonVencedor = HPPika
            HPIvy = 0
            break
        HPPika = HPPika - int(float(input())*float(input()))
        if HPPika <= 0:
            PokemonVencedor = "Ivysaur"
            HPPokemonVencedor = HPIvy
            HPPika = 0
            break
        print("HP Ivysaur = {:.0f}".format(HPIvy))
        print("HP Pikachu = {:.0f}".format(HPPika))
    print("HP Ivysaur = {:.0f}".format(HPIvy))
    print("HP Pikachu = {:.0f}".format(HPPika))

# Impressão do vencedor
if PokemonVencedor == "Ivysaur":
    print("Pokémon Vencedor: Ivysaur")
if PokemonVencedor == "Pikachu":
    print("Pokémon Vencedor: Pikachu")

print("HP do Vencedor: {:.0f}".format(HPPokemonVencedor))
