import logging
from partida import Partida


def jogar():
    partida = Partida()
    partida.iniciar()
    while not partida.terminou():
        partida.jogar_rodada()


if __name__ == "__main__":
    logging.basicConfig(filename='banco_imobiliario.log', level=logging.DEBUG)
    jogar()
