from flask import Flask,\
                escape,\
                url_for
# 找到 project/__init__.py 中的blueprint
from project import *
# 创建 flask app
# param: instance_relative_config 从instance/config.py读取
app = Flask(__name__, instance_relative_config=True)

# 加载 instance/config.py
app.config.from_object('config')
app.config.from_pyfile('config.py')          

# 注册蓝图
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(learn, url_prefix='/learn')

@app.route('/')
def main_page():
    return "main page"

if __name__ == '__main__':
    app.run()