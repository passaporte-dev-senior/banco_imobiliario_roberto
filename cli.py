import logging
from banco.partida import Partida


def jogar():
    partida = Partida()

    partida.iniciar()
    while not partida.terminou():
        partida.jogar_rodada()


if __name__ == "__main__":
    FORMAT = "%(message)s"
    logging.basicConfig(
        filename="banco_imobiliario.log", level=logging.DEBUG, format=FORMAT
    )
    jogar()
