"""
Example of a one-file Flask application
that uses an API and ORM (SQLAlchemy).
FLASK_APP='space_app.py' flask run
"""

# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
# TODO figure out requests

# Set up app/db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)


class Astronauts(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    num_astronauts = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return '# of astronauts: {}'.format(self.num_astronauts)


# reading from db
@app.route('/')
def root():
    astro_data = Astronauts.query.all()[0]
    num_astronauts = astro_data.num_astronauts
    return 'There are {} astronauts in space right now!'.format(num_astronauts)


@app.route('/refresh')
def refresh():
    # Very simple proof of concept, wouldn't want to always reset db
    # Create Schema
    DB.drop_all()
    DB.create_all()
    # Connect to the API
    request = requests.get('http://api.open-notify.org/astros.json')
    astro_data = request.json()
    num_astronauts = astro_data['number']
    # Store in db
    record = Astronauts(num_astronauts=num_astronauts)
    DB.session.add(record)
    DB.session.commit()
    return str(Astronauts.query.all())
