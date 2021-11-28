import sys
import math
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QRadioButton, QPushButton, QLCDNumber


class CalcActions:
    def __init__(self):
        self.main_screen = QLineEdit(self)
        self.cache_screen = QLineEdit(self)
        self.operator_screen = QLineEdit(self)
        self.operations = {
            "/": (lambda a, b: a / b),
            "*": (lambda a, b: a * b),
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "%": (lambda a, b: a % b),
        }

    def digit_0(self):
        current = self.main_screen.text()
        result = current + "0"
        self.main_screen.setText(result)

    def digit_1(self):
        current = self.main_screen.text()
        result = current + "1"
        self.main_screen.setText(result)

    def digit_2(self):
        current = self.main_screen.text()
        result = current + "2"
        self.main_screen.setText(result)

    def digit_3(self):
        current = self.main_screen.text()
        result = current + "3"
        self.main_screen.setText(result)

    def digit_4(self):
        current = self.main_screen.text()
        result = current + "4"
        self.main_screen.setText(result)

    def digit_5(self):
        current = self.main_screen.text()
        result = current + "5"
        self.main_screen.setText(result)

    def digit_6(self):
        current = self.main_screen.text()
        result = current + "6"
        self.main_screen.setText(result)

    def digit_7(self):
        current = self.main_screen.text()
        result = current + "7"
        self.main_screen.setText(result)

    def digit_8(self):
        current = self.main_screen.text()
        result = current + "8"
        self.main_screen.setText(result)

    def digit_9(self):
        current = self.main_screen.text()
        result = current + "9"
        self.main_screen.setText(result)

    def digit_comma(self):
        current = self.main_screen.text()
        result = current + "."
        self.main_screen.setText(result)

    def digit_parenthasis_left(self):
        current = self.main_screen.text()
        current = current + "("
        self.main_screen.setText(current)

    def digit_parenthasis_right(self):
        current = self.main_screen.text()
        current = current + ")"
        self.main_screen.setText(current)

    def digit_eq(self):
        result = 0
        try:
            result = self.operations[self.current_operator](
                float(self.cache_screen.text()),
                float(self.main_screen.text())
            )
        except ZeroDivisionError:
            result = float("NaN")

        self.cache_screen.clear()
        self.operator_screen.clear()
        self.main_screen.setText(str(result))

    def backspace(self):
        text = self.main_screen.text()
        self.main_screen.setText(text[:-1])

    def clear_screen(self):
        if not self.main_screen.text():
            self.cache_screen.clear()
        else:
            self.main_screen.clear()

    def operation_mul(self):
        current = self.main_screen.text()
        self.current_operator = "*"
        self.operator_screen.setText("×")
        self.cache_screen.setText(current)
        self.main_screen.clear()

    def operation_div(self):
        current = self.main_screen.text()
        self.current_operator = "/"
        self.operator_screen.setText("÷")
        self.cache_screen.setText(current)
        self.main_screen.clear()

    def operation_add(self):
        current = self.main_screen.text()
        self.current_operator = "+"
        self.operator_screen.setText("+")
        self.cache_screen.setText(current)
        self.main_screen.clear()

    def operation_sub(self):
        current = self.main_screen.text()
        self.current_operator = "-"
        self.operator_screen.setText("-")
        self.cache_screen.setText(current)
        self.main_screen.clear()

    def operation_mod(self):
        current = self.main_screen.text()
        self.current_operator = "%"
        self.operator_screen.setText("mod")
        self.cache_screen.setText(current)
        self.main_screen.clear()

    def operation_sqrt(self):
        current = self.main_screen.text()
        number = float(current)
        self.main_screen.setText(str(math.sqrt(number)))
