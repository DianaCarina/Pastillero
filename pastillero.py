# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pastillero.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 443)
        MainWindow.setMinimumSize(QtCore.QSize(501, 443))
        MainWindow.setMaximumSize(QtCore.QSize(501, 443))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 421))
        self.tabWidget.setMinimumSize(QtCore.QSize(501, 421))
        self.tabWidget.setMaximumSize(QtCore.QSize(501, 421))
        self.tabWidget.setStyleSheet("background-color: rgb(60, 223, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 361, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(60, 223, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_registrarce = QtWidgets.QPushButton(self.tab)
        self.btn_registrarce.setGeometry(QtCore.QRect(270, 260, 176, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_registrarce.setFont(font)
        self.btn_registrarce.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_registrarce.setObjectName("btn_registrarce")
        self.btn_busqueda = QtWidgets.QPushButton(self.tab)
        self.btn_busqueda.setGeometry(QtCore.QRect(50, 260, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_busqueda.setFont(font)
        self.btn_busqueda.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_busqueda.setObjectName("btn_busqueda")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 0, 281, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lEdit_nombre_reg = QtWidgets.QLineEdit(self.tab_2)
        self.lEdit_nombre_reg.setGeometry(QtCore.QRect(190, 80, 211, 21))
        self.lEdit_nombre_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_nombre_reg.setObjectName("lEdit_nombre_reg")
        self.lEdit_edad_reg = QtWidgets.QLineEdit(self.tab_2)
        self.lEdit_edad_reg.setGeometry(QtCore.QRect(190, 120, 211, 21))
        self.lEdit_edad_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_edad_reg.setObjectName("lEdit_edad_reg")
        self.lEdit_Dx = QtWidgets.QLineEdit(self.tab_2)
        self.lEdit_Dx.setGeometry(QtCore.QRect(190, 160, 211, 21))
        self.lEdit_Dx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_Dx.setObjectName("lEdit_Dx")
        self.lEdit_NoSS = QtWidgets.QLineEdit(self.tab_2)
        self.lEdit_NoSS.setGeometry(QtCore.QRect(190, 200, 211, 21))
        self.lEdit_NoSS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_NoSS.setObjectName("lEdit_NoSS")
        self.btn_registrar_px = QtWidgets.QPushButton(self.tab_2)
        self.btn_registrar_px.setGeometry(QtCore.QRect(150, 310, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_registrar_px.setFont(font)
        self.btn_registrar_px.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_registrar_px.setObjectName("btn_registrar_px")
        self.lEdit_User = QtWidgets.QLineEdit(self.tab_2)
        self.lEdit_User.setGeometry(QtCore.QRect(190, 240, 211, 21))
        self.lEdit_User.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_User.setObjectName("lEdit_User")
        self.lEdit_Password = QtWidgets.QLineEdit(self.tab_2)
        self.lEdit_Password.setGeometry(QtCore.QRect(190, 270, 211, 21))
        self.lEdit_Password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_Password.setObjectName("lEdit_Password")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(30, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.linEdit_Medicamento = QtWidgets.QLineEdit(self.tab_4)
        self.linEdit_Medicamento.setGeometry(QtCore.QRect(210, 100, 211, 21))
        self.linEdit_Medicamento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linEdit_Medicamento.setObjectName("linEdit_Medicamento")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(60, 100, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(20, 40, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btn_add_med = QtWidgets.QPushButton(self.tab_4)
        self.btn_add_med.setGeometry(QtCore.QRect(140, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add_med.setFont(font)
        self.btn_add_med.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_add_med.setObjectName("btn_add_med")
        self.btn_end_med = QtWidgets.QPushButton(self.tab_4)
        self.btn_end_med.setGeometry(QtCore.QRect(140, 280, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_end_med.setFont(font)
        self.btn_end_med.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_end_med.setObjectName("btn_end_med")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btn_pxView = QtWidgets.QPushButton(self.tab_3)
        self.btn_pxView.setGeometry(QtCore.QRect(150, 250, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_pxView.setFont(font)
        self.btn_pxView.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_pxView.setObjectName("btn_pxView")
        self.lbl_nombre_ingresar = QtWidgets.QLineEdit(self.tab_3)
        self.lbl_nombre_ingresar.setGeometry(QtCore.QRect(190, 90, 211, 21))
        self.lbl_nombre_ingresar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_nombre_ingresar.setObjectName("lbl_nombre_ingresar")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(60, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lbl_password = QtWidgets.QLineEdit(self.tab_3)
        self.lbl_password.setGeometry(QtCore.QRect(190, 140, 211, 21))
        self.lbl_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_password.setObjectName("lbl_password")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(60, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(150, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(40, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(40, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(40, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setGeometry(QtCore.QRect(40, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lbl_nombre = QtWidgets.QLabel(self.tab_5)
        self.lbl_nombre.setGeometry(QtCore.QRect(150, 20, 47, 13))
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_edad = QtWidgets.QLabel(self.tab_5)
        self.lbl_edad.setGeometry(QtCore.QRect(140, 50, 47, 13))
        self.lbl_edad.setObjectName("lbl_edad")
        self.lbl_Dx = QtWidgets.QLabel(self.tab_5)
        self.lbl_Dx.setGeometry(QtCore.QRect(190, 80, 47, 13))
        self.lbl_Dx.setObjectName("lbl_Dx")
        self.lbl_NoSocial = QtWidgets.QLabel(self.tab_5)
        self.lbl_NoSocial.setGeometry(QtCore.QRect(230, 110, 47, 13))
        self.lbl_NoSocial.setObjectName("lbl_NoSocial")
        self.btn_back_inicio = QtWidgets.QPushButton(self.tab_5)
        self.btn_back_inicio.setGeometry(QtCore.QRect(290, 290, 176, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_back_inicio.setFont(font)
        self.btn_back_inicio.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_back_inicio.setObjectName("btn_back_inicio")
        self.btn_modificar = QtWidgets.QPushButton(self.tab_5)
        self.btn_modificar.setGeometry(QtCore.QRect(30, 290, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_modificar.setFont(font)
        self.btn_modificar.setStyleSheet("background-color: rgb(60, 223, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.btn_modificar.setObjectName("btn_modificar")
        self.medicamentosList = QtWidgets.QListView(self.tab_5)
        self.medicamentosList.setGeometry(QtCore.QRect(40, 140, 371, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 223, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.medicamentosList.setPalette(palette)
        self.medicamentosList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.medicamentosList.setObjectName("medicamentosList")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        MainWindow.setMenuBar(self.menubar)
        self.actionInformacion = QtWidgets.QAction(MainWindow)
        self.actionInformacion.setObjectName("actionInformacion")
        self.menuOpciones.addAction(self.actionInformacion)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pastillero"))
        self.label.setText(_translate("MainWindow", "Registro Pacientes"))
        self.btn_registrarce.setText(_translate("MainWindow", "Registrarce"))
        self.btn_busqueda.setText(_translate("MainWindow", "Iniciar Sesion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Inicio"))
        self.label_2.setText(_translate("MainWindow", "Registro"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Edad"))
        self.label_5.setText(_translate("MainWindow", "Padecimiento"))
        self.label_6.setText(_translate("MainWindow", "No. Seguro Social"))
        self.btn_registrar_px.setText(_translate("MainWindow", "Registrar"))
        self.label_13.setText(_translate("MainWindow", "Contraseña"))
        self.label_24.setText(_translate("MainWindow", "Usuario"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Registrarce"))
        self.label_11.setText(_translate("MainWindow", "Medicamento"))
        self.label_15.setText(_translate("MainWindow", "Ingrese los medicamentos, uno por uno"))
        self.btn_add_med.setText(_translate("MainWindow", "Agregar"))
        self.btn_end_med.setText(_translate("MainWindow", "Concluir registro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Registro de medicamentos"))
        self.btn_pxView.setText(_translate("MainWindow", "Buscar"))
        self.label_7.setText(_translate("MainWindow", "Usuario"))
        self.label_8.setText(_translate("MainWindow", "Contraseña"))
        self.label_14.setText(_translate("MainWindow", "Ingrese los datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Inicio Sesion"))
        self.label_16.setText(_translate("MainWindow", "Padecimiento"))
        self.label_17.setText(_translate("MainWindow", "Edad"))
        self.label_18.setText(_translate("MainWindow", "Paciente"))
        self.label_19.setText(_translate("MainWindow", "No. Seguridad Social"))
        self.lbl_nombre.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_edad.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_Dx.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_NoSocial.setText(_translate("MainWindow", "TextLabel"))
        self.btn_back_inicio.setText(_translate("MainWindow", "Cerrar Sesion"))
        self.btn_modificar.setText(_translate("MainWindow", "Modificar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Pacientes"))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones "))
        self.actionInformacion.setText(_translate("MainWindow", "Informacion "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

