import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import Qt
import gui  # Это наш конвертированный файл дизайна
import random


class Word:
    def __init__(self, ucode, trans):
        self.ucode = ucode
        self.trans = trans

def initBase():
    base = []
    str = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in str:
        base.append(Word(i, i+'0'))
    return base

def str_from_words(arr: list[Word]):
    s = ''
    for i in arr:
        s += i.ucode
    return s

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
    Word(u'\u3132', 'кы’'),
    Word(u'\u3138', 'ты’'),
    Word(u'\u3143', 'пы’'),
    Word(u'\u3146', 'сс'),
    Word(u'\u3149', 'цы')
]






base = initBase()

class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    word = random.choice(base)
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.lineEdit.textEdited.connect(self.checkAnswer)
        self.label_2.setText("Нажмите Enter для подсказки")
        self.textBrowser.zoomIn(50)

        self.initCheckBox()
        # self.setStyleSheet("background-color: #1f1b27;")
        # self.textBrowser.setStyleSheet("background-color: #ffffff;")
        # self.label_2.setStyleSheet("background-color: #f8cedb;")
        # self.lineEdit.setStyleSheet("background-color: #f8cedb;")

        # self.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.textBrowser.setText(self.word.ucode)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


    def initCheckBox(self):
        self.checkBox.setText(str_from_words(arr1))
        self.checkBox_2.setText(str_from_words(arr2))
        self.checkBox_3.setText(str_from_words(arr3))
        self.checkBox_4.setText(str_from_words(arr4))
        self.checkBox_5.setText(str_from_words(arr5))
        self.checkBox_6.setText(str_from_words(arr6))
        self.checkBox_7.setText(str_from_words(arr7))
        self.checkBox_8.setText(str_from_words(arr8))
        self.checkBox_9.setText(str_from_words(arr9))
        self.checkBox_10.setText(str_from_words(arr10))
        self.checkBox_11.setText(str_from_words(arr11))
        self.buttonBox


    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.label_2.setText(self.word.trans)

    def next_word(self):
        self.word = random.choice(base)
        self.label_2.setText("Нажмите Enter для подсказки")
        self.textBrowser.setText(self.word.ucode)
        self.lineEdit.clear()

    def checkAnswer(self):
        if self.lineEdit.text() == self.word.trans:
            self.next_word()



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
