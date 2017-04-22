from PyQt5 import QtWidgets, QtGui
import os
import json


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        querry_label = QtWidgets.QLabel("Consultas")
        result_label = QtWidgets.QLabel("Resultados")
        self.querry_table = QtWidgets.QTableWidget(self)
        self.result_table = QtWidgets.QTextEdit(self)

        first_layout = QtWidgets.QVBoxLayout()
        first_layout.addWidget(querry_label)
        first_layout.addWidget(self.querry_table)

        second_layout = QtWidgets.QVBoxLayout()
        second_layout.addWidget(result_label)
        second_layout.addWidget(self.result_table)

        aux_layour = QtWidgets.QHBoxLayout()
        aux_layour.addLayout(first_layout)
        aux_layour.addLayout(second_layout)

        all_querry_boton = QtWidgets.QPushButton(
            "Realizar toda\n las consultas")
        selected_querry_boton = QtWidgets.QPushButton(
            "Realizar consulta(s)\nselecciona(s)")
        save_file_boton = QtWidgets.QPushButton(
            "Generar\narchivo")

        third_layout = QtWidgets.QHBoxLayout()
        third_layout.addWidget(all_querry_boton)
        third_layout.addWidget(selected_querry_boton)
        third_layout.addWidget(save_file_boton)

        self.querry = QtWidgets.QLineEdit(self)
        send_querry_boton = QtWidgets.QPushButton("Enviar Consulta")
        fourty_layout = QtWidgets.QHBoxLayout()
        fourty_layout.addWidget(self.querry)
        fourty_layout.addWidget(send_querry_boton)

        principal_layout = QtWidgets.QVBoxLayout()
        principal_layout.addLayout(aux_layour)
        principal_layout.addLayout(third_layout)
        principal_layout.addLayout(fourty_layout)

        self.setLayout(principal_layout)
        self.index = 0
        self.querry_table.setColumnCount(1)
        header = self.querry_table.horizontalHeader()
        header.setStretchLastSection(True)
        header.hide()
        self.querry.setPlaceholderText("Agregar Consulta")

        send_querry_boton.clicked.connect(self.add_new_querry)
        all_querry_boton.clicked.connect(self.process_querry)
        selected_querry_boton.clicked.connect(self.process_querry)
        save_file_boton.clicked.connect(self.save_file)

        self.querry_table.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.result_table.setReadOnly(True)

    def keyPressEvent(self, key_event):
        if key_event.key() == 16777220:
            self.add_new_querry()

    def add_querry(self, text):
        item = QtWidgets.QTableWidgetItem()
        item.setText(text)
        self.querry_table.insertRow(self.index)
        self.querry_table.setItem(0, self.index, item)
        self.index += 1

    def add_new_querry(self):
        querry = self.querry.text()
        if querry.startswith("'"):
            querry = querry.strip("'")
        elif querry.startswith('"'):
            querry = querry.strip('"')
        try:
            querry_list = json.loads(querry)
            self.add_querry(str(querry_list))
            self.querry.clear()
        except ValueError:
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("No es posible procesar la consulta")
            msg.setWindowTitle("Consulta Invalida")
            msg.show()

    def process_querry(self):
        if self.sender().text() == "Realizar toda\n las consultas":
            self.querry_table.selectAll()
            all_items = self.querry_table.selectedItems()
            self.querry_table.clearSelection()
            array = []
            for querry in all_items:
                array.append(json.loads(querry.text().replace("'", '"')))
            self.process_consult(array)
        else:
            array = []
            for querry in self.querry_table.selectedItems():
                array.append(json.loads(querry.text().replace("'", '"')))
            self.process_consult(array)

    def save_file(self):
        self.querry_table.selectAll()
        all_items = self.querry_table.selectedItems()
        self.querry_table.clearSelection()
        array = []
        for querry in all_items:
            array.append(json.loads(querry.text().replace("'", '"')))
        self.save_file_consult(array)

    def add_answer(self, texto):
        self.result_table.insertPlainText(texto)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setCentralWidget(MyWidget())
        self.show()
        self.setWindowTitle("RQL")
        self.setWindowIcon(QtGui.QIcon(os.getcwd() + os.sep + "gui" +
                                       os.sep + "icon.png"))
        self.centralWidget().process_consult = self.process_consult
        self.centralWidget().save_file_consult = self.save_file

        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Archivo")
        menu_archivo_abrir = QtWidgets.QAction(QtGui.QIcon(), "&Abrir", self)
        menu_archivo_abrir.triggered.connect(self.load_path)
        menu_archivo.addAction(menu_archivo_abrir)

    def load_path(self):
        with open("consultas.json") as file:
            json_file = json.load(file)
        for querry in json_file:
            self.add_querry(str(querry))

    def add_querry(self, text):
        self.centralWidget().add_querry(text)

    def add_answer(self, text):
        self.centralWidget().add_answer(text)

    def process_consult(self, array):
        pass

    def save_file(self, array):
        pass
