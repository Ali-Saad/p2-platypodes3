"""crossover will provide API on warming projections based on certain policies"""
from flask import Blueprint, render_template, Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

import model

members_crossover_bp = Blueprint('crossover', __name__, static_folder="static", template_folder="templates")

app = Flask(__name__)
db = SQLAlchemy()
dbURI = 'sqlite:///model/projections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)


class Data(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    policy = db.Column(db.String(50))
    projection = db.Column(db.Integer)
    paris_agreement = db.Column(db.String(50))

    def json(self):
        return {
            "id": self.id,
            "policy": self.policy,
            "projection": self.projection,
            "paris_agreement": self.paris_agreement
        }

    class Create(Resource):
        def post(self, policy, projection, paris_agreement):
            person = model_create(policy, projection, paris_agreement)
            if person:
                return person.json()
            return {'failed': None}, 404

    api.add_resource(Create, '/create/<string:policy>/<int:projection>/<string:paris_agreement>')


def model_create(policy, projection, paris_agreement):
    """prepare data for primary table extracting from form"""
    try:
        stat = Data(
            policy=policy,
            projection=projection,
            paris_agreement=paris_agreement
        )
        db.session.add(stat)
        db.session.commit()
        return stat
    except:
        return None


def model_read_all():
    """convert Users table into a list of dictionary rows"""
    stats = Data.query.all()
    return [stat.json() for stat in stats]


@members_crossover_bp.route("/")
def crossover():
    return render_template("crossover.html", model=model.setup())


@members_crossover_bp.route('/projections')
def display():
    """extracts Users table from DB and returns in json format"""
    records = model_read_all()
    return render_template("projections.html", table=records)


@members_crossover_bp.route('/data')
def data():
    stats = Data.query.all()
    list = [stat.json() for stat in stats]
    return {"list": list}


if __name__ == "__main__":
    db.create_all()

