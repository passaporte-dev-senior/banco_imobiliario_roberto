from banco.partida import Partida, Dado


def test_dado_seed():
    numero = Dado.sortear()
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

def test_partida_ganhador():
    partida_01 = Partida()
    assert partida_01.ganhador() is None

def test_partida_jogar_rodada():
    partida_01 = Partida()
    partida_01.iniciar()
    partida_01.jogar_rodada()
    assert partida_01.rodada == 1

def test_partida_jogar_rodada():
    partida_01 = Partida(2, 20)
    partida_01.iniciar()
    partida_01.jogar_rodada()
    assert partida_01.rodada == 1    
