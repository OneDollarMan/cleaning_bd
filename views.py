from __init__ import app
from flask import render_template
import repo

r = repo.Repo(host=app.config['HOST'], user=app.config['USER'], password=app.config['PASSWORD'], db=app.config['DB'])


@app.route("/")
def index():
    return render_template('index.html', title="Главная")
