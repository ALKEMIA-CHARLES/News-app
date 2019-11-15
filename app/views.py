from flask import render_template
from app import app
from app.requests import get_news_articles

# Views
@app.route('/')
def index():

    top_headlines =  get_news_articles()
    print(top_headlines)
    title = 'News app -  Welcome to the best news app in the world '
    return render_template('index.html' , title = title, top_headlines = top_headlines)

@app.route('/contactus')
def contactus():

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('contactus.html')