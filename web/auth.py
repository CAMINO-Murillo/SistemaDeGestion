from flask import Blueprint, redirect, url_for, request, flash, Response
from flask import json
from flask.json import jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from web.models import User

auth = Blueprint('auth', __name__)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout'


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    # TODO: Request the complete data from forms

    # TODO: Check if the user already exists and redirect to
    # return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password))

    # TODO: add the new user to the database

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')
    
    if name == "yo" and password == "hey":
        return jsonify({"status": "logged in"})
    return Response(json.dumps({"status": "not logged in"}), status=400, mimetype='application/json')
