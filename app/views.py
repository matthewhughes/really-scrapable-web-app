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
