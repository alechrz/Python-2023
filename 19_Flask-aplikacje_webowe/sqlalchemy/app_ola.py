# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "top_secret"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.tagname
        # return '<Tag %r>' % self.tagname


def get_tag(session):
    return session.query(Tag).all()

def create_tag(name, session):
    try:
        tag = Tag(tagname=name)
        session.add(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True

def delete_tag(name, session):
    try:
        tag = Tag.query.filter_by(tagname=name).first()
        session.delete(tag)
        session.commit()
        return True
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False


@app.route('/')
def hello():
    return render_template('form.html', data=get_tag(db.session),
                           tytul="Tagi", no_error=True)


@app.route('/add')
def add():
    args = request.args
    no_error = create_tag(args["name"], db.session)
    if no_error:
        tytul = "Dodano tag"
        flash("Dodano tag!")

    else:
        tytul = "Taki tag już istnieje"
        flash("Taki tag juz istnieje.")
    return render_template('form_ola.html', data=get_tag(db.session),
                           no_error=no_error,
                           tytul=tytul)

@app.route('/remove', methods=['POST'])
def remove():
    no_error = delete_tag(request.form["name"], db.session)
    tytul = "Usunieto tag" if no_error else "Taki tag nie istnieje"
    flash(tytul)
    return render_template('form_ola.html', data=get_tag(db.session),
                           no_error=no_error,
                           tytul=tytul)








