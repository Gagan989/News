class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCE_API='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_SOURCES_URL ='https://newsapi.org/v2/everything?q=apple&from=2021-08-10&to=2021-08-10&sortBy=popularity&apiKey=fe2e99be7ea24b9b9ad0000e6b90af33'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True