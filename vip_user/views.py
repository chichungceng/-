from . import vip_user

@vip_user.route("/")
@vip_user.route("/index")
def index():
    return "尊贵的会员主页"

# 这里还可以写有关于会员用户的页面