
peso = float(input('Insira o seu peso em KG: '))
altura = float(input('Insira a sua altura: '))


imc = peso / altura **2

print('Seu IMC é igual a: {:.2f}'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obeso')


