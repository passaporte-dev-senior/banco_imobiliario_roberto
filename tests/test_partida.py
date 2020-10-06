from jogador import Jogador
from propriedade import Propriedade
from partida import Dado, Tabuleiro


def test_dado_seed():
    numero = Dado.sortear()
    assert 0 < numero <= 6


