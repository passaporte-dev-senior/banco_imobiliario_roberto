import random


class Propriedade:
    def __init__(self, n):
        self.proprietario = None
        self.aluguel = random.choice([80, 50, 70, 40])
        self.custo_venda = random.choice([80, 50, 70, 40])


def criar_propriedades():
    lst = []
    for n in range(20):
        lst.append(Propriedade(n))

    return lst
