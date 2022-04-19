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

base = initBase()

class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    word = random.choice(base)
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.lineEdit.textEdited.connect(self.checkAnswer)
        self.label.setText("Нажмите Enter для подсказки")
        self.textBrowser.zoomIn(50)
        self.setStyleSheet("background-color: #1f1b27;")
        self.textBrowser.setStyleSheet("background-color: #897ea5;")
        self.label.setStyleSheet("background-color: #f8cedb;")
        self.lineEdit.setStyleSheet("background-color: #f8cedb;")

        # self.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.textBrowser.setText(self.word.ucode)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.label.setText(self.word.trans)

    def next_word(self):
        self.word = random.choice(base)
        self.label.setText("Нажмите Enter для подсказки")
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

base = initBase()
