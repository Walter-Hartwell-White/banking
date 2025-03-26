from models.users_models import User
from flask import request, jsonify
import bcrypt, jwt
from __main__ import app, db, session
class Login_Routes:
    def Login(self):
        if request.method == 'POST':
            user = User.query.filter_by(emailid=request.get_json()['emailid']).first()
            # print(user.id)
            if not user:
                return jsonify({'message': "No user found with that email"}), 404
            if bcrypt.checkpw(request.get_json()['pswd'].encode(), user.pswd.encode()):
                session['user-id'] = user.id
                session['jwt'] = jwt.encode({"id":user.id},app.config['SECRET_KEY'],algorithm="HS256")
                session.modified = True
                if jwt.decode(session['jwt'],app.config['SECRET_KEY'],algorithms=["HS256"]):
                    # print(user.id)
                    # print(jwt.encode({"id":user.id},app.config['SECRET_KEY'],algorithm="HS256"))
                    # print(user.uuid)
                    return jsonify({'message': "Login successful","id":user.id,"token":session['jwt']},200)
                else:
                    return jsonify({"message":"JWT Invalid!"},403)
            return jsonify({'message': "Incorrect Password"}), 403
        return jsonify({'message': "Invalid request"}), 404

    def Logout(self):
        if request.method == 'POST':
            session.pop('user-id', None)
            session.pop('jwt', None)
            session.pop('user_id', None)
            session.pop('otp_time', None)
            session.pop('otp', None)
            return jsonify({'message': "Logout successful"}), 200
        return jsonify({'message': "Invalid request"}), 404
