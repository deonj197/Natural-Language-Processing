class Sentence(object):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def from_dict(source):
        return
        #...

    def to_dict(self):
        return {
            u'text': self.text
        }