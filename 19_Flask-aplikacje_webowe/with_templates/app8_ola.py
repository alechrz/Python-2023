# flask --app app2 run
#
from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('select_ola.html', data=data, tytul="To jest tytul z parametru")


@app.route('/add', methods=['POST'])
def add():
    received = request.form  # a multidict containing POST data
    print(received)
    print(received['key'])
    print(received['val'])

    if any(received['key'] == d['key'] for d in data):
        print('istnieje')

        for d in data:
            for k, v in d.items():
                if v == received['key']:

                    d['value'] = received['val']
    else:
        data.append({'key': received['key'], 'value': received['val']})
        # print(data)
    # data.append({'key': received['key'], 'value': received['value']})
    return render_template('select_ola.html', data=data, tytul="Dodano pozycję do listy")


@app.route('/remove', methods=['POST'])
def remove():
    global data
    received = request.form  # a multidict containing POST data
    print(received)
    print(received['values'])
    data = [ x for x in data if x["key"]!=received['values']]
    return render_template('select_ola.html', data=data, tytul="Usunieto pozycję do listy")