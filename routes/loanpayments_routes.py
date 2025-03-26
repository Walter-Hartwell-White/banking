from flask import request, jsonify
from models.loanpayments_models import Loanpayment
from __main__ import app, db, session
import datetime
class Loanpayment_Routes:
	def loanpayments(self):
		if request.method == 'GET':
			loanpayments = Loanpayment.query.all()
			if not loanpayments:
				return jsonify({'message': "No loanpayments found"}), 404

			response = []
			for loanpayment in loanpayments:
				response.append({
					"id": loanpayment.id,
					"user_id": loanpayment.user_id,
					"amount": loanpayment.amount,
					"principalamount": loanpayment.principalamount,
					"interestamount": loanpayment.interestamount,
					"paidamount": loanpayment.paidamount,
					"scheduledate": loanpayment.scheduledate,
					"created": loanpayment.created
					})
			return jsonify(response)

		if request.method == 'POST':
			new_loanpayment = Loanpayment	(
				user_id=session['user-id'],
				amount=request.get_json()['amount'],
				principalamount=request.get_json()['principalamount'],
				interestamount=request.get_json()['interestamount'],
				paidamount=request.get_json()['paidamount'],
				scheduledate=request.get_json()['scheduledate'],
				created=datetime.datetime.now()
				)
			db.session.add(new_loanpayment)
			db.session.commit()
			return jsonify({'message': "loanpayment added successfully."}), 200
	def loanpayment(self, loanpayment_id, extended=False):
		if request.method == 'GET':
			loanpayment = Loanpayment.query.get_or_404(loanpayment_id)
			response = {}
			response['id']= loanpayment.id
			response['user_id']= loanpayment.user_id
			response['amount']= loanpayment.amount
			response['principalamount']= loanpayment.principalamount
			response['interestamount']= loanpayment.interestamount
			response['paidamount']= loanpayment.paidamount
			response['scheduledate']= loanpayment.scheduledate
			response['created']= loanpayment.created
			if extended:
				response["users"] = []
				response["users"].append({
					'id': loanpayment.users.id,
					'name': loanpayment.users.name,
					'phonenumber': loanpayment.users.phonenumber,
					'aadharno': loanpayment.users.aadharno,
					'address': loanpayment.users.address,
					'emailid': loanpayment.users.emailid,
					'pswd': loanpayment.users.pswd,
					'mpin': loanpayment.users.mpin,
					'created': loanpayment.users.created
					})

			return jsonify(response)

		if request.method == 'PATCH':
			loanpayment = Loanpayment.query.get_or_404(loanpayment_id)
			if 'user_id' in request.get_json():
				loanpayment.user_id = request.get_json()['user_id']
			if 'amount' in request.get_json():
				loanpayment.amount = request.get_json()['amount']
			if 'principalamount' in request.get_json():
				loanpayment.principalamount = request.get_json()['principalamount']
			if 'interestamount' in request.get_json():
				loanpayment.interestamount = request.get_json()['interestamount']
			if 'paidamount' in request.get_json():
				loanpayment.paidamount = request.get_json()['paidamount']
			if 'scheduledate' in request.get_json():
				loanpayment.scheduledate = request.get_json()['scheduledate']
			if 'created' in request.get_json():
				loanpayment.created = request.get_json()['created']
			db.session.commit()

			return jsonify({'message': "loanpayment updated successfully."}), 200

		if request.method=='DELETE':
				loanpayment = Loanpayment.query.get_or_404(loanpayment_id)
				db.session.delete(loanpayment)
				db.session.commit()
				return jsonify({'message': "loanpayment deleted successfully."}), 200
