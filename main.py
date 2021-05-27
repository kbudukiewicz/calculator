# Konrad Budukiewicz, Tomasz Czajkowski
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StopWatchWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 360, 520)
        self.setWindowIcon(QIcon('calculator.png'))

        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False

        self.label = QLabel(self)
        self.label.setGeometry(120, 440, 150, 70)

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setGeometry(5, 350, 170, 40)
        self.line_edit1.setPlaceholderText('Color and button')
        self.line_edit1.editingFinished.connect(self.change_background)

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setGeometry(185, 350, 170, 40)
        self.line_edit2.setPlaceholderText('Color and button')
        self.line_edit2.editingFinished.connect(self.change_button)

        self.start = QPushButton("Start clock", self)
        self.start.setGeometry(5, 400, 170, 40)
        self.start.pressed.connect(self.Start)

        self.but1 = QPushButton("1", self)
        self.but1.setGeometry(5, 150, 80, 40)
        self.but1.clicked.connect(self.action1)

        self.but2 = QPushButton("2", self)
        self.but2.setGeometry(95, 150, 80, 40)
        self.but2.clicked.connect(self.action2)

        self.but3 = QPushButton("3", self)
        self.but3.setGeometry(185, 150, 80, 40)
        self.but3.clicked.connect(self.action3)

        self.but4 = QPushButton("4", self)
        self.but4.setGeometry(5, 200, 80, 40)
        self.but4.clicked.connect(self.action4)

        self.but5 = QPushButton("5", self)
        self.but5.setGeometry(95, 200, 80, 40)
        self.but5.clicked.connect(self.action5)

        self.but6 = QPushButton("5", self)
        self.but6.setGeometry(185, 200, 80, 40)
        self.but6.clicked.connect(self.action6)

        self.but7 = QPushButton("7", self)
        self.but7.setGeometry(5, 250, 80, 40)
        self.but7.clicked.connect(self.action7)

        self.but8 = QPushButton("8", self)
        self.but8.setGeometry(95, 250, 80, 40)
        self.but8.clicked.connect(self.action8)

        self.but9 = QPushButton("9", self)
        self.but9.setGeometry(185, 250, 80, 40)
        self.but9.clicked.connect(self.action9)

        self.but0 = QPushButton("0", self)
        self.but0.setGeometry(5, 300, 80, 40)
        self.but0.clicked.connect(self.action0)

        self.but_point = QPushButton(".", self)
        self.but_point.setGeometry(95, 300, 80, 40)
        self.but_point.clicked.connect(self.action_point)

        self.but_equal = QPushButton("=", self)
        self.but_equal.setGeometry(185, 300, 80, 40)
        self.but_equal.clicked.connect(self.action_equal)

        self.but_plus = QPushButton("+", self)
        self.but_plus.setGeometry(275, 150, 80, 40)
        self.but_plus.clicked.connect(self.action_plus)

        self.but_minus = QPushButton("-", self)
        self.but_minus.setGeometry(275, 200, 80, 40)
        self.but_minus.clicked.connect(self.action_minus)

        self.but_mul = QPushButton("*", self)
        self.but_mul.setGeometry(275, 250, 80, 40)
        self.but_mul.clicked.connect(self.action_mul)

        self.but_div = QPushButton("/", self)
        self.but_div.setGeometry(275, 300, 80, 40)
        self.but_div.clicked.connect(self.action_div)

        self.but_del = QPushButton("Delete", self)
        self.but_del.setGeometry(210, 100, 145, 40)
        self.but_del.clicked.connect(self.action_del)

        self.but_clear = QPushButton("Clear", self)
        self.but_clear.setGeometry(5, 100, 200, 40)
        self.but_clear.clicked.connect(self.action_clear)

        self.label1 = QLabel(self)
        self.label1.setGeometry(5, 5, 350, 70)
        self.label1.setFont(QFont('Arial', 15))
        self.label1.setStyleSheet('QLabel{border : 4px solid black; background : white;}')

        self.label2 = QLabel(self)
        self.label2.setGeometry(200, 400, 100, 50)

        self.resetWatch = QPushButton("Reset clock", self)
        self.resetWatch.setGeometry(185, 400, 170, 40)
        self.resetWatch.pressed.connect(self.Reset)

        timer = QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(100)

        self.move(300, 400)
        self.show()

    def showCounter(self):
        if self.startWatch:
            self.counter += 1

            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))

                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        text = self.minute + ':' + self.second + ':' + self.count
        self.label.setText('<h1 style="color:blue">' + text + '</h1>')

    def change_background(self):
        col = self.line_edit1.text()
        self.setStyleSheet(f'QWidget {{background-color: {col};}}')
        self.line_edit1.clear()

    def change_button(self):
        col = self.line_edit2.text()
        self.start.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but1.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but2.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but3.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but4.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but5.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but6.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but7.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but8.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but9.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but0.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_point.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_equal.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_plus.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_minus.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_mul.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_div.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_del.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.but_clear.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.resetWatch.setStyleSheet(f'QPushButton{{background-color : {col};}}')
        self.line_edit1.setStyleSheet(f'QLineEdit {{background-color:{col};}}')
        self.line_edit2.setStyleSheet(f'QLineEdit {{background-color:{col};}}')
        self.line_edit2.clear()

    def Start(self):
        if self.start.text() == 'Stop':
            self.start.setText('Resume')
            self.startWatch = False
        else:
            self.startWatch = True
            self.start.setText('Stop')

    def Reset(self):
        self.startWatch = False
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.label.setText(str(self.counter))

    def action0(self):
        text = self.label1.text()
        self.label1.setText(text + "0")

    def action1(self):
        text = self.label1.text()
        self.label1.setText(text + "1")

    def action2(self):
        text = self.label1.text()
        self.label1.setText(text + "2")

    def action3(self):
        text = self.label1.text()
        self.label1.setText(text + "3")

    def action4(self):
        text = self.label1.text()
        self.label1.setText(text + "4")

    def action5(self):
        text = self.label1.text()
        self.label1.setText(text + "5")

    def action6(self):
        text = self.label1.text()
        self.label1.setText(text + "6")

    def action7(self):
        text = self.label1.text()
        self.label1.setText(text + "7")

    def action8(self):
        text = self.label1.text()
        self.label1.setText(text + "8")

    def action9(self):
        text = self.label1.text()
        self.label1.setText(text + "9")

    def action_equal(self):
        equation = self.label1.text()
        ans = eval(equation)
        self.label1.setText(str(ans))

    def action_plus(self):
        text = self.label1.text()
        self.label1.setText(text + " + ")

    def action_minus(self):
        text = self.label1.text()
        self.label1.setText(text + " - ")

    def action_mul(self):
        text = self.label1.text()
        self.label1.setText(text + " * ")

    def action_div(self):
        text = self.label1.text()
        self.label1.setText(text + " / ")

    def action_point(self):
        text = self.label1.text()
        self.label1.setText(text + ".")

    def action_clear(self):
        self.label1.setText("")

    def action_del(self):
        text = self.label1.text()
        self.label1.setText(text[:len(text) - 1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopWt = StopWatchWindow()
    app.exec()
