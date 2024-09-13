from database import db

class Doacao(db.Model):
    __tablename__ = "doacao"
    id_doacao = db.Column(db.Integer, primary_key=True)
    doador = db.Column(db.String(100))
    valor = db.Column(db.Float(2))
    data = db.Column(db.Date)

    def __init__(self, doador, valor, data):
        self.doador = doador
        self.valor = valor
        self.data = data

    def __repr__(self):
        return "<Doação de {}>".format(self.valor)
