import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

def setUp(self):
     '''
        Set up method that will run before every Test
        '''
        self.new_news = News(   "id": "abc-news",
                                "name": "ABC News",
                                "description": "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
                                "url": "https://abcnews.go.com",
                                "category": "general",
                                "language": "en",
                                "country": "us")
       

def test_instance(self):
    self.assertTrue(isinstance(self.new_news,News))
        


if __name__ == '__main__':
    unittest.main()