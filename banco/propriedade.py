import random


class Propriedade:
    """
    Define uma propriedade com proprietario, aluguel e custo de venda.
    """

    def __init__(self):
        self.proprietario = None
        self.aluguel = random.choice([40, 50, 60])
        self.custo_venda = random.choice([80, 100])

    def remover_proprietario(self):
        self.proprietario = None

    def adicionar_proprietario(self, jogador):
        self.proprietario = jogador

    def possui_proprietario(self):
        return not self.proprietario is None

    @property
    def nome_proprietario(self):
        return self.proprietario.nome if self.proprietario else "-"

    def __repr__(self):
        return "<Propriedade p:{0} a#:{1} v#:{2}>".format(
            self.nome_proprietario, self.aluguel, self.custo_venda
        )


def criar_propriedades(n):
    return [Propriedade() for n in range(n)]
