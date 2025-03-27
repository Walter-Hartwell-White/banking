from flask import request, jsonify
from models.transactions_models import Transaction
from __main__ import app, db, session
import datetime
class Transaction_Routes:
    def newtransaction(self):
        if request.method == 'POST' and session.get('login') == True:
            # print(session['login'])
            # print(session)
            return jsonify({"message":"OKAY"}),200
        else:
            return jsonify({"message":"Please Login before adding transaction."}),404
        # else:
        #     print("Please Login before adding transaction. ")
            # return jsonify({"message":"Please Login before adding transaction."}),404

    def transactions(self):
        if request.method == 'GET':
            transactions = Transaction.query.all()
            if not transactions:
                return jsonify({'message': "No transactions found"}), 404

            response = []
            for transaction in transactions:
                response.append({
                    "id": transaction.id,
                    "user_id": transaction.user_id,
                    "type": transaction.type,
                    "amount": transaction.amount,
                    "created": transaction.created
                    })
            return jsonify(response)

        if request.method == 'POST':
            new_transaction = Transaction   (
                user_id=session['user-id'],
                type=request.get_json()['type'],
                amount=request.get_json()['amount'],
                created=datetime.datetime.now()
                )
            db.session.add(new_transaction)
            db.session.commit()
            return jsonify({'message': "transaction added successfully."}), 200
    def transaction(self, transaction_id, extended=False):
        if request.method == 'GET':
            transaction = Transaction.query.get_or_404(transaction_id)
            response = {}
            response['id']= transaction.id
            response['user_id']= transaction.user_id
            response['type']= transaction.type
            response['amount']= transaction.amount
            response['created']= transaction.created
            if extended:
                response["users"] = []
                response["users"].append({
                    'id': transaction.users.id,
                    'name': transaction.users.name,
                    'phonenumber': transaction.users.phonenumber,
                    'aadharno': transaction.users.aadharno,
                    'address': transaction.users.address,
                    'emailid': transaction.users.emailid,
                    'pswd': transaction.users.pswd,
                    'mpin': transaction.users.mpin,
                    'created': transaction.users.created
                    })

            return jsonify(response)

        if request.method == 'PATCH':
            transaction = Transaction.query.get_or_404(transaction_id)
            if 'user_id' in request.get_json():
                transaction.user_id = request.get_json()['user_id']
            if 'type' in request.get_json():
                transaction.type = request.get_json()['type']
            if 'amount' in request.get_json():
                transaction.amount = request.get_json()['amount']
            if 'created' in request.get_json():
                transaction.created = request.get_json()['created']
            db.session.commit()

            return jsonify({'message': "transaction updated successfully."}), 200

        if request.method=='DELETE':
                transaction = Transaction.query.get_or_404(transaction_id)
                db.session.delete(transaction)
                db.session.commit()
                return jsonify({'message': "transaction deleted successfully."}), 200
