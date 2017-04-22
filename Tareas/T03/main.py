from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys


class T03Window(MyWindow):
    def __init__(self):
        super().__init__()

    def process_consult(self, querry_array):
        # Agrega en pantalla la solución. Muestra los graficos!!
        print(querry_array)
        text = "Probando funcion\nConsulta 01\n"
        self.add_answer(text)

    def save_file(self, querry_array):
        # Crea un archivo con la solucion. NO muestra los graficos!!
        print(querry_array)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
