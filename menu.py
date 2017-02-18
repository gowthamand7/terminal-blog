from models.blog import Blog
from monogoDB import Database

class Menu(object):

    """def __int__(self):
        self.user = input("Enter your author name : ")
        self.userBlog = None
        if self.userGotAccount():
            print("Welcome back {}!".format(self.user))
        else:
            self.promptUserForAccount()"""

    def user(self):
        self.user = input("Enter your author name : ")
        self.userBlog = None
        if self.userGotAccount():
            print("Welcome back {}!".format(self.user))
        else:
            self.promptUserForAccount()

    def userGotAccount(self):
        blog =  Database.findOne(collection='blogs',query={'author':self.user})
        if blog is not None:
            self.userBlog = Blog.getFromMongo(blog['id'])
            return True
        else:
            return False

    def promptUserForAccount(self):
        print("Welcome {}, Its looks you dont have any blog to post, Please give us a Blog Details as Below ".format(self.user))
        title = input("Enter a Blog title :")
        description = input("Enter a blog description :")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.saveToMongo()
        self.userBlogId = blog.id

    def runMenu(self):
        action = input("Do you  want to read(R) or write(W) blogs ?")
        if action == 'R':
            self.listBlogs()
            self.viewBlogs()
        elif action == 'W':
            self.userBlog.newPost()
        else:
            input("Thankyou for blogging!")

    def listBlogs(self):
        blogs = Database.find(collection='blogs',query={})
        for blog in blogs:
            print("Id: {}, Title: {}, Author: {}, Description: {}".format(blog['id'],blog['title'],blog['author'],blog['description']))

    def viewBlogs(self):
        blogid = input("Enter the Id of the blog you'd like to read: ")
        blog = Blog.getFromMongo(blogid)
        posts = blog.getPosts()
        if not posts:
            print("The selected blogs dont have any post")
        else:
            for post in posts:
                print("Date: {}, title: {}\n\n{}\n".format(post['dateCreated'],post['title'],post['content']))