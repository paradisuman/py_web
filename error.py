from flask import url_for , Flask, redirect
app = Flask(__name__)

@app.errorhandler(404)
def page_not_find(error):
    return render_template('page_404.html'), 404


@app.errorhandler(401)
def unauth():
    return redirect(url_for('login'))
