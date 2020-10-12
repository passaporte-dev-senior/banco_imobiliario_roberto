from banco.jogador import Jogador
from banco.propriedade import Propriedade


def test_inicializacao():
    propriedade_01 = Propriedade()
    assert propriedade_01.custo_venda > 0
    assert propriedade_01.aluguel > 0
    assert propriedade_01.proprietario is None
    assert 'Propriedade' in repr(propriedade_01)  

def test_proprietario():
    jogador_01 = Jogador()
    propriedade_01 = Propriedade()
    propriedade_01.adicionar_proprietario(jogador_01)
    assert propriedade_01.possui_proprietario()
    assert propriedade_01.proprietario == jogador_01
    propriedade_01.remover_proprietario()
    assert not propriedade_01.possui_proprietario()
