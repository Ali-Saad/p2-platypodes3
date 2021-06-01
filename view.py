from flask import Flask, render_template, request
import model
import sqlite3 as sl3

# import stats
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

# import sqlite3 as sl3
from subs import new

# Blueprints
app = Flask(__name__)
app.register_blueprint(members_navodit_bp, url_prefix='/navodit')
app.register_blueprint(members_pragadeesh_bp, url_prefix='/pragadeesh')
app.register_blueprint(members_ali_bp, url_prefix='/ali')
app.register_blueprint(members_ayman_bp, url_prefix='/ayman')
app.register_blueprint(members_mustafa_bp, url_prefix='/mustafa')


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
    return render_template("faq.html", model=model.setup())


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


@app.route("/subscribe/", methods=["POST"])
def subscribe():
    return new(request)
    return render_template("home.html")