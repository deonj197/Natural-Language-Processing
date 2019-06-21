class Word(object):
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
    @staticmethod
    def from_dict(source):
        return
        #...

    def to_dict(self):
        return {
            u'text': self.text,
            u'tag': self.tag
        }
