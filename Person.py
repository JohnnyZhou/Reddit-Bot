
class Person:
    def __init__(self, name, last_comments, messaged="n"):
        self.last_comments = last_comments
        self.name = name
        self.messaged = messaged

    def to_string(self):
        return "{},{},{} ****".format(self.name, self.messaged, self.last_comments)
