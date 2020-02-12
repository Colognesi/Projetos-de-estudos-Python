import random


def jogar():
    imprime_mensagem_inicio()
    palavra_secreta = inicia_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    # letras_faltantes = captura_letras_faltantes(letras_acertadas) -- ainda nao sei como implementar isso corretamente

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()  # Strip utilizado para remover espacos em branco caso digitados, upper para
        # manter sempre em caixa alta

        if chute in palavra_secreta:

            index = 0  # utilizado para armazenar o espaço da letra chute
            for letra in palavra_secreta:

                if chute.upper() == letra.upper():  # usado para captar o chute ele sendo maiusculo ou minusculo
                    letras_acertadas[index] = letra  # ajuda a armazenar a letra correta em sua posição
                index += 1
        else:
            erros = erros + 1
            print("Ops você errou! faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        # print(letras_faltantes) blagablaga

        print("Jogando...")

    if acertou:
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")


print("Fim do jogo")


def imprime_mensagem_inicio():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def inicia_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:  # funcao with para autofechamento do arquivo mesmo em caso de erros
        palavras = [linha.strip() for linha in arquivo]  # aprendendo a usar List Comprehension!

    numero = random.randrange(0, len(palavras))  # adicionado para randomizar a palavra que vai ser selecionada
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in
            palavra]  # adicionada lista para poder saber onde estao as letras acertadas


'''
def captura_letras_faltantes(letra):
    total_letras = str(letra.count("_"))
    resposta = ("Ainda faltam {} letras".format(total_letras))
    return resposta 
'''

if __name__ == "__main__":
    jogar()
