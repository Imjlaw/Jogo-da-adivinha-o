n = int(input("Digite um número: "))

print("O dobro de {} vale {}.".format(n, (n*2)))
print("O triplo de {} vale {}.".format(n,(n*3)))
print("A raiz quadrada de {} vale {}".format(n,(n** (1/2))))

m = float(input("Quanto de dinheiro vc tem na carteira? R$"))
print("Com R${} vc pode comprar US${}".format(m, (m/5.06)))

p = float(input("Largura da parede: "))
p1 = float(input("Altura da parede: "))
a = p*p1
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m2.".format(p, p1, a))
print("Para pintar essa parede vc vai precisar de {}L de tinta".format(a/2))