import forca
import adivinhacao

'''
Arquivo utilizado para chamar os jogos!
'''

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo? "))

if (jogo == 1):
    print("Jogando Forca!")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhacao!")
    adivinhacao.jogar()