import random

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
valor_escolhido:int

print('Qual o nível de dificuldade?')
print('1 - Fácil, 2 - Médio, 3 - Dificil')
nivel = int(input('Digite o nivel: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print(f'Tentavias {rodada} de {total_de_tentativas}')
    valor_escolhido = int(input('Digite um número entre 1 a 100: '))
    print('Você digitou ', valor_escolhido)


    if valor_escolhido < 1 or valor_escolhido > 100:
        print('Número inválido. o número deve ser entre 1 e 100')
        continue
    acertou = valor_escolhido == numero_secreto
    maior = valor_escolhido > numero_secreto
    menor = valor_escolhido < numero_secreto

    if valor_escolhido == numero_secreto:
        print('Parabéns você acertou o número secreto!')
        break
    else:
        if valor_escolhido < numero_secreto:
            print('O número secreto é maior.')
        else:
            print('O número secreto é menor.')

    # Dicas
    distancia = abs(numero_secreto - valor_escolhido)
    if distancia <= 10:
        print('Você está muito próximo!')
    elif distancia <= 25:
        print('Você está próximo!')
    elif distancia <= 50:
        print('Vocês está longezinho!')
    else:
        print('Você está longe!')

print('O número secreto era:', numero_secreto)
print('Fim do jogo!')