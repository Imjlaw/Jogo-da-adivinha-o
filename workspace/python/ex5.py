# Soma do número 1 a N

def soma_ate_n(n):
    soma = (0)
    for i in range(1, n+1):
        soma += i
    return soma

numero = int(input("Digite um número inteiro: "))
resultado = soma_ate_n(numero)
print("A soma dos números de 1 até,", numero, "é:", resultado)