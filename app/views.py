from flask import render_template
from app import app
from .request import get_sources



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sourceSamples =get_sources()
    title = 'News'
    return render_template('index.html',title=title, sourceList= sourceSamples)

@app.route('/source/<id>')
def source(id):
    '''
    View source page function that returns the source details page and its data
    '''
    source=get_sources(id)
    title=f'{source.title}'
    return render_template('source.html',title=title,source=source)