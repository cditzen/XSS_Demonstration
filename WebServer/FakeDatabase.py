class FakeDatabase:
    posts = []

    def initPosts(self):
        # Add some posts to the database
        message = "This is a harmless message"
        self.posts.append(message)

        message = "This is the results of our Ajax call."
        message += "<img src=\"loaded.gif\" alt=\"\""
        message += "onload=\"alert('This is malicious JS code');"
        message += "this.parentNode.removeChild(this);\" />"
        self.posts.append(message)

        message = "<p>This is another harmless message</p>"
        self.posts.append(message)

    def getPosts(self):
        return self.posts

    def addPost(self, post):
        self.posts.append(post)

    def deletePosts(self):
        self.posts.clear()