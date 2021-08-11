import unittest
from app.models import Source,Article

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the source class.
    '''

    def setUp(self):
        '''
        set up method that will run before every test 
        '''
        self.new_source=Source("abc","Abc news","this gives timely news","https://www.aljazeera.com/news/","private",)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behavior of the article class.
    '''
    def setUp(self):
        self.new_article=Article("BBC", "War" ,"Ethiopian PM Abiy Ahmed calls on civilians to join", "Tigray war" ,"Tigray crisis","https://www.bbc.com/news/world-africa-58163641","11/08/2021")

    def  test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))




if __name__=='__main__':
    unittest.main()