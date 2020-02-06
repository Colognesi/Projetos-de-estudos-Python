import random

'''
Adicionado aleatoriedade no numero
Adicionado niveis de dificuldade, quanto mais facil mais tentativas || Aula 7 projeto 1
'''

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

rodada = 1
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número de 1 a 100: ")
    print("voce digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto

    if (acertou):
        print("Voce acertou!")
        break
    else:
        if(maior):
            print("Seu chute e maior que o numero secreto")
        elif(menor):
            print("Seu chute e menor que o numero secreto")

print("Fim do jogo")