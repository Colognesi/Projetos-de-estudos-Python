'''
Adicionada uma funcao para chamar o jogo.
Adicionado permissao para que o jogo seja chamado diretamente tambem com a __name__
Jogo sera iniciado no curso de Python 2
'''
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not acertou and not enforcou):

        chute = input("Qual a letra? ")

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posicao {}".format(letra, index))
            index += 1

        print("Jogando...")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
