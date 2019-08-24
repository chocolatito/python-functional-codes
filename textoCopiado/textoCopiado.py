import sys, re
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
#______________________________>
class TextoCopiado(QMainWindow):
	""" Doc """
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("textoCopiado.ui", self)

		self.pushButton.clicked.connect(self.quitarSalto)

	def quitarSalto(self):
		self.mostrarTexto("".join(re.sub("\n"," ",self.textEdit.toPlainText())))

	def mostrarTexto(self, texto):
		print(texto)
		self.textBrowser.setText(texto)


app = QApplication(sys.argv)
main = TextoCopiado()
main.show()
app.exec_()

