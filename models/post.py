import uuid

import datetime

from monogoDB import Database


class Post(object):

    def __init__(self,title,author,content,blogId,dateCreated=datetime.datetime.utcnow(),id=None):
        self.title = title
        self.author = author
        self.dateCreated = dateCreated
        self.content = content
        self.blogId = blogId
        self.id = uuid.uuid4().hex if id is None else id

    def save(self):
        Database.insert(collection='posts',data=self.json())


    def json(self):
        return {
            'id':self.id,
            'blogId':self.blogId,
            'title':self.title,
            'author':self.author,
            'content':self.content,
            'dateCreated':self.dateCreated
        }

    @classmethod
    def fromMonogo(cls,id):
        postData = Database.findOne(collection='posts',query={'id':id})
        return cls(title=postData['title'],
                   author=postData['author'],
                   content=postData['content'],
                   blogId=postData['blogId'],
                   dateCreated=postData['dateCreated'],
                   id=postData['id'])

    @staticmethod
    def fromBlog(id):
        return [post for post in Database.find(collection='posts', query={'blogId': id})]
