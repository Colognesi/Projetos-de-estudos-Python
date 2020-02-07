import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    rodada = 1
    numero_secreto = random.randrange(1, 101)  # Randrange definindo o inicio e fim que o numero secreto pode ter
    total_de_tentativas = 3
    total_de_pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):  # usado para definir o total de rodadas

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número de 1 a 100: ")
        print("voce digitou: ", chute_str)
        chute = int(chute_str)  # o chute é definido a principio como String, sendo convertido para INT nessa linha

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
            if (maior):
                print("Seu chute e maior que o numero secreto")
            elif (menor):
                print("Seu chute e menor que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                total_de_pontos = total_de_pontos - pontos_perdidos
            print("Seu total de pontos é ", total_de_pontos)

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
