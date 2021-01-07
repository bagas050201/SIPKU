from flask import Flask, render_template, url_for, redirect, request, session, Blueprint
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename 
import os
from logincontroller import login
from model.member import Member
from model.event import Event
from model.presence import Presence
from model.log import Log

dashboard=Blueprint('dashboard', __name__, url_prefix='/')

@dashboard.route('/')
def dashboard_user():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))

    name_member=Member().getFullname(str(session['masuk']))
    photo=Member().getPhoto(str(session['masuk']))
    kehadiran=Member().getDataPresenceMember((session['masuk']))
    total_hadir=0
    total_thadir=0
    for hadir in kehadiran:
        if hadir['status']=="Hadir":
            total_hadir+=1
        else:
            total_thadir+=1
    return render_template("dashboard_user.html", name_member=name_member, hadir=total_hadir, thadir=total_thadir, photo=photo)

@dashboard.route('/profil')
def dashboard_user_profil():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    data=Member().getDataMember(str(session['masuk']))
    return render_template("dashboard_user_profil.html", name_member=data['fullname'], data_member=data)

@dashboard.route('/profil/update-photo', methods=["POST", "GET"])
def dashboard_user_updatephoto():
    if request.method=='POST':
        file=request.files['photo']
        try:
            filename=secure_filename(file.filename)
            file.save(os.path.join('static/uploads', filename))
        except:
            filename=""
        photo="../static/uploads/"+filename
        Member().setPhoto(str(session['masuk']), photo)
        Log().addLog(Member().getFullname(str(session['masuk']))+" memperbarui foto profil")
    return redirect (url_for('dashboard.dashboard_user_profil'))

@dashboard.route('/profil/update-data', methods=["POST", "GET"])
def update_data():
    if request.method=='POST':
        fullname=request.form['fullname']
        study=request.form['study']
        gen=request.form['gen']
        Member(str(session['masuk'])).updateMember(fullname, study, gen)
        Log().addLog(Member().getFullname(str(session['masuk']))+" memperbarui data profil")
        data=Member().getDataMember(str(session['masuk']))
        return render_template("dashboard_user_profil.html", name_member=data['fullname'], data_member=data, pesan=True)
    return redirect (url_for('dashboard.dashboard_user_profil'))

@dashboard.route('/isi-kehadiran')
def dashboard_user_kehadiran():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    name_member=Member().getFullname(str(session['masuk']))
    data_event=Event().getAllEvents()
    photo=Member().getPhoto(str(session['masuk']))
    # print(data_event)
    return render_template("dashboard_user_isi_kehadiran.html", name_member=name_member, data_event=data_event, photo=photo)

@dashboard.route('/isi-kehadiran/<id_event>')
def dashboard_user_kehadiran_isi(id_event):
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    kehadiran=Presence()
    id_member=str(session['masuk'])
    pesan=kehadiran.addPresenceMember(id_event, id_member)
    Log().addLog(Member().getFullname(str(session['masuk']))+" mengisi daftar hadir")

    name_member=Member().getFullname(str(session['masuk']))
    data_event=Event().getAllEvents()
    # return redirect(url_for('dashboard.dashboard_user_kehadiran', pesan=pesan))
    return render_template("dashboard_user_isi_kehadiran.html", name_member=name_member, data_event=data_event, pesan=pesan)
    

@dashboard.route('/riwayat')
def dashboard_user_riwayat():
    if('masuk' not in session):
        return redirect(url_for("login.login_user"))
    name_member=Member().getFullname(str(session['masuk']))
    kehadiran=Member().getDataPresenceMember(session['masuk'])
    photo=Member().getPhoto(str(session['masuk']))
    return render_template("dashboard_user_riwayat.html", name_member=name_member, kehadiran=kehadiran, photo=photo)

# ------------------------FOR ADMIN-----------------------------
@dashboard.route('/admin')
def dashboard_admin():
    if('admin' not in session):
        return redirect(url_for("login.login_user"))
    total_events=len(Event().getAllEvents())
    total_users=len(Member().getAllMembers())
    return render_template("dashboard_admin.html", tEvent=total_events, tUser=total_users)

@dashboard.route('/kelola-user')
def dashboard_admin_kelola_user():
    if('admin' not in session):
        return redirect(url_for("login.login_user"))
    members=Member().getAllMembers()
    return render_template("dashboard_admin_kelola_user.html", members=members)

@dashboard.route('/kelola-user/tambah', methods=["POST", "GET"])
def dashboard_admin_tambah():
    if request.method=='POST':
        id_member=request.form['id_member']
        fullname=request.form['fullname']
        study=request.form['study']
        gen=request.form['gen']
        password=request.form['password']
        Member().addMember(id_member, fullname, study, gen, password, "../static/img/unj.png")
    return redirect (url_for('dashboard.dashboard_admin_kelola_user'))

@dashboard.route('/kelola-user/edit', methods=["POST", "GET"])
def dashboard_admin_edit():
    if request.method=='POST':
        id_member=request.form['id_member']
        fullname=request.form['fullname']
        study=request.form['study']
        gen=request.form['gen']
        # password=request.form['password']
        Member(id_member).updateMember(fullname, study, gen)
    return redirect (url_for('dashboard.dashboard_admin_kelola_user'))

@dashboard.route('/kelola-user/hapus/<id_member>')
def dashboard_admin_hapus(id_member):
    Member().deleteMember(str(id_member))
    return redirect (url_for('dashboard.dashboard_admin_kelola_user'))

@dashboard.route('/kelola-acara')
def dashboard_admin_kelola_acara():
    if('admin' not in session):
        return redirect(url_for("login.login_user"))
    
    events=Event().getAllEvents()
    return render_template("dashboard_admin_kelola_acara.html", events=events)

@dashboard.route('/kelola-acara/tambah', methods=["POST", "GET"])
def dashboard_admin_tambahacara():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['description']
        date=request.form['date']
        time=request.form['time']
        file=request.files['poster']
        try:
            filename=secure_filename(file.filename)
            file.save(os.path.join('static/uploads', filename))
        except:
            filename=""
        poster="../static/uploads/"+filename
        # password=request.form['password']
        status=request.form['status']
        Event().addEvent(title, desc, poster, date, time, status)
        idEvent=Event().getId(title, desc, date, time)
        Presence().addPresence(str(idEvent), [])
    return redirect (url_for('dashboard.dashboard_admin_kelola_acara'))

@dashboard.route('/kelola-acara/edit', methods=["POST", "GET"])
def dashboard_admin_editacara():
    if request.method=='POST':
        id_event=request.form['id_event']
        title=request.form['title']
        desc=request.form['description']
        date=request.form['date']
        time=request.form['time']
        status=request.form['status']
        Event().updateEvent(id_event,title, desc, date, time, status)
    return redirect (url_for('dashboard.dashboard_admin_kelola_acara'))

@dashboard.route('/kelola-acara/hapus/<id_event>')
def dashboard_admin_hapusacara(id_event):
    Presence().deletePresence(str(id_event))
    Event().deleteEvent(str(id_event))
    return redirect (url_for('dashboard.dashboard_admin_kelola_acara'))

@dashboard.route('/daftar-hadir')
def dashboard_admin_daftar_hadir():
    if('admin' not in session):
        return redirect(url_for("login.login_user"))
    events=Event().getAllEvents()

    return render_template("dashboard_admin_daftar_hadir.html", events=events)

@dashboard.route('/daftar-hadir/<id_event>')
def dashboard_admin_daftar_hadir_detail(id_event):
    presences=Presence().getDataPresence(id_event)
    judul=Event(ObjectId(id_event)).getTitle()
    anggota=[]
    for member in presences['attendance']:
        angg=Member().getFullname(str(member))
        anggota.append(angg)
    return render_template("dashboard_admin_detail_hadir.html", title=judul, hadir=anggota)

@dashboard.route('/logout')
def logout():
    if 'masuk' in session:
        Log().addLog(Member().getFullname(str(session['masuk']))+" logout")
        session.pop('masuk')
        return redirect(url_for('login.login_user'))
    if 'admin' in session:
        session.pop('admin')
        return redirect(url_for('login.login_user'))
    # elif 'admin' in session:
    #     session.pop('admin')
    #     return redirect(url_for('admin.login_admin'))
