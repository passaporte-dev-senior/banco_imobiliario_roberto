import random
from jogador import criar_jogadores
from propriedade import criar_propriedades
import logging


class Dado:
    @classmethod
    def sortear(self):
        return random.randint(1, 6)


class Tabuleiro:
    def __init__(self, jogadores, propriedades):
        self.jogadores = jogadores
        self.propriedades = propriedades

    def propriedade(self, pos):
        return self.propriedades[pos]

    def jogadores_ativos(self):
        return [j for j in self.jogadores if j.ativo]

    def liberar_propriedades(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.remover_proprietario()


class Partida:
    def __init__(self):
        self.executando = False
        self.rodada = 0
        self.tabuleiro = Tabuleiro(criar_jogadores(),
                                   criar_propriedades())

    def iniciar(self):
        self.executando = True

    def terminou(self):
        return not self.executando

    def ganhador(self):
        ativos = self.tabuleiro.jogadores_ativos()
        if len(ativos) == 1:
            return ativos[0]
        if self.rodada > 50:
            return ativos[0]

        return None

    def jogar_rodada(self):

        if len(self.tabuleiro.jogadores_ativos()) == 1:
            logging.info("***Temos um vencedor ***")
            logging.info(self.ganhador())
            self.executando = False
            return

        self.rodada += 1
        if self.rodada > 50:
            self.executando = False
            logging.info("***Temos um vencedor ***")
            logging.info(self.ganhador())
            return

        for jogador in self.tabuleiro.jogadores:
            if jogador.ativo:
                self.jogar(jogador)
            logging.info("{0}: {1}".format(self.rodada, jogador))

    def jogar(self, jogador):

        pos, acumular_saldo = self.proxima_pos(jogador)
        if acumular_saldo:
            jogador.saldo += 100

        propriedade = self.tabuleiro.propriedade(pos)
        if propriedade.proprietario is None:
            if jogador.comprar(propriedade.aluguel, propriedade.custo_venda):
                jogador.debitar(propriedade.custo_venda)
                propriedade.adicionar_proprietario(jogador)
        else:
            jogador.debitar(propriedade.aluguel)
            propriedade.proprietario.creditar(propriedade.aluguel)
            if not jogador.ativo:
                self.tabuleiro.liberar_propriedades(jogador)

        jogador.andar(pos)

    def proxima_pos(self, jogador):
        acumular_saldo = False

        numero = Dado.sortear()
        if jogador.pos + numero >= 20:
            pos = jogador.pos + numero - 20
            acumular_saldo = True
        else:
            pos = jogador.pos + numero

        return pos, acumular_saldo