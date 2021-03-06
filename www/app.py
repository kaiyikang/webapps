from flask import Flask,\
                escape,\
                url_for
# 找到 __init__中的home
from project.HOME import home

# 创建 flask app
# param: instance_relative_config 从instance/config.py读取
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')          

# 注册
app.register_blueprint(home, url_prefix='/home')


@app.route('/')
def main_page():
    return "main page"

if __name__ == '__main__':
    app.run()