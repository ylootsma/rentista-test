from app import app
from flask import render_template, flash
from rentista_web.blueprints.landings.views import landings_blueprint
from rentista_web.blueprints.emails.views import emails_blueprint
from werkzeug.utils import secure_filename
from flask_assets import Environment, Bundle
from .util.assets import bundles
from flask_login import login_required, current_user, login_user
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
import os
import config


assets = Environment(app)
assets.register(bundles)

app.register_blueprint(landings_blueprint, url_prefix="/landings")
app.register_blueprint(emails_blueprint, url_prefix="/emails")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/", methods=['POST', 'GET'])
def home():

    return render_template('home.html')
