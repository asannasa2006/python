import random

def jogar():
    print("**************************************")
    print("Olá. Bem-vindo ao jogo de Adivinhação!")
    print("**************************************")

    numero_secreto1 = random.randrange(1, 101)
    total_de_tentativas= 0
    pontos= 100

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("\nDigite um número entre 1 e 100: ",) #dara um erro, pois ao chute é tipo string (por causa do input) e o numero_screto1 é int.
        chute_str = int(chute_str) #converção de string para int.

        print( "\nVocê propos o numero: ", chute_str )

        if (chute_str < 1 or chute_str > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute_str == numero_secreto1
        maior = chute_str > numero_secreto1
        menor = chute_str < numero_secreto1

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto1 - chute_str)
            pontos = pontos - pontos_perdidos


        total_de_tentativas = total_de_tentativas - 1

    print("\nSuas tentativas acabou!")
    print ("\nFim de jogo ************") # \n é um comando para pular linha.

if (__name__ == "__main__"):
    jogar()