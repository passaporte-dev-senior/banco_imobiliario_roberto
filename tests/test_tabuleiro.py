from banco.partida import Tabuleiro


def test_tabuleiro_init():
    tabuleiro_01 = Tabuleiro(4, 20)
    assert len(tabuleiro_01.jogadores_ativos()) == 4
    assert len(tabuleiro_01.propriedades) == 20

def test_tabuleiro_obter_propriedade():
    tabuleiro_01 = Tabuleiro(4, 20)
    assert not tabuleiro_01.obter_propriedade(0) is None

def test_tabuleiro_liberar_propriedades():
    tabuleiro_01 = Tabuleiro(4, 20)
    propriedade = tabuleiro_01.obter_propriedade(0)
    jogador = tabuleiro_01.jogadores_ativos()[0]
    propriedade.adicionar_proprietario(jogador)
    assert propriedade.possui_proprietario()
    tabuleiro_01.liberar_propriedades(jogador)
    assert not propriedade.possui_proprietario()
