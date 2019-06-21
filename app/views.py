from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message='Home-welcome to the best News Highlights online'
    return render_template('index.html',message=message)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View Newse page function that returns the News details page and its data
    '''
    return render_template('news.html',id = news_id)