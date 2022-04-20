class Word:
    def __init__(self, ucode, trans):
        self.ucode = ucode
        self.trans = trans

arr1 = [
    Word(u'\u314F', 'а:'),
    Word(u'\u3151', 'йа'),
    Word(u'\u3153', 'о:'),
    Word(u'\u3155', 'йо')
]

arr2 = [
    Word(u'\u3157', 'уо:'),
    Word(u'\u315B', 'йуо'),
    Word(u'\u315C', 'у:'),
    Word(u'\u3160', 'йу')
]

arr3 = [
    Word(u'\u3161', 'ы:'),
    Word(u'\u3163', 'и:')
]

arr4 = [
    Word(u'\u3150', 'э:'),
    Word(u'\u3152', 'йэ:'),
    Word(u'\u3154', 'эы:'),
    Word(u'\u3156', 'йэы:')
]

arr5 = [
    Word(u'\u3158', 'ва:'),
    Word(u'\u3159', 'вэ:'),
    Word(u'\u315A', 'вюэ:')
]

arr6 = [
    Word(u'\u315D', 'во:'),
    Word(u'\u315E', 'выэ:'),
    Word(u'\u316F', 'ви:'),
    Word(u'\u3152', 'ыи:')
]

arr7 = [
    Word(u'\u3131', 'кы:'),
    Word(u'\u3134', 'ны:'),
    Word(u'\u3137', 'ты:'),
    Word(u'\u3139', 'ры,л,ль:')
]

arr8 = [
    Word(u'\u3141', 'мы:'),
    Word(u'\u3142', 'пы:'),
    Word(u'\u3145', 'сы:'),
    Word(u'\u3147', 'ынн')
]

arr9 = [
    Word(u'\u3148', 'тьы'),
    Word(u'\u314A', 'цьы')
]

arr10 = [
    Word(u'\u314B', 'кх'),
    Word(u'\u314C', 'тх'),
    Word(u'\u314D', 'пх'),
    Word(u'\u314E', 'хы:')
]

arr11 = [
    Word(u'\u3132', "кы'"),
    Word(u'\u3138', "ты'"),
    Word(u'\u3143', "пы'"),
    Word(u'\u3146', 'сс'),
    Word(u'\u3149', 'цы')
]