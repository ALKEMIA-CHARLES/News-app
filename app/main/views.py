from flask import render_template, redirect, url_for, request
from .import main
from ..request import get_news_articles, get_news_by_source



@main.route('/')
def index():

    top_headlines =  get_news_articles()

    title = 'News app -  Welcome to the best news app in the world '
    return render_template('index.html' , title = title, top_headlines = top_headlines)


@main.route('/source')
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

@main.route('/contactus')
def contactus():

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('contactus.html')