n = int(input("Insira um número para verificarmos se ele é primo ou não: "))

def verificar_primo(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
if verificar_primo(n):
    print("O número é primo")
else:
    print("O número não é primo")
