from app import app
import urllib.request,json
from app.models import news_articles, news_source

News = news_articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        title = news_item.get('title')
        content = news_item.get('content')
        image = news_item.get('image_path')
        publishedAt = news_item.get('publishedAt')

        if image:
            news_object = News(title,content,image, publishedAt)
            news_results.append(news_object)

    return news_results