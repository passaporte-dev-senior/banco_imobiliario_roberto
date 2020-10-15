import random
from .jogador import criar_jogadores
from .propriedade import criar_propriedades


class Tabuleiro:
    def __init__(self, qtd_jogadores, qtd_propriedades):
        jogadores = criar_jogadores(qtd_jogadores)
        self.jogadores = random.sample(jogadores, k=len(jogadores))
        self.propriedades = criar_propriedades(qtd_propriedades)

    @property
    def qtd_propriedades(self):
        return len(self.propriedades)

    @property
    def qtd_jogadores(self):
        return len(self.jogadores)

    def obter_propriedade(self, pos):
        return self.propriedades[pos]

    def jogadores_ativos(self):
        return [j for j in self.jogadores if j.ativo]

    def liberar_propriedades(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.remover_proprietario()
