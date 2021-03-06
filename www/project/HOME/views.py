from . import home
from flask import Flask,\
                escape,\
                url_for
    
# /home    
@home.route('/')
def show():
    return 'This is Book page.'


# /home/etc/xxx
@home.route('/etc/<var>') 
def etc_page(var):
    return 'User: %s' % escape(var)

# /home/test
@home.route('/test')
def test_url_for():
    print(url_for('etc_page', var='greyli')) 
    print(url_for('etc_page', var='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', whatever=2))  # /test?num=2
    return 'Test page'
