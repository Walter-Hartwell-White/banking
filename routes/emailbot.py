from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jwt import algorithms
from models.users_models import User
from flask import request, jsonify
import smtplib, time, random
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
from __main__ import app, db, session
# from routes.login_routes import Login_Routes
import jwt
class Email_Routes:
    def WelcomeEmail(self, email, name, extended=False):
        # print(email)
        # print(name)
        msg = MIMEMultipart()
        content = "Hey {}. It's great to have you on board. Welcome to Aapki Apna Bank - the best bank to open your account. We hope you have a great time here.".format(name)
        msg['Subject'] = 'AAP - AAPKI APNA BANK'
        msg['From'] = "jinay.c.kothari@gmail.com"
        msg['To'] = email
        msg.attach(MIMEText(content,'plain'))
        # msg.attach(MIMEText(str(time.strftime("%H:%M:%S")),'plain'))
        # print("server yet to start")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # print("Server Started")
        server.ehlo()
        # print("ehlo")
        server.starttls()
        # print("tls started")
        server.ehlo()
        # print("ehlo")
        server.login("jinay.c.kothari@gmail.com", "vonijfgwrlchmkqy")
        # print("logged in")
        server.send_message(msg)
        # print("email sent")
        server.quit()

        return "Email Sent Successfully.", 200
    def SendOTP(self, user_id, token, extended=False):
        # print(session['user-id'])
        # print(Login_Routes().Login()[0].__dict__)
        # print("USER-ID",session['user-id'])
        # print("user_id",session['user_id'])
        try:
            print("NONE")
            # print(jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"]))
            # print(jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"]))
        except:
            return jsonify({"message":"Invalid JWT Token!"}), 403
        emails = []
        if request.method == 'GET':
            user = User.query.get_or_404(user_id)
            emails.append(user.emailid)
        temp = random.randint(000000,999999)
        msg = MIMEMultipart()
        content = "Your otp for AAPKI APNA BANK Login is {}. Please don't share it with anyone.".format(temp)
        msg['Subject'] = 'AAB - AAPKI APNA BANK'
        msg['From'] = "jinay.c.kothari@gmail.com"
        # mails = ['jinay.c.kothari@gmail.com']
        msg['To'] = emails[0]
        # msg['cc'] = 'jinaykothari90@gmail.com'
        # msg['bcc'] = "jinay.c.kothari@gmail.com"
        msg.attach(MIMEText(content,'plain'))
        # filename = "ST Certificate and Index.pdf"
        # attachment = open("/Users/jinay/Downloads/ST Certificate and Index.pdf", "rb")
        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # msg.attach(part)
        msg.attach(MIMEText(str(time.strftime("%H:%M:%S")),'plain'))
        session['otp'] = temp
        session['user_id'] = user_id
        session['otp_time'] = datetime.now().minute + 5
        # print("server yet to start")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # print("Server Started")
        server.ehlo()
        # print("ehlo")
        server.starttls()
        # print("tls started")
        server.ehlo()
        # print("ehlo")
        server.login("jinay.c.kothari@gmail.com", "vonijfgwrlchmkqy")
        # print("logged in")
        server.send_message(msg)
        # print("email sent")
        server.quit()

        return jsonify({'message': "OTP Sent Successfully."}), 200

    def VerifyOTP(self, extended=False):
        if request.method == 'POST':
            otp = request.get_json()['otp']
            # print(otp)
            # print(session['otp'])
            # print(session)
            print(session['otp_time'])
            print(datetime.now().minute)
            # print(datetime.now().minute)
            if session['otp'] == otp and session['otp_time'] >= datetime.now().minute:
                return jsonify({'message': "OTP Verified Successfully. "}), 200
            else:
                return jsonify({'message': "OTP Verification Failed "}), 400

#             # -------------------------------------------------------- END OF THE PROGRAM --------------------------------------------------
