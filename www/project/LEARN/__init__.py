from flask import Blueprint

learn = Blueprint(
    'learn',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views
