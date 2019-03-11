from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd

app = Flask(__name__)

# Create an engine to a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pitchingdata.sqlite"

db = SQLAlchemy(app)

# reflect an existing database into a new model
#Base = automap_base()

#aut0map bae only works with a primary key - so need to make sure there is a primary key
Base= automap_base()

#engine= create_engine('sqlite:///pitchingdata.sqlite')

Base.prepare(db.engine, reflect=True)

Visualdata= Base.classes.visualdata





# Flask Routes
@app.route("/")
def home():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/test")
def test():

    #FLASK APP WORKS!!!
    """Testing to see if this works"""
    #need to write a better query but should work

    stmt = db.session.query(Visualdata).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.pitch_name[:50]))

#@app.route("/sample")
#def sample():

    #stmt = db.session.query(Visualdata).statement
    #df = pd.read_sql_query(stmt, db.session.bind)

   # sample = df.loc[df.pitch_name == 'Changeup']

    #data = [sample.values.tolist()]

    #return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)