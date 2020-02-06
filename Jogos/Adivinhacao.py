'''
Alterado o modo que é utilizado para repetição com for,
adicionado também contador +1 no laço para contablizar 3 tentativas totais.
Adicionado também validação para o tamanho do numero que deve ser digitado
E adicionado Break para terminar a interação caso acerte
'''

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

total_de_tetativas = 3
rodada = 1
numero_secreto = 42

for rodada in range(1, total_de_tetativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tetativas))

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