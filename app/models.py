class News_Articles:

    def __init__(self,title, content,image, publishedAt, url):
        
        self.title = title
        self.content =  content
        self.image =  image
        self.publishedAt = publishedAt
        self.url = url

class NewsSources:

    def __init__(self, id, name, url, description ):
        self.id = id
        self.name =  name
        self.url = url
        self.description = description