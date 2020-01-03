from app import app
from flask_login import login_required, current_user, login_user, login_manager
import datetime
from models.landing import Landing
from flask import request, flash, redirect, url_for, request, session
from flask import Blueprint, render_template
# from werkzeug.utils import secure_filename


landings_blueprint = Blueprint('landings',
                               __name__,
                               template_folder='templates')


@landings_blueprint.route('/new', methods=['POST'])
def new():
    email = request.form.get('email')
    size = request.form.get('size')
    subscription = request.form.get('subscription')
    landingpage = 'index'
    payment = request.form.get('payment')
    name = request.form.get('name')

    landing = Landing(email=email, size=size, subscription=subscription,
                      landingpage=landingpage, payment=payment, name=name)
    if landing.save():
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@landings_blueprint.route('/premium_nl', methods=['GET'])
def premium_nl():
    pass


@landings_blueprint.route('/sustainable_nl', methods=['POST'])
def sustainable_nl():
    pass


@landings_blueprint.route('/standard_nl', methods=['GET'])
def standard_nl():
    pass


# @landing_blueprint.route('/premium-de', methods=['GET'])
# def premium-de():
#     pass


# @landing_blueprint.route('/sustainable-de', methods=['POST'])
# def sustainable-de():
#     pass


# @landing_blueprint.route('/standard-de', methods=['GET'])
# def standard-de:
#     pass

@landings_blueprint.route('/premium_fr', methods=['GET'])
def premium_fr():
    pass


@landings_blueprint.route('/sustainable_fr', methods=['POST'])
def sustainable_fr():
    pass


@landings_blueprint.route('/standard_fr', methods=['GET'])
def standard_fr():
    pass

# @landing_blueprint.route('/premium-es', methods=['GET'])
# def premium-es():
#     pass


# @landing_blueprint.route('/sustainable-es', methods=['POST'])
# def sustainable-es():
#     pass


# @landing_blueprint.route('/standard-es', methods=['GET'])
# def standard-es():
#     pass


# @landing_blueprint.route('/premium-en', methods=['GET'])
# def premium-en():
#     pass


# @landing_blueprint.route('/sustainable-en', methods=['POST'])
# def sustainable-en():
#     pass


# @landing_blueprint.route('/standard-en', methods=['GET'])
# def standard-en():
#     pass


@landings_blueprint.route('/premium_uk', methods=['GET'])
def premium_en():
    pass


@landings_blueprint.route('/sustainable_uk', methods=['POST'])
def sustainable_en():
    pass


@landings_blueprint.route('/standard_uk', methods=['GET'])
def standard_en():
    pass
