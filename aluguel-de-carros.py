d = int(input('Quantos dias alugados? '))
k = float(input('Quantos KM rodados? '))
total = (d * 60) + (k * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))