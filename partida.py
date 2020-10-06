import random
from jogador import criar_jogadores
from propriedade import criar_propriedades
import logging


class Dado:
    @classmethod
    def sortear(self):
        return random.randint(1, 6)


class Tabuleiro:
    def __init__(self):
        QUANTIDADE_PROPRIEDADES = 20
        self.jogadores = criar_jogadores()
        self.propriedades = criar_propriedades(QUANTIDADE_PROPRIEDADES)

    def obter_propriedade(self, pos):
        return self.propriedades[pos]

    def jogadores_ativos(self):
        return [j for j in self.jogadores if j.ativo]

    def liberar_propriedades(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.remover_proprietario()


class Partida:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.executando = False
        self.rodada = 0

    def iniciar(self):
        self.executando = True

    def terminou(self):
        return not self.executando

    def ganhador(self):
        ativos = self.tabuleiro.jogadores_ativos()
        if len(ativos) == 1:
            return ativos[0]
        if self.rodada > 50:
            return max(ativos, key=lambda j: j.saldo)

        return None

    def jogar_rodada(self):

        self.rodada += 1
        jogadores_ativos = self.tabuleiro.jogadores_ativos()

        if len(jogadores_ativos) == 1 or self.rodada > 50:
            self.executando = False
            logging.info("***Temos um vencedor ***")
            logging.info(self.ganhador())
            return

        for jogador in jogadores_ativos:
            self.fazer_jogada(jogador)
            logging.info("{0}: {1}".format(self.rodada, jogador))

    def fazer_jogada(self, jogador):

        pos, acumular_saldo = self.proxima_pos(jogador)
        jogador.andar(pos)

        if acumular_saldo:
            jogador.creditar(100)

        propriedade = self.tabuleiro.obter_propriedade(pos)
        if propriedade.possui_proprietario():
            if jogador.comprar(propriedade.aluguel, propriedade.custo_venda):
                jogador.debitar(propriedade.custo_venda)
                propriedade.adicionar_proprietario(jogador)
        else:
            jogador.debitar(propriedade.aluguel)
            propriedade.proprietario.creditar(propriedade.aluguel)
            if not jogador.ativo:
                self.tabuleiro.liberar_propriedades(jogador)

    def proxima_pos(self, jogador):
        acumular_saldo = False

        numero = Dado.sortear()
        if jogador.pos + numero >= 20:
            pos = jogador.pos + numero - 20
            acumular_saldo = True
        else:
            pos = jogador.pos + numero

        return pos, acumular_saldo
