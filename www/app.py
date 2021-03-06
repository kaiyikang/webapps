from flask import Flask,\
                escape,\
                url_for
                
# 创建 flask app
# param: instance_relative_config 从instance/config.py读取
app = Flask(__name__, instance_relative_config=True) 
app.config.from_object('config')
app.config.from_pyfile('config.py')


# ETC PAGE
@app.route('/etc/<var>') 
def etc_page(var):
    return 'User: %s' % escape(var)


@app.route('/test')
def test_url_for():
    print(url_for('main_page'))  # /
    print(url_for('etc_page', var='greyli')) 
    print(url_for('etc_page', var='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', whatever=2))  # /test?num=2
    return 'Test page'

@app.route('/')
def main_page():
    return "main page"

if __name__ == '__main__':
    app.run()