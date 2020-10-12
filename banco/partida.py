import random
from .jogador import criar_jogadores
from .propriedade import criar_propriedades
from .tabuleiro import Tabuleiro
import logging


class Dado:
    @classmethod
    def sortear(self):
        return random.randint(1, 6)

class Partida:
    def __init__(self, num_jogador=4, num_propriedades=20, qtd_rodadas=50):
        self.tabuleiro = Tabuleiro(num_jogador, num_propriedades)
        self.executando = False
        self.qtd_rodadas = qtd_rodadas
        self.rodada = 0

    def iniciar(self):
        self.executando = True

    def terminou(self):
        return not self.executando

    def ganhador(self):
        ativos = self.tabuleiro.jogadores_ativos()
        if len(ativos) == 1:
            return ativos[0]
        if self.rodada > self.qtd_rodadas:
            return max(ativos, key=lambda j: j.saldo)

        return None

    def jogar_rodada(self):
        self.rodada += 1
        jogadores_ativos = self.tabuleiro.jogadores_ativos()

        if len(jogadores_ativos) == 1 or self.rodada > self.qtd_rodadas:
            self.executando = False
            logging.info("***Temos um vencedor ***")
            logging.info(self.ganhador())
            return

        logging.info("*** Rodada {0}".format(self.rodada))
        for jogador in jogadores_ativos:
            self.fazer_jogada(jogador)
            

    def fazer_jogada(self, jogador):

        pos, acumular_saldo = self.proxima_pos(jogador)
        jogador.andar(pos)

        if acumular_saldo:
            jogador.creditar(100)

        propriedade = self.tabuleiro.obter_propriedade(pos)
        if not propriedade.possui_proprietario():
            if jogador.comprar(propriedade.aluguel, propriedade.custo_venda):
                jogador.debitar(propriedade.custo_venda)
                propriedade.adicionar_proprietario(jogador)
                logging.info("{0} comprou p# {1}".format(jogador.nome, pos))
            else:
                logging.info("{0} NAO comprou p# {1}".format(jogador.nome, pos))
        else:
            if propriedade.proprietario and propriedade.proprietario != jogador:
                jogador.debitar(propriedade.aluguel)
                propriedade.proprietario.creditar(propriedade.aluguel)
                logging.info("{0} alugou p# {1}".format(jogador.nome, pos))
                if not jogador.ativo:
                    logging.info("{0} foi excluido da partida".format(jogador.nome))
                    self.tabuleiro.liberar_propriedades(jogador)
            else:
                logging.info("{0} ficou p# {1}".format(jogador.nome, pos))

    def proxima_pos(self, jogador):
        acumular_saldo = False

        numero = Dado.sortear()
        if jogador.pos + numero > self.tabuleiro.quantidade_propriedades - 1:
            pos = jogador.pos + numero - self.tabuleiro.quantidade_propriedades
            acumular_saldo = True
        else:
            pos = jogador.pos + numero

        return pos, acumular_saldo

