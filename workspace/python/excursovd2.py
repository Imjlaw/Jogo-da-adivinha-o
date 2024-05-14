a = int(input("Qual o preço do produto? R$"))

print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${}.".format(a, a - (a*5/100)))

s = float(input("Qual é o seu salário? R$"))

print("O seu salário com 15% e aumento será R${}".format(s + (s*15/100)))

t = float(input("Digite a temperatura em graus C: "))
print("A temperatura de {}°C corresponde a {}°F!".format(t, (t*9/5) + 32))