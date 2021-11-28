import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class App(QWidget):
    def on_click(self) -> None:
        print("Dupa cyce wadowice")

    def __init__(self):
        super().__init__()
        self.title = "Pierwszy program okienkowy"
        self.left = 100  # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 100  # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 300  # szerokośc okna
        self.height = 100  # wysokość okna

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton("Pierwszy przycisk", self)
        self.button.setToolTip("Podpowiedź do pierwszego przycisku")
        self.button.move(100, 40)  # położenie pierwszego przycisku

        self.button.clicked.connect(
            self.on_click
        )  # podłącza metodę on_click do przyciśnięcia przycisku

        self.show()


app = QApplication(sys.argv)
ex = App()
app.exec_()
