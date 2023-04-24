import random

def jogar():

    inicio_forca()
    opcao = seleciona_categoria()
    palavra_secreta = seleciona_palavra_secreta(opcao)

    letras_acertadas = ["_" for letra in palavra_secreta]
    chutes_errados = []

    acertou = False
    enforcou = False
    erros = 6

    print("Adivinhe a palavra secreta: \n")

    while not enforcou and not acertou:
        print(*letras_acertadas, sep=" ")
        nome_categoria(opcao)
        chute = pede_chute()

        if chute in palavra_secreta:
            chute_certo(palavra_secreta, erros, letras_acertadas, chute)
            desenhar_forca(erros)
        elif chute in chutes_errados:
            print("Você já chutou essa letra!\nTENTE NOVAMENTE")
            lista_chutes_errados(chutes_errados)
            desenhar_forca(erros)
            continue
        else:
            erros = chute_errado(erros)
            chutes_errados.append(chute)
            lista_chutes_errados(chutes_errados)
            desenhar_forca(erros)

        acertou = letras_acertadas.count("_") == 0   # outro jeito de escrever: acertou = "_" not in letras_acertadas
        enforcou = erros == 0

    if acertou:
        mensagem_ganhador(palavra_secreta)
    elif enforcou:
        mensagem_perderdor(palavra_secreta)

    print("Fim de jogo")

def inicio_forca():
    print("\n*********Jogo*********")
    print("**********da**********")
    print("*********Forca********\n")

def seleciona_categoria():
    opcao = int(input("Qual categoria você escolhe?\n1-Comidas\n2-Frutas\n3-Legumes\n"))
    return opcao

def nome_categoria(opcao):
    if opcao == 1:
        print("Categoria: Comidas")
    elif opcao == 2:
        print("Categoria: Frutas")
    else:
        print("Categoria: Legumes")

def seleciona_palavra_secreta(opcao):
    lista_palavras = []
    if opcao == 1:
        with open("comidas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                lista_palavras.append(linha)
    elif opcao == 2:
        with open("frutas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                lista_palavras.append(linha)
    elif opcao == 3:
        with open("legumes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                lista_palavras.append(linha)

    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Escreva uma letra: ").strip().upper()
    return chute

def chute_certo(palavra_secreta, erros, letras_acertadas, chute):
    print("Acertou! Chances restantes: {} ".format(erros))
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[index] = chute
        index += 1

def chute_errado(erros):
    print("Errou! Chances restantes: {} ".format(erros - 1))
    erros -= 1
    return erros

def lista_chutes_errados(chutes_errados):
    print("Chutes errados: ", end="")
    print(*chutes_errados, sep=", ")

def mensagem_ganhador(palavra_secreta):
    print("Você acertou a palavra: ")
    print(palavra_secreta)
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

def mensagem_perderdor(palavra_secreta):
    print("Você errou a palavra: ")
    print(palavra_secreta)

def desenhar_forca(erros):
    if erros == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif erros == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif erros == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif erros == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif erros == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|             ")
        print("|             ")
    elif erros == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|     /       ")
        print("|             ")
    elif erros == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|     / \\    ")
        print("|             ")
    else:
        pass

if __name__ == "__main__":
    jogar()
