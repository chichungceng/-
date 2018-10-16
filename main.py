from flask import Flask
from normal_user import normal_user
from vip_user import vip_user

app = Flask(__name__,static_folder='static',template_folder='templates')

app.register_blueprint(normal_user,url_prefix='/normal_user')
app.register_blueprint(vip_user,url_prefix='/vip_user')

@app.route('/')
@app.route('/index')
def index():
    return "网站的首页"

# 还有很多关于主页的视图函数，写在这里。

if __name__ == '__main__':
    app.run(debug=True)