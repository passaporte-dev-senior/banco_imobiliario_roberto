Considere o seguinte jogo hipotético muito semelhante a Banco Imobiliário, onde várias de suas mecânicas foram simplificadas.

O tabuleiro é composto por 20 propriedades distribuídas sequencialmente.

O jogo é iniciado com o sorteio da ordem dos jogadores

Jogadores iniciam a partida com saldo igual a 300.

Cada propriedade tem um custo de venda e um valor de aluguel.

A propriedade pode ter um proprietário ou não.

O jogador joga um dado não-viciado de 6 faces que determina quantos espaços no tabuleiro o jogador vai andar.

Ao parar em uma propriedade pode ocorrer 2 situações:

-   A propriedade já possui um proprietário. Nesse caso o jogador deve pagar ao proprietário o valor de aluguel.
-   A propriedade não possui um proprietário. Nesse caso o jogador pode escolher entre comprar ou não comprar a propriedade. Se escolher comprar e tiver saldo suficiente, ele deve pagar o custo de venda.

Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.

Se um jogador ficar com saldo negativo, ele é eliminado do jogo. Ele perde suas propriedades que podem ser compradas por qualquer outro jogador.

Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida com 4 diferentes tipos de possíveis jogadores.

Os comportamentos definidos são:

-   O jogador **impulsivo** compra qualquer propriedade sobre a qual ele parar.
-   O jogador **exigente** compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
-   O jogador **cauteloso** compra qualquer propriedade desde que ele tenha uma reserva de 80 de saldo sobrando depois de realizada a compra.
-   O jogador **aleatório** compra ou não a propriedade que ele parar em cima com probabilidade de 50%.

Será declarado vencedor o último jogador que permanecer no jogo ou de 1000 rodadas, o jogador com mais saldo.

O critério de desempate é a ordem de turno dos jogadores nesta partida.
