from flask import Flask, render_template, url_for, redirect, request, session, Blueprint
from bson.objectid import ObjectId
from model.member import Member


login=Blueprint('login', __name__, url_prefix='/login')

@login.route('/')
def login_user():
    if('masuk' in session):
        return redirect(url_for("dashboard.dashboard_user"))
    return render_template("login.html")

@login.route('/auth', methods=["POST", "GET"])
def authLogin():
    if request.method=='POST':
        id_member = int(request.form['idMember'])
        password = request.form['password']
        if checkLogin(id_member, password):
            session['masuk']=id_member
            return redirect(url_for('dashboard.dashboard_user'))
    return url_for('login.login_user')

def checkLogin(id_member, password):
    member=Member()
    if member.getPassword(id_member)==password:
        return True
    # return False
    return redirect(url_for('dashboard.dashboard_user'))

# print(checkLogin(12345, "sesuatu"))
# print(session['masuk'])