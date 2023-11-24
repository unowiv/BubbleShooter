from config import *

# curl -i -X POST -F files=@foto.jpeg localhost:5000/salvar
@app.route("/salvar", methods=["post"])
def salvar():

    try:
        imagem = request.files["files"]
        caminho_salvar = os.path.join(pastaimagens, 'bg.png')
        imagem.save(caminho_salvar)
        resposta = jsonify({"resultado":"ok", "detalhes": "Imagem salva"})

    except Exception as erro:
        resposta = jsonify({"resposta": "Erro!", "detalhes": str(erro)})

    return resposta