import random
from .jogador import criar_jogadores
from .propriedade import criar_propriedades


class Tabuleiro:
    def __init__(self, num_jogador, num_propriedades):
        jogadores = criar_jogadores(num_jogador)
        self.jogadores = random.sample(jogadores, k=len(jogadores))
        self.propriedades = criar_propriedades(num_propriedades)

    @property
    def quantidade_propriedades(self):
        return len(self.propriedades)

    def obter_propriedade(self, pos):
        return self.propriedades[pos]

    def jogadores_ativos(self):
        return [j for j in self.jogadores if j.ativo]

    def liberar_propriedades(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.remover_proprietario()

