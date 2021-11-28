import sys
import PyQt5
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, \
    QRadioButton, QPushButton, QLCDNumber

from calc_actions import CalcActions

class DummyButton():
    def move(self, *args):
        pass

    def resize(self, *args):
        pass

    def setFont(self, *args):
        pass

class App(QWidget, CalcActions):
    def __init__(self):
        super().__init__()
        self.title = "Calculator"
        self.setWindowTitle(self.title)

        self.left = 750
        self.top = 250

        self.button_gap = 5
        self.button_width = 50

        self.cache_screen_height = 30
        self.main_screen_height = 50
        self.keyboard_offset = 3 * self.button_gap + self.cache_screen_height + self.main_screen_height

        self.width = 4 * self.button_width + 5 * self.button_gap
        self.height = self.keyboard_offset + 5 * self.button_width + 5 * self.button_gap

        self.cache_screen.move(self.button_gap, self.button_gap)
        self.cache_screen.resize(self.width - 2 * self.button_gap, self.cache_screen_height)
        self.cache_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.cache_screen.setReadOnly(True)
        self.cache_screen.selectionChanged.connect(lambda: self.cache_screen.setSelection(0, 0))

        self.main_screen.move(self.button_gap, self.cache_screen_height + 2 * self.button_gap)
        self.main_screen.resize(self.width - 2 * self.button_gap, self.main_screen_height)
        self.main_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.main_screen.setReadOnly(True)
        self.main_screen.selectionChanged.connect(lambda: self.main_screen.setSelection(0, 0))

        self.operator_screen.move(self.button_gap, self.cache_screen_height + 2 * self.button_gap)
        self.operator_screen.resize(40, self.main_screen_height)
        self.operator_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.operator_screen.setReadOnly(True)
        self.operator_screen.selectionChanged.connect(lambda: self.operator_screen.setSelection(0, 0))

        self.setGeometry(self.left, self.top, self.width, self.height)

        self.digit_button_0 = QPushButton("0", self)
        self.digit_button_1 = QPushButton("1", self)
        self.digit_button_2 = QPushButton("2", self)
        self.digit_button_3 = QPushButton("3", self)
        self.digit_button_4 = QPushButton("4", self)
        self.digit_button_5 = QPushButton("5", self)
        self.digit_button_6 = QPushButton("6", self)
        self.digit_button_7 = QPushButton("7", self)
        self.digit_button_8 = QPushButton("8", self)
        self.digit_button_9 = QPushButton("9", self)
        self.digit_button_comma = QPushButton(".", self)
        self.digit_button_eq = QPushButton("=", self)

        self.button_clear = QPushButton("C/CE", self)
        self.button_backspace = QPushButton("<-", self)

        self.operation_button_mul = QPushButton("×", self)
        self.operation_button_div = QPushButton("÷", self)
        self.operation_button_add = QPushButton("+", self)
        self.operation_button_sub = QPushButton("-", self)
        self.operation_button_mod = QPushButton("mod", self)
        self.operation_button_sqrt = QPushButton("√", self)

        self.digit_button_0.clicked.connect(self.digit_0)
        self.digit_button_1.clicked.connect(self.digit_1)
        self.digit_button_2.clicked.connect(self.digit_2)
        self.digit_button_3.clicked.connect(self.digit_3)
        self.digit_button_4.clicked.connect(self.digit_4)
        self.digit_button_5.clicked.connect(self.digit_5)
        self.digit_button_6.clicked.connect(self.digit_6)
        self.digit_button_7.clicked.connect(self.digit_7)
        self.digit_button_8.clicked.connect(self.digit_8)
        self.digit_button_9.clicked.connect(self.digit_9)
        self.digit_button_comma.clicked.connect(self.digit_comma)
        self.digit_button_eq.clicked.connect(self.digit_eq)
        self.button_clear.clicked.connect(self.clear_screen)

        self.button_backspace.clicked.connect(self.backspace)
        self.operation_button_mul.clicked.connect(self.operation_mul)
        self.operation_button_div.clicked.connect(self.operation_div)
        self.operation_button_add.clicked.connect(self.operation_add)
        self.operation_button_sub.clicked.connect(self.operation_sub)
        self.operation_button_mod.clicked.connect(self.operation_mod)
        self.operation_button_sqrt.clicked.connect(self.operation_sqrt)

        self.dummy = DummyButton()  # dummy button to fill the gaps in UI

        self.keyboard = [
            self.button_clear, self.button_backspace, self.operation_button_mod, self.operation_button_sqrt,
            self.digit_button_7, self.digit_button_8, self.digit_button_9, self.operation_button_mul,
            self.digit_button_4, self.digit_button_5, self.digit_button_6, self.operation_button_div,
            self.digit_button_1, self.digit_button_2, self.digit_button_3, self.operation_button_add,
            self.digit_button_0, self.digit_button_comma, self.digit_button_eq, self.operation_button_sub
        ]

        for i, button in enumerate(self.keyboard):
            button.move(
                ((i % 4) * self.button_width) + (i % 4 * self.button_gap) + self.button_gap,
                (i // 4) * (self.button_gap + self.button_width) + self.keyboard_offset,
            )
            if i > 2:
                button.setFont(QFont('Noto Mono', 12))
            else:
                button.setFont(QFont('Noto Mono', 12))
            button.resize(self.button_width, self.button_width)
