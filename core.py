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
        lst = []
        for jogador in self.jogadores:
            if jogador.ativo:
                lst.append(jogador)

        return lst


class Partida:
    def __init__(self):
        self.executando = False
        self.rodada = 0
        self.tabuleiro = Tabuleiro(criar_jogadores(),
                                   criar_propriedades())

    def iniciar(self):
        self.executando = True

    def jogar_rodada(self):

        if len(self.tabuleiro.jogadores_ativos()) == 1:
            logging.info("***Temos um vencedor ***")
            logging.info(self.tabuleiro.jogadores_ativos()[0])
            self.executando = False
            return

        self.rodada += 1
        if self.rodada > 50:
            self.executando = False
            return

        for jogador in self.tabuleiro.jogadores:
            if jogador.ativo:
                numero = Dado.sortear()
                if jogador.pos + numero >= 20:
                    pos = jogador.pos + numero - 20
                    jogador.saldo += 100
                else:
                    pos = jogador.pos + numero

                propriedade = self.tabuleiro.propriedade(pos)
                if propriedade.proprietario is None:
                    if jogador.comprar(propriedade.aluguel, propriedade.custo_venda):
                        jogador.debitar(propriedade.custo_venda)
                        propriedade.proprietario = jogador
                else:
                    jogador.debitar(propriedade.aluguel)
                    propriedade.proprietario.creditar(propriedade.aluguel)

                jogador.andar(pos)
                logging.info("{0}: {1}".format(self.rodada, jogador))

    def terminou(self):
        return not self.executando


def jogar():
    partida = Partida()
    partida.iniciar()
    while not partida.terminou():
        partida.jogar_rodada()


if __name__ == "__main__":
    logging.basicConfig(filename='banco_imobiliario.log', level=logging.DEBUG)
    jogar()
