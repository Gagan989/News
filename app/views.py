from flask import render_template
from app import app
from .request import get_sources

sourceSamples =get_sources()


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - News-site'
    return render_template('index.html',title=title, sourceList=sourceSamples)