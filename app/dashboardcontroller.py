from flask import Flask, render_template, url_for, redirect, request, session, Blueprint
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename 
import os
from logincontroller import login
from model.member import Member
from model.event import Event

dashboard=Blueprint('dashboard', __name__, url_prefix='/')

@dashboard.route('/')
def dashboard_user():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    name_member=Member().getFullname(session['masuk'])
    return render_template("dashboard_user.html", name_member=name_member)

@dashboard.route('/profil')
def dashboard_user_profil():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    data=Member().getDataMember(session['masuk'])
    return render_template("dashboard_user_profil.html", name_member=data['fullname'], data_member=data)

@dashboard.route('/profil/update-data', methods=["POST", "GET"])
def update_data():
    if request.method=='POST':
        fullname=request.form['fullname']
        study=request.form['study']
        gen=request.form['gen']
        Member(session['masuk']).updateMember(fullname, study, gen)
        data=Member().getDataMember(session['masuk'])
        return render_template("dashboard_user_profil.html", name_member=data['fullname'], data_member=data, pesan=True)
    return redirect (url_for('dashboard.dashboard_user_profil'))

@dashboard.route('/isi-kehadiran')
def dashboard_user_kehadiran():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    name_member=Member().getFullname(session['masuk'])
    data_event=Event().getAllEvents()
    return render_template("dashboard_user_isi_kehadiran.html", name_member=name_member, data_event=data_event)

@dashboard.route('/riwayat')
def dashboard_user_riwayat():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    name_member=Member().getFullname(session['masuk'])
    return render_template("dashboard_user_riwayat.html", name_member=name_member)

@dashboard.route('/logout')
def logout():
    if 'masuk' in session:
        session.pop('masuk')
        return redirect(url_for('login.login_user'))
    # elif 'admin' in session:
    #     session.pop('admin')
    #     return redirect(url_for('admin.login_admin'))