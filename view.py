from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# import json
import model
from subs import new
import storefb
import storesignup
# import storelogin
from mapalgo import Color
# Import Blueprints
from members.navodit import members_navodit_bp
from members.pragadeesh import members_pragadeesh_bp
from members.ayman import members_ayman_bp
from members.ali import members_ali_bp
from members.mustafa import members_mustafa_bp
from flask_migrate import Migrate
from flask_restful import Resource, Api

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
# import sqlite3 as sl3

app = Flask(__name__)
db = SQLAlchemy()
dbURI = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)
app.register_blueprint(members_navodit_bp, url_prefix='/navodit')
app.register_blueprint(members_pragadeesh_bp, url_prefix='/pragadeesh')
app.register_blueprint(members_ali_bp, url_prefix='/ali')
app.register_blueprint(members_ayman_bp, url_prefix='/ayman')
app.register_blueprint(members_mustafa_bp, url_prefix='/mustafa')


class Info(db.Model):  # Basic Info Database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    carbon_footprint = db.Column(db.Integer)
    paris_agreement = db.Column(db.String(50))

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "carbon_footprint": self.carbon_footprint,
            "paris_agreement": self.paris_agreement
        }

    # class for create/post
    class Create(Resource):
        def post(self, name, carbon_footprint, paris_agreement):
            country = model_create(name, carbon_footprint, paris_agreement)
            if country:
                return country.json()
            return {'failed': None}, 404  # need to have better message on errors

    api.add_resource(Create, '/api/add_info/<string:name>/<int:carbon_footprint>/<string:paris_agreement>')


def model_create(name, carbon_footprint, paris_agreement):
    """prepare data for primary table extracting from form"""
    try:
        country = Info(
            name=name,
            carbon_footprint=carbon_footprint,
            paris_agreement=paris_agreement
        )
        db.session.add(country)
        db.session.commit()
        return country
    except:
        return None


@app.route('/blueprint/')
def blue_route():
    return render_template("blueprint.html", model=model.setup())


# main home pages
@app.route('/')  # app routes to various html pages that we have assigned it to
def home_route():
    return render_template("home.html", model=model.setup())


@app.route('/aboutus/')
def about_route():
    return render_template("aboutus.html", model=model.setup())


# lock screen test
@app.route('/lock/')
def lock_route():
    return render_template("lock.html", model=model.setup())


# info app routes
@app.route('/info/')
def info_route():
    return render_template("information.html", model=model.setup())


@app.route('/info/faq/')
def faq_route():
    return render_template("faq.html", model=model.Faq())


# experimenting with backend above


@app.route('/info/prevention/')
def prevent_route():
    return render_template("prevention.html", model=model.setup())


@app.route('/info/trends/')
def trends_route():
    return render_template("trends.html", model=model.setup())


@app.route('/login/')
def login_route():
    return render_template("login.html", model=model.setup())


@app.route('/login', methods=['POST'])
def login():
    mailadd = request.form['email']
    psswrd = request.form['psw']

    print('Login Page Username:', mailadd)
    print('Login Page Password:', psswrd)
    result = storesignup.logincheck(mailadd, psswrd)
    if result == "yes":
        return render_template("home.html", model=model.setup())
    else:
        return render_template("login.html", msg='Invalid Username or Password', model=model.setup())


@app.route('/register/')
def register_route():
    return render_template("register.html", model=model.setup())


@app.route('/sign_up', methods=['POST'])
def sign_up():
    mailadd = request.form['email']
    psswrd = request.form['psw']
    pssrep = request.form['psw-repeat']

    storesignup.insertsignup(mailadd, psswrd, pssrep)
    '''
    print (fname)
    print (lname)
    print (mailid)
    print(service)
    print(opinion)
    '''
    return render_template("login.html", model=model.setup())


@app.route('/feedback/')
def fb_route():
    return render_template("feedback.html", model=model.setup())


@app.route('/feedback_form', methods=['POST'])
def feedback_form():
    fname = request.form['firstname']
    lname = request.form['lastname']
    mailid = request.form['email']
    service = request.form['type']
    opinion = request.form['feedback']
    storefb.insertfeedback(fname, lname, mailid, service, opinion)
    '''
    print (fname)
    print (lname)
    print (mailid)
    print(service)
    print(opinion)
    '''

    return render_template("misc/confirmation.html", model=model.setup())


@app.route('/tosandp/')
def ts_route():
    return render_template("misc/tos&p.html", model=model.setup())


@app.route('/cookies/')
def jar_route():
    return render_template("misc/cookies.html", model=model.setup())


@app.route('/qstat/')
def qstat_route():
    return render_template("qstat.html", model=model.setup())


@app.route('/userdashboard/')
def userdashboard_route():
    return render_template("userdashboard.html", model=model.setup())


@app.route('/templates/SomeFAQ/')
def SomeFAQ():
    return render_template("SomeFAQ.html", model=model.setup())


@app.route("/map/", methods=["GET", "POST"])
def map():
    if request.form:
        return render_template("map.html", color=Color(request.form.get("int")))
    return render_template("map.html", color=Color(200))


""""bot = ChatBot("Candice")
bot.set_trainer(ListTrainer)
bot.train(['What is your name?', 'My name is Candice'])
bot.train(['Who are you?', 'I am a bot' ])
bot.train(['I have some questions', 'resort to our FAQ and informational pages to find your answers linked below', 'Platypodes', 'You?'])
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

@app.route("/templates/candicebot/")
def candicebot():
    return render_template("candicebot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))"""


@app.route('/memes/')
def meme_route():
    return render_template("meme.html")


@app.route("/subscribe/", methods=["POST"])
def subscribe():
    return new(request)
    return render_template("home.html")


@app.route('/hotspots/')
def hot_route():
    return render_template("hotspot.html")


'''@app.route('/api/add_info', methods=['POST'])
def add_info():
    info_data = request.get_json()
    print(info_data)

    new_info = Info(name=info_data['name'], carbon_footprint=info_data['carbon_footprint'],
                    paris_agreement=info_data['paris_agreement'])

    db.session.add(new_info)
    db.session.commit()

    return 'Done', 201'''


@app.route('/api/info')
def info():
    countries = Info.query.all()
    list = [country.json() for country in countries]
    return {"list": list}


if __name__ == "__main__":
    db.create_all()
