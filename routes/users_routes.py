from flask import request, jsonify
from models.users_models import User
from models.emailbot import Email_Routes
from __main__ import app, db
import datetime, bcrypt, uuid
class User_Routes:
	def users(self):
		if request.method == 'GET':
			users = User.query.all()
			if not users:
				return jsonify({'message': "No users found"}), 404

			response = []
			for user in users:
				response.append({
					"id": user.id,
					"name": user.name,
					"phonenumber": user.phonenumber,
					"aadharno": user.aadharno,
					"address": user.address,
					"emailid": user.emailid,
					"pswd": user.pswd,
					"mpin": user.mpin,
					"created": user.created
					})
			return jsonify(response)

		if request.method == 'POST':
			new_user = User	(
			name=request.get_json()['name'],
			phonenumber=request.get_json()['phonenumber'],
			aadharno=bcrypt.hashpw(request.get_json()['aadharno'].encode(), salt = bcrypt.gensalt()),
			address=request.get_json()['address'],
			emailid=request.get_json()['emailid'],
			pswd=bcrypt.hashpw(request.get_json()['pswd'].encode(), salt = bcrypt.gensalt()),
			mpin=bcrypt.hashpw(request.get_json()['mpin'].encode(), salt = bcrypt.gensalt()),
			created=datetime.datetime.utcnow()
				)
			db.session.add(new_user)
			db.session.commit()
			return jsonify({'message': "user added successfully."}), 200
			Email_Routes().WelcomeEmail(request.get_json()['emailid'],request.get_json()['name'])
			return jsonify({'message': "user added successfully."}), 200
	def user(self, user_id, extended=False):
		if request.method == 'GET':
			user = User.query.get_or_404(user_id)
			response = {}
			response["id"] = user.id
			response["name"] = user.name
			response["phonenumber"] = user.phonenumber
			response["aadharno"] = user.aadharno
			response["address"] = user.address
			response["emailid"] = user.emailid
			response["pswd"] = user.pswd
			response["mpin"] = user.mpin
			response["created"] = user.created
			if extended:
				response["accounts"] = []
				for account in user.accounts:
					response["accounts"].append({
						'id': account.id,
						'user_id': account.user_id,
						'balance': account.balance,
						'type': account.type,
						'created': account.created
						})

			if extended:
				response["loanpayments"] = []
				for loanpayment in user.loanpayments:
					response["loanpayments"].append({
						'id': loanpayment.id,
						'user_id': loanpayment.user_id,
						'amount': loanpayment.amount,
						'principalamount': loanpayment.principalamount,
						'interestamount': loanpayment.interestamount,
						'paidamount': loanpayment.paidamount,
						'scheduledate': loanpayment.scheduledate,
						'created': loanpayment.created
						})

			if extended:
				response["loans"] = []
				for loan in user.loans:
					response["loans"].append({
						'id': loan.id,
						'user_id': loan.user_id,
						'amount': loan.amount,
						'interestrate': loan.interestrate,
						'startdate': loan.startdate,
						'enddate': loan.enddate,
						'status': loan.status,
						'term': loan.term,
						'created': loan.created
						})

			if extended:
				response["transactions"] = []
				for transaction in user.transactions:
					response["transactions"].append({
						'id': transaction.id,
						'user_id': transaction.user_id,
						'type': transaction.type,
						'amount': transaction.amount,
						'created': transaction.created
						})

			return jsonify(response)

		if request.method == 'PATCH':
			user = User.query.get_or_404(user_id)
			if 'name' in request.get_json():
				user.name = request.get_json()['name']
			if 'phonenumber' in request.get_json():
				user.phonenumber = request.get_json()['phonenumber']
			if 'aadharno' in request.get_json():
				user.aadharno = request.get_json()['aadharno']
			if 'address' in request.get_json():
				user.address = request.get_json()['address']
			if 'emailid' in request.get_json():
				user.emailid = request.get_json()['emailid']
			if 'pswd' in request.get_json():
				user.pswd = request.get_json()['pswd']
			if 'mpin' in request.get_json():
				user.mpin = request.get_json()['mpin']
			if 'created' in request.get_json():
				user.created = request.get_json()['created']
			db.session.commit()

			return jsonify({'message': "user updated successfully."}), 200

		if request.method=='DELETE':
				user = User.query.get_or_404(user_id)
				db.session.delete(user)
				db.session.commit()
				return jsonify({'message': "user deleted successfully."}), 200
