from database import db

class Doacao(db.Model):
    __tablename__ = "usuario"
    id_doacao = db.Column(db.Integer, primary_key=True)
    doador = db.Column(db.String(100))
    valor = db.Column(db.Float(10, 2))
    data = db.Column(db.Date)

    def __init__(self, nome, email, idade):
        self.doador = doador
        self.valor = valor
        self.data = data

    def __repr__(self):
        return "<Doação de {}>".format(self.doador)
