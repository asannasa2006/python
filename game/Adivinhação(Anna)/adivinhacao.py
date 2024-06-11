print("**************************************")
print("Olá. Bem-vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto1 = 42
total_de_tentativas= 3
rodada = 1


while (rodada <= total_de_tentativas):
    print("\nTentativas:",  total_de_tentativas)
    chute_str = input("\nDigite um número: ",) #dara um erro, pois ao chute é tipo string (por causa do input) e o numero_screto1 é int.
    chute_str = int(chute_str) #converção de string para int.

    print( "\nVocê propos o numero: ", chute_str )

    acertou = chute_str == numero_secreto1
    maior = chute_str > numero_secreto1
    menor = chute_str < numero_secreto1

    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    total_de_tentativas = total_de_tentativas - 1

print("\nSuas tentativas acabou!")
print ("\nFim de jogo ************") # \n é um comando para pular linha.