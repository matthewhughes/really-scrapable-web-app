from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/challengeone')
def challengeone():
    return render_template('challengeone.html')

@app.route('/challengetwo')
def challengetwo():
    return render_template('challengetwo.html')

@app.route('/challengethree')
def challengethree():
    return render_template('challengethree.html')

@app.route('/challengefour')
def challengefour():
    return render_template('challengefour.html')

@app.route('/api/<standard>')
def api(standard):
    if standard == 'json':
        return "json"
    elif standard == 'xml':
        return "xml"
    else:
        return "Wrong type"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
