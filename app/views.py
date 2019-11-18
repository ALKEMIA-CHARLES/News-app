from flask import render_template
from app import app
from app.requests import get_news_articles, get_news_by_source

# Views
@app.route('/')
def index():

    top_headlines =  get_news_articles()
    title = 'News app -  Welcome to the best news app in the world '
    return render_template('index.html' , title = title, top_headlines = top_headlines)


@app.route('/source')
def source():
    top_headlines_by_source = get_news_by_source()
    categories = ["business",
                "entertainment",
                "health",
                "science",
                "sports",
                "technology"]

    return render_template("source.html", 
                        sources = top_headlines_by_source,
                        categories =  categories 
                        )

@app.route('/contactus')
def contactus():

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('contactus.html')