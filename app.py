from flask import Flask, request, session, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ipDJUthuXrbIostNvFcbKswbkTzwdvgJ@trolley.proxy.rlwy.net:15772/railway"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Root-123@localhost/banking"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "92f1ee3a98f44ccb93f0c949d51f247e"
db = SQLAlchemy(app)

@app.route("/")
def home():
	return {"success":"true"}

@app.route("/accounts", methods = ['GET', 'POST'])
def Accounts_App():
		from routes.accounts_routes import Account_Routes
		return Account_Routes().accounts()

@app.route("/loanpayments", methods = ['GET', 'POST'])
def Loanpayments_App():
		from routes.loanpayments_routes import Loanpayment_Routes
		return Loanpayment_Routes().loanpayments()

@app.route("/loans", methods = ['GET', 'POST'])
def Loans_App():
		from routes.loans_routes import Loan_Routes
		return Loan_Routes().loans()

@app.route("/transactions", methods = ['GET', 'POST'])
def Transactions_App():
		from routes.transactions_routes import Transaction_Routes
		return Transaction_Routes().transactions()

@app.route("/users", methods = ['GET', 'POST'])
def Users_App():
		from routes.users_routes import User_Routes
		return User_Routes().users()

@app.route("/accounts/<int:account_id>", methods = ['GET', 'PATCH', 'DELETE'])
def accounts_App(account_id):
		from routes.accounts_routes import Account_Routes
		return Account_Routes().account(account_id, True if request.args.get('extended') else False)

@app.route("/loanpayments/<int:loanpayment_id>", methods = ['GET', 'PATCH', 'DELETE'])
def loanpayments_App(loanpayment_id):
		from routes.loanpayments_routes import Loanpayment_Routes
		return Loanpayment_Routes().loanpayment(loanpayment_id, True if request.args.get('extended') else False)

@app.route("/loans/<int:loan_id>", methods = ['GET', 'PATCH', 'DELETE'])
def loans_App(loan_id):
		from routes.loans_routes import Loan_Routes
		return Loan_Routes().loan(loan_id, True if request.args.get('extended') else False)

@app.route("/transactions/<int:transaction_id>", methods = ['GET', 'PATCH', 'DELETE'])
def transactions_App(transaction_id):
		from routes.transactions_routes import Transaction_Routes
		return Transaction_Routes().transaction(transaction_id, True if request.args.get('extended') else False)

@app.route("/users/<int:user_id>", methods = ['GET', 'PATCH', 'DELETE'])
def users_App(user_id):
		from routes.users_routes import User_Routes
		return User_Routes().user(user_id, True if request.args.get('extended') else False)


@app.route("/sendotp", methods = ['GET'])
def sendotp():
    # print(session['user-id'])
    from routes.emailbot import Email_Routes
    return Email_Routes().SendOTP(session['user-id'],session['jwt'], True if request.args.get('extended') else False)

@app.route("/verifyotp", methods = ['POST'])
def verifyotp():
    from routes.emailbot import Email_Routes
    return Email_Routes().VerifyOTP()

@app.route("/login", methods = ['POST'])
def login():
    from routes.login_routes import Login_Routes
    return Login_Routes().Login()

@app.route("/logout", methods = ['POST'])
def logout():
    from routes.login_routes import Login_Routes
    return Login_Routes().Logout()

@app.route("/transfer", methods = ["POST"])
def transfer():
    from routes.transactions_routes import Transaction_Routes
    return Transaction_Routes().newtransaction()


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=3000)
