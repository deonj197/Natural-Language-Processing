class Sentence(object):
    def __init__(self, text, words):
        self.text = text
        self.words = words
    @staticmethod
    def from_dict(source):
        return
        #...

    def to_dict(self):
        return {
            u'text': self.text,
            u'words': self.words
        }