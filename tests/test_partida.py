import pytest
from banco.partida import Partida, Dado


def test_dado_seed():
    dado = Dado()
    numero = dado.sortear()
    assert 0 < numero <= 6


def test_partida_init():
    partida_01 = Partida()
    assert not partida_01.tabuleiro is None
    assert not partida_01.executando
    assert partida_01.rodada == 0


def test_partida_iniciar():
    partida_01 = Partida()
    assert not partida_01.executando
    partida_01.iniciar()
    assert partida_01.executando
    assert not partida_01.terminou()


def test_partida_vencedor_esgotou_rodadas():
    partida_01 = Partida(qtd_jogadores=2, qtd_propriedades=6, qtd_rodadas=1)
    assert partida_01.vencedor() is None
    partida_01.iniciar()
    partida_01.jogar_rodada()
    partida_01.jogar_rodada()
    assert not partida_01.vencedor() is None


def test_partida_vencedor_sobrou_um():
    dado = Dado(1, 1)
    partida_01 = Partida(qtd_jogadores=2, qtd_propriedades=2, qtd_rodadas=1, dado=dado)
    assert partida_01.vencedor() is None
    partida_01.iniciar()
    partida_01.jogar_rodada()
    partida_01.jogar_rodada()
    assert not partida_01.vencedor() is None


def test_partida_jogar_rodada():
    partida_01 = Partida()
    partida_01.iniciar()
    partida_01.jogar_rodada()
    assert partida_01.rodada == 1


@pytest.mark.parametrize(
    "pos_atual,total_pos,numero,expected",
    [(0, 10, 2, (2, False)), (8, 10, 2, (0, True))],
)
def test_proxima_pos(pos_atual, total_pos, numero, expected):
    partida_01 = Partida()
    assert partida_01.proxima_pos(pos_atual, total_pos, numero) == expected


def test_fazer_jogada():
    # fazer_jogada(self, jogador, numero):
    #  self.tabuleiro.qtd_propriedades
    #  self.tabuleiro.qtd_propriedades
    pass