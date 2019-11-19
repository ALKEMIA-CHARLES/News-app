import unittest
from app.models import news_source
News = news_source.News

class News_Sources_Test(unittest.TestCase):

    def setUp(self):
        self.new_news_sources = News("the-verge", "The Verge", "https://www.theverge.com/2019/11/15/20966237/google-chrome-white-tab-screen-crash-experiment-it-admins")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_sources,News))

if __name__ == '__main__':
    unittest.main()