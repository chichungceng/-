from . import normal_user

@normal_user.route('/')
@normal_user.route('/index')
def index():
    return "普通用户的主页"

# 还有很多其他关于普通用户的页面，可以写在这里。