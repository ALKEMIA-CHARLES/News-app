from app import app
import urllib.request,json
from app.models import news_articles, news_source
import requests

News = news_articles.News_Articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news_articles():
    '''
    Function that gets the json response to our url request
    '''
    # get_news_url = base_url.format(api_key)
    news_results = requests.get('https://newsapi.org/v2/top-headlines?country=za&apiKey=1b7e8d876a1d4b6d81cd805f238083f8').json()
    
    articles =[]
    for item in news_results['articles']:
        title = item['title']
        content = item['content']
        image = item['urlToImage']
        publishedAt = item['publishedAt']

        news_object = News(title,content,image,publishedAt)
        articles.append(news_object)
    return articles

def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        title = news_item.get('title')
        content = news_item.get('content')
        image = news_item.get('image_path')
        publishedAt = news_item.get('publishedAt')

    if image:
        news_object = News(title,content,image,publishedAt)
        news_results.append(news_object)

    return news_results