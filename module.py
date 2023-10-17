from flask import Flask
import redis

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_hash = set()
passwords = {"tt" : "123456", "dd" : "654321"}

# redis数据库
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# 账号密码 myhash
def add_user_code(name, code):
    r.hset('user_code', name, code)

def set_user_code(name, code):
    add_user(name, code)

def remove_user_code(name, code):
    r.hdel('user_code', name)

def get_user_code(name):
    return r.hget('user_code', name)

# 登录验证
def set_log_hash(hash):
    r.sadd('log_hash', hash)

def remove_log_hash(hash):
    r.srem('log_hash', hash)

def is_log_hash(hash):
    return r.sismember('log_hash', hash)
