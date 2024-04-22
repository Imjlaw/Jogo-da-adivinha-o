nome = input('Digite o seu nome completo: ')
separa = nome.split()
print("""
Analisando o seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome tem {} letras e ele é {}
      """.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(' '), separa[0], len(separa[0])))