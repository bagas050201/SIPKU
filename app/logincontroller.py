from flask import Flask, render_template, url_for, redirect, request, session, Blueprint
from bson.objectid import ObjectId
from model.member import Member
from model.log import Log

login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/')
def login_user():
    if ('masuk' in session):
        return redirect(url_for("dashboard.dashboard_user"))
    if ('admin' in session):
        return redirect(url_for("dashboard.dashboard_admin"))
    return render_template("login.html")


@login.route('/auth', methods=["POST", "GET"])
def authLogin():
    if request.method == 'POST':
        id_member = request.form['idMember']
        password = request.form['password']

        if id_member == '2021' and password == "admin":
            session['admin'] = id_member
            return redirect(url_for('dashboard.dashboard_admin'))
        elif checkLogin(id_member, password):
            session['masuk'] = int(id_member)
            Log().addLog(Member().getFullname(str(session['masuk'])) +
                         " login")
            return redirect(url_for('dashboard.dashboard_user'))

    return url_for('login.login_user')


def checkLogin(id_member, password):
    member = Member()
    print("masuk ga ya")
    print(member.getPassword(id_member))
    # print(password)
    print("test")
    if str(member.getPassword(id_member)) == password:
        return True
    return False
