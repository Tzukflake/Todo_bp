from flask import Blueprint, render_template, request

from marshmallow import ValidationError

bp = Blueprint('hello', __name__)

@bp.route('/')
def show_login_form():
    return render_template('login_form.html')













