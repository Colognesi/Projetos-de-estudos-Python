def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ['_', '_', '_', '_', '_',
                        '_']  # adicionada lista para poder saber onde estao as letras acertadas
    letras_faltando = str(letras_acertadas.count("_"))
    print("Ainda faltam {} letras".format(letras_faltando))
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()  # Strip utilizado para remover espacos em branco caso digitados, upper para manter sempre em caixa alta
        index = 0  # utilizado para armazenar o espaço da letra chute
        for letra in palavra_secreta:

            if (chute.upper() == letra.upper()):  # usado para captar o chute ele sendo maiusculo ou minusculo
                letras_acertadas[index] = letra  # ajuda a armazenar a letra correta em sua posição
            index += 1
        else:
            erros += 1
            print("Ops você errou! faltam {} tentativas.".format(6 - erros))

            enforcou = erros == 6
            acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        print("Jogando...")

    if (acertou):
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
