class Article(object):
    def __init__(self, topic, author):
        self.topic = topic
        self.text = None
        self.authors = []
        self.authors.append(author)
    def editTopic(self, topic):
        self.topic = topic
    def setText(self, text):
        self.text = text
    def editText(self, text, author):
        self.text = text
        if not (author in self.authors):
            self.authors.append((author, "Editor"))

class Author(object):
    def __init__(self, name):
        self.name = name
        self.email = None
    def setEmail(self, email):
        self.email = email

aut1 = Author("helmut03")
aut2 = Author("loreley")
html = Article("HTML", aut1)
css = Article("CSS", aut2)
bf = Article("Barrierefreiheit", aut2)
html.setText("Lorem")
html.editText("Lorem Ipsum", aut2)
html.editText("HTML ist cool", aut1)
