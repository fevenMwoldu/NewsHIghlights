from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_sources,get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Retrieve sources from news api
    sources= get_news_sources()

    return render_template('index.html',sources=sources)

@main.route('/articles/<string:source_id>')
def articles(source_id):
    '''
    View Newse page function that returns the News details page and its data
    '''

    # Retrieve articles for source_id
    articles = get_articles(source_id)

    return render_template('articles.html', articles = articles)








