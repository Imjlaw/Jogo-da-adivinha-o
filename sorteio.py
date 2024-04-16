from random import choice, shuffle

a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))

a11 = str(input('Nome do primeiro aluno: '))
a22 = str(input('Nome do segundo aluno: '))
a33 = str(input('Nome do terceiro aluno: '))
a44 = str(input('Nome do quarto aluno: '))
lista1 = [a11, a22, a33, a44]
shuffle(lista1)

print('A ordem de apresentação será ')
print(lista1)