print("**************************************")
print("Olá. Bem vindo ao jogo de Adivinhação!")
print("**************************************")

numero_secreto1 = 42

chute = input("Digite um número: ", chute_str)
chute = int(chute_str)

print( " Você propos o numero", chute )

if (numero_secreto1 == chute):
    print("E você acerto, Parabéns!")
#para atribuir condições dentro do if/else é necessário ter 4 espaços ou 1 tab

else:
    print( "E você errou, tente novamente.")

#dara um erro, pois ao chute é tipo string (por causa do input) e o numero_screto1 é int
