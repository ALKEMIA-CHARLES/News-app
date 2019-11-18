from app import app
import urllib.request,json
from app.models import news_articles, news_source
import requests

News = news_articles.News_Articles
NewsSources = news_source.NewsSources

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news_articles():
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

def get_news_by_source():
    source_results = requests.get('https://newsapi.org/v2/sources?apiKey=1b7e8d876a1d4b6d81cd805f238083f8').json()

    articles = []
    for item in source_results['sources']:
        identification = item['id']
        name = item['name']
        url = item['url']
        description =  item['description']
        source_object = NewsSources(identification, name, url, description)
        articles.append(source_object)
    return articles

def process_sources(sources_results_list):
    sources_results = []
    for source_item in sources_results_list:
        identification = source_item.get('id')
        name = source_item.get('name')
        url = source_item.get('url')
        description = source_item('description')
    # if image:
    #     source_object = News(identification, name, url)
    #     sources_results.append(source_object)
    
    return sources_results

