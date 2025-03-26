from flask import request, jsonify
from models.loans_models import Loan
from __main__ import app, db, session
import datetime
class Loan_Routes:
	def loans(self):
		if request.method == 'GET':
			loans = Loan.query.all()
			if not loans:
				return jsonify({'message': "No loans found"}), 404

			response = []
			for loan in loans:
				response.append({
					"id": loan.id,
					"user_id": loan.user_id,
					"amount": loan.amount,
					"interestrate": loan.interestrate,
					"startdate": loan.startdate,
					"enddate": loan.enddate,
					"status": loan.status,
					"term": loan.term,
					"created": loan.created
					})
			return jsonify(response)

		if request.method == 'POST':
			new_loan = Loan	(
				user_id=session['user-id'],
				amount=request.get_json()['amount'],
				interestrate=request.get_json()['interestrate'],
				startdate=request.get_json()['startdate'],
				enddate=request.get_json()['enddate'],
				status=request.get_json()['status'],
				term=request.get_json()['term'],
				created=datetime.datetime.now()
				)
			db.session.add(new_loan)
			db.session.commit()
			return jsonify({'message': "loan added successfully."}), 200
	def loan(self, loan_id, extended=False):
		if request.method == 'GET':
			loan = Loan.query.get_or_404(loan_id)
			response = {}
			response['id']= loan.id
			response['user_id']= loan.user_id
			response['amount']= loan.amount
			response['interestrate']= loan.interestrate
			response['startdate']= loan.startdate
			response['enddate']= loan.enddate
			response['status']= loan.status
			response['term']= loan.term
			response['created']= loan.created
			if extended:
				response["users"] = []
				response["users"].append({
					'id': loan.users.id,
					'name': loan.users.name,
					'phonenumber': loan.users.phonenumber,
					'aadharno': loan.users.aadharno,
					'address': loan.users.address,
					'emailid': loan.users.emailid,
					'pswd': loan.users.pswd,
					'mpin': loan.users.mpin,
					'created': loan.users.created
					})

			return jsonify(response)

		if request.method == 'PATCH':
			loan = Loan.query.get_or_404(loan_id)
			if 'user_id' in request.get_json():
				loan.user_id = request.get_json()['user_id']
			if 'amount' in request.get_json():
				loan.amount = request.get_json()['amount']
			if 'interestrate' in request.get_json():
				loan.interestrate = request.get_json()['interestrate']
			if 'startdate' in request.get_json():
				loan.startdate = request.get_json()['startdate']
			if 'enddate' in request.get_json():
				loan.enddate = request.get_json()['enddate']
			if 'status' in request.get_json():
				loan.status = request.get_json()['status']
			if 'term' in request.get_json():
				loan.term = request.get_json()['term']
			if 'created' in request.get_json():
				loan.created = request.get_json()['created']
			db.session.commit()

			return jsonify({'message': "loan updated successfully."}), 200

		if request.method=='DELETE':
				loan = Loan.query.get_or_404(loan_id)
				db.session.delete(loan)
				db.session.commit()
				return jsonify({'message': "loan deleted successfully."}), 200
