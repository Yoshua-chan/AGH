import sys
from PyQt5.QtWidgets import QApplication, QWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Pierwszy program okienkowy"
        self.left = 100  # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 100  # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 300  # szerokośc okna
        self.height = 100  # wysokość okna

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        ###############
        # Tu w kolejnych zadaniach będziemy dodwać przycisk typu QPushButton, Slot
        #  oraz QLineEdit
        ###############
        self.show()


app = QApplication(sys.argv)
ex = App()
app.exec_()
