from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from random import randint
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Jolomi\\Documents\\NCIRL\\DevSecOps\\App\\sqlite\\test.db'
db =SQLAlchemy(app)

class Volunteers(db.Model):
    volunteerid = db.Column(db.Integer(), primary_key=True)
    volunteername = db.Column(db.String(50))
    volunteeremail = db.Column(db.String(50))
    volunteermessage = db.Column(db.String(200))

    def __repr__(self):
        return f"Clients('{self.volunteerid}','{self.volunteername}','{self.volunteeremail}','{self.volunteeremail}')"


with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():

    return render_template('index.html')


@app.route("/join")
def join():

    return render_template('join.html')


@app.route("/about")
def about():

    #send input to DB
    # db.session.add(
    #     volunteerid = randint(0, 100000),
    #     volunteername = name,
    #     volunteeremail = email        
    # )
    # db.session.commit()

    return render_template('about.html')


@app.route("/database")
def database():
    #return all volunteers in db
    return render_template('database.html', volunteers = Volunteers.query.all())



