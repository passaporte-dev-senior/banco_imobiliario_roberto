import random


class Propriedade:
    '''
    Define uma propriedade com proprietario, aluguel e custo de venda.
    '''

    def __init__(self):
        self.proprietario = None
        self.aluguel = random.choice([80, 50, 70, 40])
        self.custo_venda = random.choice([80, 50, 70, 40])

    def remover_proprietario(self):
        self.proprietario = None

    def adicionar_proprietario(self, jogador):
        self.proprietario = jogador


def criar_propriedades():
    return [Propriedade() for n in range(20)]
