from flask import request, jsonify
from models.accounts_models import Account
from __main__ import app, db, session
import datetime
class Account_Routes:
	def accounts(self):
		if request.method == 'GET':
			accounts = Account.query.all()
			if not accounts:
				return jsonify({'message': "No accounts found"}), 404

			response = []
			for account in accounts:
				response.append({
					"id": account.id,
					"user_id": account.user_id,
					"balance": account.balance,
					"type": account.type,
					"created": account.created
					})
			return jsonify(response)

		if request.method == 'POST':
			new_account = Account	(
				user_id=session['user-id'],
				balance=request.get_json()['balance'],
				type=request.get_json()['type'],
				created=datetime.datetime.now()
				)
			db.session.add(new_account)
			db.session.commit()
			return jsonify({'message': "account added successfully."}), 200
	def account(self, account_id, extended=False):
		if request.method == 'GET':
			account = Account.query.get_or_404(account_id)
			response = {}
			response['id']= account.id
			response['user_id']= account.user_id
			response['balance']= account.balance
			response['type']= account.type
			response['created']= account.created
			if extended:
				response["users"] = []
				print(account.users)
				response["users"].append({
					'id': account.users.id,
					'name': account.users.name,
					'phonenumber': account.users.phonenumber,
					'aadharno': account.users.aadharno,
					'address': account.users.address,
					'emailid': account.users.emailid,
					'pswd': account.users.pswd,
					'mpin': account.users.mpin,
					'created': account.users.created
					})

			return jsonify(response)

		if request.method == 'PATCH':
			account = Account.query.get_or_404(account_id)
			if 'user_id' in request.get_json():
				account.user_id = request.get_json()['user_id']
			if 'balance' in request.get_json():
				account.balance = request.get_json()['balance']
			if 'type' in request.get_json():
				account.type = request.get_json()['type']
			if 'created' in request.get_json():
				account.created = request.get_json()['created']
			db.session.commit()

			return jsonify({'message': "account updated successfully."}), 200

		if request.method=='DELETE':
				account = Account.query.get_or_404(account_id)
				db.session.delete(account)
				db.session.commit()
				return jsonify({'message': "account deleted successfully."}), 200
