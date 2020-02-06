#Codigo realizado até a aula 4 do módulo 1 sobre laços de repetição
#Adicionado variável total_de_tentativas e rodada

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

total_de_tetativas = 3
rodada = 1
numero_secreto = 42

while(rodada <= total_de_tetativas):
    print("Tentativa {} de {}".format(rodada, total_de_tetativas))

    chute_str = input("Digite seu numero: ")
    print("voce digitou: ", chute_str)
    chute = int(chute_str)

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto

    if (acertou):
        print("Voce acertou!")
    else:
        if(maior):
            print("Seu chute e maior que o numero secreto")
        elif(menor):
            print("Seu chute e menor que o numero secreto")

            rodada +=1

    print("Fim do jogo")