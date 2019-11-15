class Config:
 NEWS_API_BASE_URL = 'https://newsapi.org/account'

    



class ProdConfig(Config):

    
    pass


class DevConfig(Config):
 
    DEBUG = True