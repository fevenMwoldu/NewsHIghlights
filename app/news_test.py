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
        self.new_news = News('bbc-news',
                             'BBC News',
                             'BBC News',
                             'Spains top court decides if sex gang were rapists',
                             'Prosecutors are calling for five men known as the \"wolf pack\" to have their jail terms doubled.',
                             'http://www.bbc.co.uk/news/world-europe-48716940',
                             'https://ichef.bbci.co.uk/images/ic/1024x576/p075hcbd.jpg',
                             '2019-06-21T11:43:35Z',
                             'Media captionActivists say rage over Spain..... ')
       

def test_instance(self):
    self.assertTrue(isinstance(self.new_news,News))
        


if __name__ == '__main__':
    unittest.main()