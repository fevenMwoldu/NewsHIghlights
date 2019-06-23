from flask import render_template
import urllib.request,json
from app import app
from .models.source import Source, Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the sources url
sources_url = app.config["SOURCES_API_URL"]

# Getting the articles url
articles_url = app.config["ARTICLES_API_URL"]

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Retrieve sources from news api
    sources= get_news_sources()

    return render_template('index.html',sources=sources)


def get_news_sources():
    # make news api call to retrieve news sources

    '''
    Function that gets the json response to our url request
    '''
    get_news_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)

        sources_results=None

        if get_sources_response['sources']:
            sources_list = get_sources_response['sources']
            sources_results = process_results(sources_list)

    return sources_results

def process_results(sources_list):
    sources_result=[]
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        source_object=Source(id,name,description,url,category,language,country)
        sources_result.append(source_object)
        

    return sources_result

@app.route('/articles/<string:source_id>')
def articles(source_id):
    '''
    View Newse page function that returns the News details page and its data
    '''

    # Retrieve articles for source_id
    articles = get_articles(source_id)

    return render_template('articles.html', articles = articles)

def get_articles(source_id):

    get_articles_url = articles_url.format(source_id,api_key)

    with urllib.request.urlopen(get_articles_url)as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)
        articles_results=None

        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list)

    return articles_results


  
def process_articles_results(articles_list):
        articles_result=[]
        for article_item in articles_list:
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            content = article_item.get('content')

            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            articles_result.append(article_object)

        return articles_result



