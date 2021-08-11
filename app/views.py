from flask import render_template
from app import app
from .request import get_sources, search_source



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

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the  source search results
    '''
    source_name_list=source_name.split(" ")
    source_name_format="+".join(source_name_list)
    searched_sources=search_source(source_name_format)
    title=f'search result for {source_name}'

    return render_template('search.html',sources=searched_sources)