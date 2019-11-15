import unittest
import app.models
from app.models import news_articles
News = news_articles.News

class News_Articles_Test(unittest.TestCase):

    def setUp(self):
        self.new_news_articles = News("SAA plays hardball as strike starts - Fin24",'https://www.fin24.com/Companies/TravelAndLeisure/saa-plays-hardball-as-strike-starts-20191115')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_articles,News))

if __name__ == '__main__':
    unittest.main()
