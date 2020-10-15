import random
from .tabuleiro import Tabuleiro
import logging


class Dado:
    def __init__(self, start=1, end=6):
        self.start = start
        self.end = end

    def sortear(self):
        return random.randint(self.start, self.end)


class Partida:
    def __init__(self, qtd_jogadores=4, qtd_propriedades=20, qtd_rodadas=50, dado=None):
        self.tabuleiro = Tabuleiro(qtd_jogadores, qtd_propriedades)
        self.executando = False
        self.qtd_rodadas = qtd_rodadas
        self.rodada = 0
        if not dado:
            dado = Dado()
        self.dado = dado

    def iniciar(self):
        self.executando = True

    def terminou(self):
        return not self.executando

    def vencedor(self):
        nome_vencedor = None
        ativos = self.tabuleiro.jogadores_ativos()
        if len(ativos) == 1:
            nome_vencedor = ativos[0]
        if self.rodada > self.qtd_rodadas:
            nome_vencedor = max(ativos, key=lambda j: j.saldo)

        return nome_vencedor.nome if nome_vencedor else None

    def jogar_rodada(self):
        self.rodada += 1
        jogadores_ativos = self.tabuleiro.jogadores_ativos()

        logging.info("*** Rodada {0}".format(self.rodada))
        for jogador in jogadores_ativos:
            self.fazer_jogada(jogador, self.dado.sortear())

        if self.vencedor():
            self.executando = False
            logging.info("***Temos um vencedor ***")
            logging.info(self.vencedor())
            return

    def proxima_pos(self, pos_atual, total_pos, numero):
        acumular_saldo = False
        if pos_atual + numero > total_pos - 1:
            pos = pos_atual + numero - total_pos
            acumular_saldo = True
        else:
            pos = pos_atual + numero

        return pos, acumular_saldo

    def fazer_jogada(self, jogador, numero):
        pos, acumular_saldo = self.proxima_pos(
            jogador.pos, self.tabuleiro.qtd_propriedades, numero
        )
        jogador.andar_para(pos)

        if acumular_saldo:
            jogador.creditar(100)

        propriedade = self.tabuleiro.obter_propriedade(pos)
        if propriedade.proprietario == jogador:
            return

        if not propriedade.possui_proprietario():
            if jogador.comprar(propriedade.aluguel, propriedade.custo_venda):
                jogador.debitar(propriedade.custo_venda)
                propriedade.adicionar_proprietario(jogador)
                logging.info("{0} comprou p# {1}".format(jogador.nome, pos))
            else:
                logging.info("{0} NAO comprou p# {1}".format(jogador.nome, pos))
        else:
            jogador.debitar(propriedade.aluguel)
            propriedade.proprietario.creditar(propriedade.aluguel)
            logging.info("{0} alugou p# {1}".format(jogador.nome, pos))
            if not jogador.ativo:
                logging.info("{0} foi excluido da partida".format(jogador.nome))
                self.tabuleiro.liberar_propriedades(jogador)
