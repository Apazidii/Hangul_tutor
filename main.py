class Word:
    def __init__(self, ucode, trans):
        self.ucode = ucode
        self.trans = trans

def initBase():
    base = []
    str = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdf"
    for i in str:
        base.append(Word(i, i+'0'))
    return base


base = initBase()
