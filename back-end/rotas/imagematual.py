from config import *

@app.route('/imagematual')
def imagematual():
    imagem = os.path.join(pastaimagens, "bg.png")
    return send_file(imagem, mimetype='image/gif')