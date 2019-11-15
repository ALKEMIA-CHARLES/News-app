class Config:
 NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=za&apiKey=1b7e8d876a1d4b6d81cd805f238083f8'

    



class ProdConfig(Config):

    
    pass


class DevConfig(Config):
 
    DEBUG = True