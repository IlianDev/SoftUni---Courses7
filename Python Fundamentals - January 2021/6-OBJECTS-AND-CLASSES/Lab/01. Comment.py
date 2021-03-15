class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# лайковете липсват зашото сме ги сложили равни на нула
comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
