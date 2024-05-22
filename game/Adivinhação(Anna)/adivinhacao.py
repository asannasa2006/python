print("**************************************")
print("Olá. Bem-vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto1 = 42

chute_str = input("Digite um número: ",) #dara um erro, pois ao chute é tipo string (por causa do input) e o numero_screto1 é int.
chute_str = int(chute_str) #converção de string para int.

print( "Você propos o numero: ", chute_str )

#if (numero_secreto1 == chute_str):
#    print("E você acerto, Parabéns!")
#else:
#    if (chute_str > numero_secreto1):
#        print( "E você errou. O número proposto é maior que o número secreto.") #para atribuir condições dentro do if/else é necessário ter 4 espaços ou 1 tab.
#    elif (chute_str < numero_secreto1): # o else pode ser usada apenas uma ve dentro do bloco.
#        print( "E você errou. Seu número é menor que o número secreto")

# tudo acima funcionará, mas não será agil)

acertou= chute_str == numero_secreto1



print ("\nFim de jogo ************") # \n é um comando para pular linha.