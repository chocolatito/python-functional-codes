import sys
import re
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import *
# ______________________________>


class TextoCopiado(QMainWindow):
    """ Doc """

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("textoCopiado.ui", self)

        self.pushButton_Quitar.clicked.connect(self.quitarSaltos)
        self.pushButton_Insertar.clicked.connect(self.capturarSalto)

    def quitarSaltos(self):
        self.mostrarTexto("".join(re.sub("\n", " ", self.textEdit.toPlainText())))

    def mostrarTexto(self, texto):
        # print(texto)
        self.textBrowser.setText(texto)

    def capturarSalto(self):
        self.insertarSalto(self.lineEdit.text())

    def insertarSalto(self, salto):
        pass


app = QApplication(sys.argv)
main = TextoCopiado()
main.show()
app.exec_()
