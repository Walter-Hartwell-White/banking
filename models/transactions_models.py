from . import db
class Transaction(db.Model):
	__tablename__='transactions'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	type = db.Column(db.Integer)
	amount = db.Column(db.Integer)
	created = db.Column(db.DateTime)

	user = db.relationship('User', back_populates='transactions')
	def __repr__(self):
		return '<Transaction %r>' % self.id
