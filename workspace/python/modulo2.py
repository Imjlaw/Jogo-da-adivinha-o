#Estruturas Condicionais, As estruturas condicionais permitem que o programa tome decisões com base em condições específicas. Em Python, usamos if, elif e else para isso.

idade = int(input("Digite a sua idade"))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

#Loops, os loops são usados para executar um bloco de código várias vezes. Em Python, temos os loops for e while.
    
# Loop usando for
for i in range(5):
    print(i)

# Loop usando while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#Funções, As funções são blocos de código que realizam uma tarefa específica e podem ser reutilizadas em diferentes partes do programa.
    
def saudacao(nome):
    print("Olá,", nome, "! Como você está?")

saudacao("João")