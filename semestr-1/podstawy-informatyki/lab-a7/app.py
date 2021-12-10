from PyQt5.QtCore import QFile, QLine
from PyQt5.QtWidgets import QAction, QMenuBar, QWidget, QLineEdit, QPushButton, \
    QRadioButton, QSpinBox, QDoubleSpinBox, QApplication, \
    QMenu, QFileDialog, QTableWidget, QLabel, QCheckBox
import pyqtgraph

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.waveform = "sine"
        ########## WINDOW PROPERTIES ############
        self.title = "Function generator"
        self.setWindowTitle(self.title)

        self.height = 500
        self.width = 500 * 1.68
        self.setGeometry(400, 250, self.width, self.height)

        ############# ACTIONS  ##################
        self.save = QAction("Save", self)
        self.save.triggered.connect(self.save_file)

        self.load = QAction("Load", self)
        self.load.triggered.connect(self.load_file)

        self.about = QAction("About", self)
        self.about.triggered.connect(self.show_about)

        ############# MENU BAR ##################
        self.menu = QMenuBar(self)
        self.file_menu = self.menu.addMenu("File")
        self.help_menu = self.menu.addMenu("Help")

        self.file_menu.addActions([self.save, self.load])
        self.help_menu.addAction(self.about)

        self.show()

    def load_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", options=options)
        print(filename)

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getOpenFileName()", f"{self.waveform}.csv", options=options)
        file = open(filename, "w")
        file.write("Hemlo Worlmd")
        file.close()

    def show_about(self):
        pass