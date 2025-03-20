from flask import Blueprint, render_template, request

# Criando o Blueprint para as rotas
bp = Blueprint('main', __name__)

# Rota para a página principal (home)


@bp.route('/')
def home():
    return render_template('home.html', title='Página Inicial')

# Rota para uma página de "sobre"


@bp.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre nós')

# Rota para uma página dinâmica (com parâmetro na URL)


@bp.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('saudacao.html', nome=nome)
