from flask import abort, redirect, url_for, request, make_response, Flask
from datetime import datetime, timedelta
import hashlib
import os
app = Flask('__name__')

def generate_login_hash():
    random_bytes = os.urandom(32)  # 32 bytes = 256 bits
    result = hashlib.sha256(random_bytes).hexdigest()
    return result

def set_cookie():
    tem_hash = generate_login_hash()
    resp = make_response(f'Setting cookie')
    expires = datetime.now() + timedelta(days=1)
    resp.set_cookie('loghash', tem_hash, expires=expires)
    resp.set_cookie('username', request.form['username'])
    return (tem_hash,resp)