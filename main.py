import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import Qt
import gui  # Это наш конвертированный файл дизайна
import random
from word_groups import *


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


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    base = arr1+arr2+arr3+arr4+arr5+arr6+arr7+arr8+arr9+arr10+arr11
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.textEdited.connect(self.checkAnswer)
        self.label_2.setText("Нажмите Enter для подсказки")
        self.cbox = self.get_all_checkbox()
        self.textBrowser.setFont(QtGui.QFont('Times', 135))
        self.counter_answer = 0
        self.counter_hint = 0

        self.hint = False

        self.initCheckBox()
        self.word = random.choice(self.base)
        self
        self.pushButton.setText("Выделить все")
        self.pushButton.clicked.connect(self.selectAll)
        self.pushButton_2.setText("Снять выделение")
        self.pushButton_2.clicked.connect(self.unselectAll)
        self.pushButton_3.setText("Применить")
        self.pushButton_3.clicked.connect(self.applyCheckBox)
        self.label_3.setText("Отвечено: " + str(self.counter_answer))
        self.label_4.setText("Подсказок использовано: " + str(self.counter_hint))


        self.tabWidget.setStyleSheet("background-color: #858ab2;")
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton_2.setStyleSheet("background-color: white;")
        self.pushButton_3.setStyleSheet("background-color: white;")
        self.lineEdit.setStyleSheet("background-color: white;")


        self.setStyleSheet("background-color: #3e3762;")


        # self.textBrowser.setStyleSheet("background-color: #ffffff;")
        # self.label_2.setStyleSheet("background-color: #f8cedb;")
        # self.lineEdit.setStyleSheet("background-color: #f8cedb;")

        # self.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textBrowser.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.textBrowser.setText(self.word.ucode)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


    def initCheckBox(self):
        for i in range(1, 12):
            eval(f'self.checkBox_{i}.setText(str_from_words(arr{i}))')
        for i in self.cbox:
            i.setFont(QtGui.QFont('Times', 20))
            # i.setStyleSheet("background-color: #38a5ff; border-radius: 7px;")



    def get_all_checkbox(self):
        res = [
            self.checkBox_1,
            self.checkBox_2,
            self.checkBox_3,
            self.checkBox_4,
            self.checkBox_5,
            self.checkBox_6,
            self.checkBox_7,
            self.checkBox_8,
            self.checkBox_9,
            self.checkBox_10,
            self.checkBox_11,
        ]
        return res

    def selectAll(self):
        for i in self.cbox:
            i.setCheckState(QtCore.Qt.CheckState.Checked)

    def unselectAll(self):
        for i in self.cbox:
            i.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def applyCheckBox(self):
        k = []
        if (self.checkBox_1.isChecked()):
            k += arr1
        if (self.checkBox_2.isChecked()):
            k += arr2
        if (self.checkBox_3.isChecked()):
            k += arr3
        if (self.checkBox_4.isChecked()):
            k += arr4
        if (self.checkBox_5.isChecked()):
            k += arr5
        if (self.checkBox_6.isChecked()):
            k += arr6
        if (self.checkBox_7.isChecked()):
            k += arr7
        if (self.checkBox_8.isChecked()):
            k += arr8
        if (self.checkBox_9.isChecked()):
            k += arr9
        if (self.checkBox_10.isChecked()):
            k += arr10
        if (self.checkBox_11.isChecked()):
            k += arr11
        self.base = k
        self.word = random.choice(self.base)
        self.label_2.setText("Нажмите Enter для подсказки")
        self.textBrowser.setText(self.word.ucode)
        self.lineEdit.clear()
        self.counter_answer += 1


    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.label_2.setText(self.word.trans)
            if (not self.hint):
                self.counter_hint += 1
                self.hint = True
            self.label_3.setText("Отвечено: " + str(self.counter_hint))

    def next_word(self):
        if self.base == []:
            return
        self.hint = False
        self.word = random.choice(self.base)
        self.label_2.setText("Нажмите Enter для подсказки")
        self.textBrowser.setText(self.word.ucode)
        self.lineEdit.clear()
        self.counter_answer += 1
        self.label_3.setText("Отвечено: " + str(self.counter_answer))

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
