from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

caminho = os.path.dirname(os.path.abspath(__file__))
caminhopai = os.path.dirname(caminho)
pastajogo = os.path.join(caminhopai, 'jogo/')
pastaimagens = os.path.join(pastajogo, 'images/')

arquivobd = os.path.join(caminho, 'data.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)