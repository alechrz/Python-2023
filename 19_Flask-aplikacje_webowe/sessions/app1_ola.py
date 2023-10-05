from flask import Flask, session, render_template, request, redirect,url_for
from flask_session import Session

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'sessions'
app.config.from_object(__name__)
Session(app)

@app.route('/set/')
def set():
    session['name'] = request.args.get('name','')
    return redirect(url_for('get'))

@app.route('/get/')
def get():
    name=session['name']
    return render_template('form_ola.html', name=name, tytul="zmiana imienia")
 # return session.get('key', 'not set')