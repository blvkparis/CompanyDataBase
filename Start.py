import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import SIGNAL, QObject

from MainWindow import FirstWindow

if __name__ == '__main__':
    app = QApplication([])
    firstWindow = FirstWindow()
    firstWindow.show()

    app.exec_()
