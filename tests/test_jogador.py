from banco.jogador import (
    Jogador,
    JogadorImpulsivo,
    JogadorExigente,
    JogadorCauteloso,
    JogadorAleatorio,
)


def test_jogador_init():
    jogador_01 = Jogador()
    assert jogador_01.ativo
    assert jogador_01.saldo == 300
    assert jogador_01.pos == 0


def test_jogador_andar_para():
    jogador_01 = Jogador()
    assert jogador_01.pos == 0
    jogador_01.andar_para(10)
    assert jogador_01.pos == 10


def test_jogador_string():
    jogador_01 = Jogador()
    jogador_01.nome = "Jogador"
    assert str(jogador_01) == "<Jogador Jogador a?:True p#:0 s#:300>"


def test_jogador_saldo():
    jogador_01 = Jogador()
    jogador_01.debitar(50)
    assert jogador_01.saldo == 250
    jogador_01.creditar(100)
    assert jogador_01.saldo == 350


def test_jogador_perde():
    jogador_01 = Jogador()
    jogador_01.debitar(350)
    assert jogador_01.saldo == -50
    assert not jogador_01.ativo


def test_jogador_impulsivo():
    jogador_01 = JogadorImpulsivo()
    assert jogador_01.comprar(0, 0)


def test_jogador_exigente():
    jogador_01 = JogadorExigente()
    assert jogador_01.comprar(100, 0)
    assert not jogador_01.comprar(10, 0)


def test_jogador_cauteloso():
    jogador_01 = JogadorCauteloso()
    assert jogador_01.comprar(0, 100)


def test_jogador_aleatorio():
    jogador_01 = JogadorAleatorio()
    jogador_01.random_choice = lambda: True
    assert jogador_01.comprar(0, 0)
