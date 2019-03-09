from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd

app = Flask(__name__)

# Create an engine to a SQLite database
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///visual_data.sqlite"

#db = SQLAlchemy(app)

# reflect an existing database into a new model
#Base = automap_base()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///visual_data.sqlite"
db = SQLAlchemy(app)



# reflect an existing database into a new model
Base = automap_base()
Base.prepare(db.engine, reflect=True)
data = Base.classes.visual_data
# reflect the tables


# Save reference to the tables

#session = scoped_session(sessionmaker(bind=engine))

# Create our session (link) from Python to the DB
#session = scoped_session(sessionmaker(bind=engine))

# Flask Routes
@app.route("/")
def home():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/test")
def test():
    """Testing to see if this works"""
    stmt = db.session.query(data)


if __name__ == "__main__":
    app.run(debug=True)