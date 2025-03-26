from . import db
class Loanpayment(db.Model):
	__tablename__='loanpayments'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	amount = db.Column(db.Numeric(10,0))
	principalamount = db.Column(db.Numeric(10,0))
	interestamount = db.Column(db.Numeric(10,0))
	paidamount = db.Column(db.Numeric(10,0))
	scheduledate = db.Column(db.DateTime)
	created = db.Column(db.DateTime)

	user = db.relationship('User', back_populates='loanpayments')
	def __repr__(self):
		return '<Loanpayment %r>' % self.id
