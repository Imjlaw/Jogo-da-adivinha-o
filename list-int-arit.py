
numeros = input('Digite uma lista de números inteiros separados por espaço: ')
# relembrar -> split = substring
numeros = numeros.split()

numeros = [int(num) for num in numeros]
# relembrar -> sum = soma tudo | len = conta quantidade de elementos na lista
media = sum(numeros) / len(numeros)
# relembrar (dificil esquecer) -> max = maior número
maior_numero = max(numeros)

numeros_pares = sum(1 for num in numeros if num % 2 == 0)

print('Média aritmética:', media)
print('Maior número:', maior_numero)
print('Quantidade de números pares:', numeros_pares)