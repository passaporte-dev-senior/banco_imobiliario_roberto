import logging
from partida import Partida


def jogar():
    partida = Partida(4, 20)
    
    partida.iniciar()
    logging.info(partida.tabuleiro)
    while not partida.terminou():
        partida.jogar_rodada()
        # logging.info(partida.tabuleiro)


if __name__ == "__main__":
    FORMAT = '%(message)s'
    logging.basicConfig(filename='banco_imobiliario.log', level=logging.DEBUG, format=FORMAT)
    jogar()
