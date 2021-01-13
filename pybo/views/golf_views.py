import functools

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from .. import db
from ..forms import UserCreateForm, UserLoginForm
from ..models import User

bp = Blueprint('golf', __name__, url_prefix='/golf')

@bp.route('/golfrule/', methods=('GET', 'POST'))




def golfrule():

    return render_template('golf/golfrule.html')
