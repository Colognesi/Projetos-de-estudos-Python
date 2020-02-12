import random


def jogar():
    imprime_mensagem_inicio()
    palavra_secreta = inicia_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not acertou and not enforcou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        print("Jogando...")

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


print("Fim do jogo")


def imprime_mensagem_inicio():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def inicia_palavra_secreta(nome_arquivo="palavras.txt"):
    with open("palavras.txt", "r") as arquivo:  # funcao with para autofechamento do arquivo mesmo em caso de erros
        palavras = [linha.strip() for linha in arquivo]  # aprendendo a usar List Comprehension!

    numero = random.randrange(0, len(palavras))  # adicionado para randomizar a palavra que vai ser selecionada
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in
            palavra]  # adicionada lista para poder saber onde estao as letras acertadas


def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()  # Strip utilizado para remover espacos em branco caso digitados, upper para
    # manter sempre em caixa alta
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0  # utilizado para armazenar o espaço da letra chute
    for letra in palavra_secreta:

        if chute.upper() == letra.upper():  # usado para captar o chute ele sendo maiusculo ou minusculo
            letras_acertadas[index] = letra  # ajuda a armazenar a letra correta em sua posição
        index += 1


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
