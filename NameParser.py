import nltk
from nameparser.parser import HumanName # pip install nameparser
from nltk.corpus import wordnet
from tkinter.filedialog import askopenfilename

person_list = []
person_names = person_list

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)
    

if __name__ == "__main__":
    file_name = askopenfilename()
    f = open(file_name)
    
    # Read from file
    raw=f.read()
    
    names = get_human_names(raw)
    for person in person_list:
        person_split = person.split(" ")
        for name in person_split:
            if wordnet.synsets(name):
                if(name in person):
                    person_names.remove(person)
                    break

    print(person_names)
