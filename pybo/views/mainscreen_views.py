import functools

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from .. import db
from ..forms import UserCreateForm, UserLoginForm
from ..models import User

bp = Blueprint('mainscreen', __name__, url_prefix='/mainscreen')

@bp.route('/mainscreen/', methods=('GET', 'POST'))




def mainscreen():

    return render_template('mainscreen/mainscreen.html')