from flask import (
    Blueprint, render_template, request
)


bp = Blueprint('main_page', __name__, url_prefix='/main_page')


@bp.route('/')
def index():
    return render_template('index.html')

