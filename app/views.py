from flask import render_template
from app import app

homepage = ''' 
<h2>Really Scrapable Web App is a tool to learn about data science</h1>
<p>Super cool, right? There are lots of things to scrape on this website. But let's start off easy.</p>
<h1>Write a scraper that yanks this line and prints it to the console </h1>
'''

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
