import uuid
import datetime

from models.post import Post
from monogoDB import Database


class Blog(object):

    def __init__(self,author,title,description,id = None):
        self.author = author
        self.title = title
        self.description  = description
        self.id = uuid.uuid4().hex if id is None else id

    def newPost(self):
        title  = input("Enter post title : ")
        author = self.author
        content = input("Enter post content : ")
        date = input("Enter post date(in format DDMMYYYY), or leave blank for today : ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(title=title,
                    author=author,
                    content=content,
                    blogId=self.id,
                    dateCreated=date)
        post.save()

    def getPosts(self):
        return Post.fromBlog(self.id)

    def saveToMongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.description,
            'id':self.id
        }

    @classmethod
    def getFromMongo(cls,id):
        blogData = Database.findOne(collection='blogs',query={'id':id})
        return cls(author=blogData['author'],
                    title=blogData['title'],
                    description=blogData['description'],
                    id=blogData['id'])

