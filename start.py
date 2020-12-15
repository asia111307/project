__author__ = 'Asia Paliwoda'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from os import path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pr_db.db'

db = SQLAlchemy()
db.app = app
db.init_app(app)

app.static_path = path.join(path.abspath(__file__), 'static')

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

migrate = Migrate(app, db)

from models import *
create_engine('sqlite:///tmp/pr_db.db', convert_unicode=True)
db.create_all()
db.session.commit()

initiate_db_with_data()

from views import *

if __name__ == 'start':
    app.run(debug=True, host='0.0.0.0')

