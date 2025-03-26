from . import db

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    balance = db.Column(db.Integer)
    type = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='accounts')

    def __repr__(self):
        return '<Account %r>' % self.id
