# Desafio do Banco Imobiliário

# Classe Propriedade

> Define um imóvel que pode ser alugado ou vendido a um jogador.

### Responsabilidades:

-   Possui proprietario, aluguel e custo de venda.
-   Adiciona o proprietário.
-   Remove o proprietário.

### Colaborações:

-   Jogador

# Classe Jogador

> Define um participante do jogo.

### Responsabilidades:

-   Possui saldo, status, posicao e nome.
-   Se elimina do jogo.
-   Anda.
-   Credita saldo.
-   Debita saldo.
-   Compra (decide se deseja comprar).

### Colaborações:

# Dado

> Representa um dado.

### Responsabilidades:

-   Sorteia um número aleatorio entre 1 e 6.

### Colaborações:

# Tabuleiro

> Representa um tabuleiro que controla os jogadores e as propriedades.

### Responsabilidades:

-   Possui propriedades e jogadores.
-   Conhece os jogadores ativos.
-   Remove o jagador de propriedades a qual ele é proprietário.

### Colaborações:

-   Jogador
-   Propriedade

# Partida

> Controla os detalhes da partida, suas rodadas e regras.

### Responsabilidades:

-   Inicia uma partida.
-   Termina um partida.
-   Joga um rodada.
-   Sabe quem é o jogador vencedor.
-   Faz uma jogada com um jogador.

### Colaborações:

-   Jogador
-   Propriedade
-   Tabuleiro

`pytest --cov=banco tests/`