from flask import url_for , Flask, redirect, render_template
from module import *

@app.errorhandler(404)
def page_not_find(error):
    return render_template('page_404.html'), 404


@app.errorhandler(401)
def unauth():
    return redirect(url_for('login'))
