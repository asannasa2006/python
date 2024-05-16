#Aula 1

print ("Hello World!")
print ( "Brasil ganhou 5 copas do mundo")
print ("Brasil", "ganhou", 5,"copas do mundo" , sep="-")
# o sep define oque tera entre os valores definidos 
# sep="-" printara - a cada valor
print ("Brasil", "ganhou", 5,"copas do mundo" , end=".\n")
# o end printa ao final dos valores.

pais = "Italia"
#para atribuir variavel basta adicionar o nome = valor

type(pais)
#questinar qual o tipo de variavel foi atribuida 
#"CLASS STR (string)"

quantidade = 4
type(quantidade)
#"CLASS INT (inteiro)"

print (pais, "ganhou", quantidade, "títulos mundiais.") 
#printar valores basta colocar o nome dado a variavel
# pode printar strings sem declararas como variaveis


#Aula 2

paiss = "Brasil"
paiss = 644
# redefini o valor da variável de Brasil para 644

type(paiss)
# <class 'int'>

paiss = 7.9

type(paiss)
#class 'float'>
