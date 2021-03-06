from flask import render_template
from . import learn

@learn.route("/")
def index():
    return render_template('index.html')