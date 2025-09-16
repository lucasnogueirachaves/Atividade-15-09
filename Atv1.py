class Curupira:
    altura = 1.50
    poder = "Controlar fogo"
    maturidade = 50
    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade

ronaldo = Curupira("Ronaldo", 10)

print(ronaldo.velocidade)