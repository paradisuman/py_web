import func
from error import *

from flask import Flask
from flask import request
from flask import url_for 
from flask import render_template
from flask import session
from flask import make_response, abort, redirect, render_template
from functools import wraps
from markupsafe import Markup
from markupsafe import escape


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_hash = set()
passwords = {"tt" : "123456", "dd" : "654321"}


def valid_login (name, password):
    if passwords[name] == password:
        return True
    else:
        return False

def require_auth(fun):
    @wraps(fun)
    def decorator(*args, **kwargs):
        hash_ = request.cookies.get('loghash') 
        print(hash_)
        if hash_ not in login_hash:
            return unauth()
        else: return fun(*args, **kwargs)
    
    return decorator  

# cookie和index
@app.route('/')
@require_auth
def index():
    resp = make_response(render_template('index.html', username=request.cookies.get('username')))
    return resp


@app.route('/logout')
@require_auth
def logout():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('loghash', '', expires=0)
    resp.set_cookie('username', '', expires=0)
    return resp


# 文件下载
@app.route('/upload', methods=['GET', 'POST'])
@require_auth
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f'/var/www/uploads/{file.filename}')
    return render_template('upload.html')


# 使用login
# searchword = request.args.get('key', '')
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return_val = func.set_cookie()
            login_hash.add(return_val[0])
            resp = return_val[1]
            resp.data = render_template('index.html', username=request.form['username'])
            return resp
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


# 模板使用

@app.route('/hello/')
@app.route('/hello/<name>')
@require_auth
def hello(name=None):
    return render_template('hello.html', name=name)

# 转发
@app.route('/destination/<des>')
@require_auth
def destination(des):
    return render_template(f'{des}.html')  # assuming you have a template named destination.html

if __name__ == '__main__':
    app.run()

