import os

class Config:
    '''
    General configurations setting class 
    '''
    NEWS_SOURCE_API='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_SOURCES_URL ='https://newsapi.org/v2/everything?q=apple&from=2021-08-10&to=2021-08-10&sortBy=popularity&apiKey=fe2e99be7ea24b9b9ad0000e6b90af33'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Args:
         general configuration class from which the child class inherits configurations settings.
    '''
    pass
class DevConfig(Config):
    '''
    development configuration settings class
    Args:
         general configuration class from which the child class inherits configurations settings.
    '''
    DEBUG=True


config_options = {
'development':DevConfig,
'production':ProdConfig
}