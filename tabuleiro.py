class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, direcao):
        if direcao == "cima":
            self.y -= 1
        elif direcao == "baixo":
            self.y += 1
        elif direcao == "esquerda":
            self.x -= 1
        elif direcao == "direita":
            self.x += 1

class Jogo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.jogador = Jogador(largura // 2, altura // 2)

    def mostrar_tabuleiro(self):
        for y in range(self.altura):
            for x in range(self.largura):
                if x == self.jogador.x and y == self.jogador.y:
                    print("X", end=" ")
                else:
                    print("-", end=" ")
            print()

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            direcao = input("Para onde deseja mover? (cima/baixo/esquerda/direita): ").lower()
            if direcao in ["cima", "baixo", "esquerda", "direita"]:
                self.jogador.mover(direcao)
            else:
                print("Direção inválida! Por favor, escolha entre cima, baixo, esquerda ou direita.")

if __name__ == "__main__":
    largura = 10
    altura = 10
    jogo = Jogo(largura, altura)
    jogo.jogar()
