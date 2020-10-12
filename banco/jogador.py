import random


class Jogador:
    '''
    Define um jogador com saldo, status, posicao e nome.
    '''

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

    def __repr__(self):
        return '<Jogador {0} a?:{1} p#:{2} s#:{3}>'.format(self.nome, self.ativo, self.pos, self.saldo)


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
        return self.random_choice()

    def random_choice(self):
        return random.choice([False, True])    


def criar_jogadores(num_jogadores):
    return (JogadorImpulsivo(),
            JogadorExigente(),
            JogadorCauteloso(),
            JogadorAleatorio())[:num_jogadores]
