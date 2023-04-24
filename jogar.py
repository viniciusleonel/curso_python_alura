import forca
import adivinhacao

def jogar():
    print("********Escolha******")
    print("**********um*********")
    print("*********Jogo********\n")

    while True:
        print("Você quer jogar \n(1) Adivinhação\n(2) Forca\n(3) Nenhum")
        jogo = int(input())
        if jogo == 1:
            adivinhacao.jogar()
            break
        elif jogo == 2:
            forca.jogar()
            break
        elif jogo == 3:
            print("Fim de Jogo!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    jogar()
