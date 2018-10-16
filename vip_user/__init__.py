from flask import Blueprint

vip_user = Blueprint('vip_user',__name__,static_folder='static',
                    static_url_path='/static',template_folder='templates')

from . import views