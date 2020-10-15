import random


class Jogador:
    """
    Define um jogador com saldo, status, posicao e nome.
    """

    def __init__(self):
        self.saldo = 300
        self.pos = 0
        self.nome = ""

    def andar_para(self, pos):
        self.pos = pos

    def debitar(self, valor):
        self.saldo = self.saldo - valor

    def creditar(self, valor):
        self.saldo = self.saldo + valor

    def possui_saldo_suficiente(self, custo_venda):
        return self.saldo >= custo_venda

    @property
    def ativo(self):
        return self.saldo > 0

    def __repr__(self):
        return "<Jogador {0} a?:{1} p#:{2} s#:{3}>".format(
            self.nome, self.ativo, self.pos, self.saldo
        )


class JogadorImpulsivo(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = "Impulsivo"

    def comprar(self, aluguel, custo_venda):
        if not self.possui_saldo_suficiente(custo_venda):
            return False
        return True


class JogadorExigente(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = "Exigente"

    def comprar(self, aluguel, custo_venda):
        if not self.possui_saldo_suficiente(custo_venda):
            return False
        return aluguel > 50


class JogadorCauteloso(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = "Cauteloso"

    def comprar(self, aluguel, custo_venda):
        if not self.possui_saldo_suficiente(custo_venda):
            return False
        return (self.saldo - custo_venda) > 80


class JogadorAleatorio(Jogador):
    def __init__(self):
        super().__init__()
        self.nome = "Aleatorio"

    def comprar(self, aluguel, custo_venda):
        if not self.possui_saldo_suficiente(custo_venda):
            return False
        return self.random_choice()

    def random_choice(self):
        return random.choice([False, True])


def criar_jogadores(num_jogadores):
    return (
        JogadorImpulsivo(),
        JogadorExigente(),
        JogadorCauteloso(),
        JogadorAleatorio(),
    )[:num_jogadores]
