import sys
import calculator as calc
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLCDNumber


def main():
    app = QApplication(sys.argv)
    calculator = calc.App()
    calculator.show()
    app.exec_()


if __name__ == "__main__":
    main()
