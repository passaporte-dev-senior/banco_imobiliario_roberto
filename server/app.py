from banco.partida import Partida
from flask import Flask, render_template, request

app = Flask(__name__)

partida = Partida(4, 20)
partida.iniciar()

@app.route('/')
def index():
    ganhador = None
    reset = request.args.get('r')
    if reset:
        global partida
        partida = Partida(4, 20)
        partida.iniciar()

    update = request.args.get('u')
    if update:
        if not partida.terminou():
            partida.jogar_rodada()
            
    ganhador = partida.vencedor()
    return render_template('index.html', ganhador=ganhador, partida=partida)
