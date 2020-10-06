# Cenários

-   Inicio da partida;
-   Uma jogada;
-   Uma rodada;
-   Um volta no tabuleiro;
-   Jogador fica com saldo negativo;
-   Fim do jogo quando restar um jogador;
-   Fim do jogo ao término de 1000 rodadas.

```
Jogador:
- sabe seu saldo
- sabe se está no jogo
- sabe seu nome
- compra propriedade
-



Jogador
    saldo
    ativo
    pos
    nome
    ------
    comprar
    debitar
    creditar
    andar
    eliminar


Propriedade
    proprietario
    aluguel
    custo_venda
    ------


Tabuleiro
    jogadores
    propriedades
    ------
    propriedade
    jogadores_ativos


Partida
    executando
    rodada
    ------
    iniciar
    jogar_rodada
    terminou
    ganhador
    liberar_propriedades
```
