import random


class Jogador:
    def __init__(self):
        self.saldo = 300
        self.ativo = True
        self.pos = 0
        self.nome = ''

    def eliminar(self):
        self.ativo = False

    def andar(self, pos):
        self.pos = pos

    def debitar(self, valor):
        self.saldo = self.saldo - valor
        if self.saldo < 0:
            self.eliminar()

    def creditar(self, valor):
        self.saldo = self.saldo + valor

    def __str__(self):
        return '[{0} ({1}) p:{2} s:{3}]'.format(self.nome, self.ativo, self.pos, self.saldo)


class JogadorImpulsivo(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = 'Impulsivo'

    def comprar(self, aluguel, custo_venda):
        return True


class JogadorExigente(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = 'Exigente'

    def comprar(self, aluguel, custo_venda):
        return aluguel > 50


class JogadorCauteloso(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = 'Cauteloso'

    def comprar(self, aluguel, custo_venda):
        return (self.saldo - custo_venda) > 80


class JogadorAleatorio(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = 'Aleatorio'

    def comprar(self, aluguel, custo_venda):
        return random.choice([False, True])


def criar_jogadores():
    return [JogadorImpulsivo(),
            JogadorExigente(),
            JogadorCauteloso(),
            JogadorAleatorio()]
