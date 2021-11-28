import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class App(QWidget):
    def on_click(self) -> None:
        self.output.setText(self.input1.text() + self.input2.text())

    def clear(self):
        self.input1.clear()
        self.input2.clear()
        self.output.clear()

    def __init__(self):
        super().__init__()
        self.title = "Pierwszy program okienkowy"
        self.left = 100  # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 100  # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 300  # szerokośc okna
        self.height = 250  # wysokość okna

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.cat_button = QPushButton("Połącz", self)
        self.cat_button.setToolTip("Podpowiedź do pierwszego przycisku")
        self.cat_button.move(40, 105)  # położenie pierwszego przycisku
        self.cat_button.resize(100, 30)
        self.cat_button.clicked.connect(
            self.on_click
        )  # podłącza metodę on_click do przyciśnięcia przycisku

        self.clear_button = QPushButton("Wyczyść", self)
        self.clear_button.setToolTip("Czyści wszystkie pola tekstowe")
        self.clear_button.move(150, 105)  # położenie pierwszego przycisku
        self.clear_button.resize(100, 30)
        self.clear_button.clicked.connect(
            self.clear
        )  # podłącza metodę on_click do przyciśnięcia przycisku

        self.input1 = QLineEdit(self)
        self.input1.move(40, 5)
        self.input1.resize(220, 30)
        self.input1.setText("Ala ma")

        self.input2 = QLineEdit(self)
        self.input2.move(40, 55)
        self.input2.resize(220, 30)
        self.input2.setText(" kota")

        self.output = QLineEdit(self)
        self.output.move(40, 155)
        self.output.resize(220, 30)
        self.output.setText("Wejście")

        self.show()


app = QApplication(sys.argv)
dupa = App()
app.exec_()
