from jogador import Jogador
from propriedade import Propriedade
from partida import Dado, Tabuleiro


def test_tabuleiro_init():
    tab = Tabuleiro(4, 20)
    assert len(tab.jogadores_ativos()) == 4
    assert len(tab.propriedades) == 20

def test_tabuleiro_obter_propriedade():
    tab = Tabuleiro(4, 20)
    assert not tab.obter_propriedade(0) is None

def test_tabuleiro_liberar_propriedades():
    tab = Tabuleiro(4, 20)
    propriedade = tab.obter_propriedade(0)
    jogador = tab.jogadores_ativos()[0]
    propriedade.adicionar_proprietario(jogador)
    assert propriedade.possui_proprietario()
    tab.liberar_propriedades(jogador)
    assert not propriedade.possui_proprietario()
