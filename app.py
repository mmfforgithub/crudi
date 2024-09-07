from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Doacao
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#drive://usuario:senha@servidor/banco_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskg1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/doacao')
def doacao():
    d = Doacao.query.all()
    return render_template('doacao_lista.html', dados = d)

@app.route('/doacao/add')
def doacao_add():
    return render_template('doacao_add.html')

@app.route('/doacao/save', methods=['POST'])
def doacao_save():
    doador = request.form.get('doador')
    valor = request.form.get('valor')
    data = request.form.get('data')
    if doador and valor and data:
        doacao = Doacao(doador, valor, data)
        db.session.add(doacao)
        db.session.commit()
        flash('Doação cadastrada!')
        return redirect ("/doacao")
    else:
        flash("Preencha todos os campos!")
        return redirect ("/doacao/add")
    
@app.route('/doacao/remove/<int:id_doacao>')
def doacao_removo(id_doacao):
    if id_doacao > 0:
        doacao = Doacao.query.get(id_doacao)
        db.session.delete(doacao)
        db.session.commit()
        flash('Doação removida.')
        return redirect('/doacao')
    else:
        flash('Caminho incorreto.')
        return redirect('/doacao')


@app.route('/doacao/edita/<int:id_doacao>')
def doacao_editar(id_doacao):
    doacao = Doacao.query.get(id_doacao)
    return render_template('doacao_editar.html', dados = doacao)

@app.route('/doacao/editasave', methods = ['POST'])
def doacao_edita_save():
    id_doacao = request.form.get('id_doacao')
    doacao = request.form.get('doador')
    valor = request.form.get('valor')
    data = request.form.get('data')
    if id_doacao and doador and valor and data:
        doacao = Doacao.query.get(id_doacao)
        doacao.doador = doador
        usuario.email = email
        usuario.idade = idade
        db.session.commit()
        flash('Dados atualizados.')
        return redirect('/doacao')
    else:
        flash('Não há.')
        return redirect('/doacao')

if __name__ == '__main__':
    app.run()
