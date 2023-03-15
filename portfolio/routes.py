from flask import render_template
from portfolio import app, db
from portfolio.models import Users


@app.route("/")
def home():
    return render_template("home.html")
