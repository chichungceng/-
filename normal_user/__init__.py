from flask import Blueprint

normal_user = Blueprint('normal_user',__name__,
                        static_folder='static',
                        static_url_path='/static',
                        template_folder='templates')

from . import views