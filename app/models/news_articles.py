class News_Articles:

    def __init__(self, title, content,image, publishedAt):
        self.title = title
        self.content =  content
        self.image = 'http://cdn.24.co.za/files/Cms/General/d/6124/3cbd0a62e7af4742930462ff468844b6.jpg' + image
        self.publishedAt = publishedAt