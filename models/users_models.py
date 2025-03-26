from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phonenumber = db.Column(db.String(10))
    aadharno = db.Column(db.String(255))
    address = db.Column(db.String(255))
    emailid = db.Column(db.String(255))
    pswd = db.Column(db.String(255))
    mpin = db.Column(db.String(255))
    created = db.Column(db.DateTime)

    accounts = db.relationship('Account', back_populates='user')
    loanpayments = db.relationship('Loanpayment', back_populates='user')
    loans = db.relationship('Loan', back_populates='user')
    transactions = db.relationship('Transaction', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.id
