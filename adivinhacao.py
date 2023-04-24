import random

def jogar():
    print("*********Jogo*********")
    print("**********da**********")
    print("*****Adivinhação******\n")

    pontos = 1000
    numero_secreto = round(random.randrange(1, 101))
    facil = 20
    medio = 10
    dificil = 5

    def iniciar_jogo(level, pontos, numero_secreto):
        for i in range(1, level + 1):
            chute = int(input("\nDigite um número de 1 a 100: \n"))
            if chute == 0 or chute > 100:
                print("Chute inválido, digite um número entre 1 e 100, tentativa {} de {}".format(i, level))
            elif i == level:
                print("\nVocê perdeu! O número era {}\nFim de Jogo".format(numero_secreto))
                break
            elif chute > numero_secreto:
                print("Você errou, seu chute foi maior que o número, tentativa {} de {}".format(i, level))
                perdeu_pontos = abs(chute - numero_secreto)
                pontos = pontos - perdeu_pontos
            elif chute < numero_secreto:
                print("Você errou,  seu chute foi menor que o número, tentativa {} de {}".format(i, level))
                perdeu_pontos = abs(chute - numero_secreto)
                pontos = pontos - perdeu_pontos
            else:
                print("Você acertou o número {}, você fez {} pontos".format(numero_secreto, pontos))
                print("Fim de Jogo")
                break

    while True:
        print("Em qual level deseja jogar?")
        print("(1)Fácil (2)Médio (3)Difícil")
        level = int(input())
        if level != 1 and level != 2 and level != 3:
            print("Level não existe")
        elif level == 1:
            iniciar_jogo(facil, pontos, numero_secreto)
            break
        elif level == 2:
            iniciar_jogo(medio, pontos, numero_secreto)
            break
        elif level == 3:
            iniciar_jogo(dificil, pontos, numero_secreto)
            break
        else:
            break

if __name__ == "__main__":
    jogar()