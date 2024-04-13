print('Olá! seja bem vindo ao conversor de graus Celsius para Fahrenheint!')

escolha = input('Você deseja fazer a conversão de qual temperatura? (c = Celsius / f = Fahrenheint): ')

if escolha == 'c':
    celsius = float(input('Digite o número de graus Celsius que deseja converter: '))
    fahrenheint = celsius * 9/5 + 32
    print('O número de graus Celsius em Fahrenheint é igual a:', fahrenheint)
elif escolha == 'f':
    fahrenheint = float(input('Digite o número de graus Fahrenheint que deseja converter: '))
    celsius = ( fahrenheint - 32) * 5/9
    print('O número de graus Fahrenheint em Celsius é igual a:', celsius)
else:
    print('Escolha inválida. Por favor, escolha "c" para Celsius ou "f" para Fahrenheint.') 