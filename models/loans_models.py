from . import db
class Loan(db.Model):
	__tablename__='loans'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	amount = db.Column(db.Integer)
	interestrate = db.Column(db.Numeric(10,0))
	startdate = db.Column(db.DateTime)
	enddate = db.Column(db.DateTime)
	status = db.Column(db.Integer)
	term = db.Column(db.Integer)
	created = db.Column(db.DateTime)

	user = db.relationship('User', back_populates='loans')

	def __repr__(self):
		return '<Loan %r>' % self.id
