# flask --app app2 run
#
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    name='wor'
    return render_template('form_ola.html', name=name, tytul="To jest tytul z parametru")


@app.route('/add')
def add():
    args = request.args
    print(args)
    name=args.get('name','')

    return render_template('form_ola.html', name=name, tytul="Dodano pozycję do listy")