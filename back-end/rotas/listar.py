from config import *
from classes.jogador import *

@app.route("/listar/<string:classe>")
def listar(classe):

    dados = None

    if classe == "Jogador":
        dados = db.session.query(Jogador).all()
        
    if dados:
        dados_json = []
        for d in dados:
            dados_json.append(d.json())

        resposta = {"resultado": "ok", "detalhes": dados_json}
    
    else:
        resposta = jsonify({"resultado": "Erro!", "detalhes": "Classe informada inválida: "+classe})

    return resposta