# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pastillero.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 443)
        MainWindow.setMinimumSize(QtCore.QSize(501, 443))
        MainWindow.setMaximumSize(QtCore.QSize(501, 443))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 440))
        self.tabWidget.setMinimumSize(QtCore.QSize(501, 440))
        self.tabWidget.setMaximumSize(QtCore.QSize(501, 440))
        self.tabWidget.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_inicio = QtWidgets.QWidget()
        self.tab_inicio.setObjectName("tab_inicio")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_inicio)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 361, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_registrarce = QtWidgets.QPushButton(self.tab_inicio)
        self.btn_registrarce.setGeometry(QtCore.QRect(270, 260, 176, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_registrarce.setFont(font)
        self.btn_registrarce.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_registrarce.setObjectName("btn_registrarce")
        self.btn_busqueda = QtWidgets.QPushButton(self.tab_inicio)
        self.btn_busqueda.setGeometry(QtCore.QRect(50, 260, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_busqueda.setFont(font)
        self.btn_busqueda.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_busqueda.setObjectName("btn_busqueda")
        self.tabWidget.addTab(self.tab_inicio, "")
        self.tab_registro_px = QtWidgets.QWidget()
        self.tab_registro_px.setObjectName("tab_registro_px")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_registro_px)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 0, 303, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.tab_registro_px)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_registro_px)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_registro_px)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_registro_px)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lEdit_nombre_reg = QtWidgets.QLineEdit(self.tab_registro_px)
        self.lEdit_nombre_reg.setGeometry(QtCore.QRect(200, 110, 211, 21))
        self.lEdit_nombre_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_nombre_reg.setObjectName("lEdit_nombre_reg")
        self.lEdit_edad_reg = QtWidgets.QLineEdit(self.tab_registro_px)
        self.lEdit_edad_reg.setGeometry(QtCore.QRect(200, 150, 211, 21))
        self.lEdit_edad_reg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_edad_reg.setObjectName("lEdit_edad_reg")
        self.lEdit_Dx = QtWidgets.QLineEdit(self.tab_registro_px)
        self.lEdit_Dx.setGeometry(QtCore.QRect(200, 190, 211, 21))
        self.lEdit_Dx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_Dx.setObjectName("lEdit_Dx")
        self.lEdit_NoSS = QtWidgets.QLineEdit(self.tab_registro_px)
        self.lEdit_NoSS.setGeometry(QtCore.QRect(200, 230, 211, 21))
        self.lEdit_NoSS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_NoSS.setObjectName("lEdit_NoSS")
        self.btn_registrar_px = QtWidgets.QPushButton(self.tab_registro_px)
        self.btn_registrar_px.setGeometry(QtCore.QRect(280, 350, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_registrar_px.setFont(font)
        self.btn_registrar_px.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_registrar_px.setObjectName("btn_registrar_px")
        self.lEdit_User = QtWidgets.QLineEdit(self.tab_registro_px)
        self.lEdit_User.setGeometry(QtCore.QRect(200, 270, 211, 21))
        self.lEdit_User.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_User.setObjectName("lEdit_User")
        self.lEdit_Password = QtWidgets.QLineEdit(self.tab_registro_px)
        self.lEdit_Password.setGeometry(QtCore.QRect(200, 300, 211, 21))
        self.lEdit_Password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lEdit_Password.setObjectName("lEdit_Password")
        self.label_13 = QtWidgets.QLabel(self.tab_registro_px)
        self.label_13.setGeometry(QtCore.QRect(40, 300, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_24 = QtWidgets.QLabel(self.tab_registro_px)
        self.label_24.setGeometry(QtCore.QRect(40, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lbl_corregir = QtWidgets.QLabel(self.tab_registro_px)
        self.lbl_corregir.setGeometry(QtCore.QRect(30, 60, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_corregir.setFont(font)
        self.lbl_corregir.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_corregir.setText("")
        self.lbl_corregir.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_corregir.setWordWrap(True)
        self.lbl_corregir.setObjectName("lbl_corregir")
        self.btn_regresar_main = QtWidgets.QPushButton(self.tab_registro_px)
        self.btn_regresar_main.setGeometry(QtCore.QRect(40, 350, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_regresar_main.setFont(font)
        self.btn_regresar_main.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_regresar_main.setObjectName("btn_regresar_main")
        self.tabWidget.addTab(self.tab_registro_px, "")
        self.tab_registro_medicamento = QtWidgets.QWidget()
        self.tab_registro_medicamento.setObjectName("tab_registro_medicamento")
        self.label_11 = QtWidgets.QLabel(self.tab_registro_medicamento)
        self.label_11.setGeometry(QtCore.QRect(50, 160, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.tab_registro_medicamento)
        self.label_15.setGeometry(QtCore.QRect(60, 30, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btn_add_med = QtWidgets.QPushButton(self.tab_registro_medicamento)
        self.btn_add_med.setGeometry(QtCore.QRect(150, 200, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add_med.setFont(font)
        self.btn_add_med.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_add_med.setObjectName("btn_add_med")
        self.btn_end_med = QtWidgets.QPushButton(self.tab_registro_medicamento)
        self.btn_end_med.setGeometry(QtCore.QRect(170, 320, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_end_med.setFont(font)
        self.btn_end_med.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_end_med.setObjectName("btn_end_med")
        self.comboBox = QtWidgets.QComboBox(self.tab_registro_medicamento)
        self.comboBox.setGeometry(QtCore.QRect(220, 150, 211, 31))
        self.comboBox.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.comboBox.setObjectName("comboBox")
        self.btn_record_med = QtWidgets.QPushButton(self.tab_registro_medicamento)
        self.btn_record_med.setGeometry(QtCore.QRect(260, 260, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_record_med.setFont(font)
        self.btn_record_med.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_record_med.setObjectName("btn_record_med")
        self.label_9 = QtWidgets.QLabel(self.tab_registro_medicamento)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setLineWidth(1)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.btn_updateBox = QtWidgets.QPushButton(self.tab_registro_medicamento)
        self.btn_updateBox.setGeometry(QtCore.QRect(30, 260, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_updateBox.setFont(font)
        self.btn_updateBox.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_updateBox.setObjectName("btn_updateBox")
        self.tabWidget.addTab(self.tab_registro_medicamento, "")
        self.tab_inicioSesion = QtWidgets.QWidget()
        self.tab_inicioSesion.setObjectName("tab_inicioSesion")
        self.btn_pxView = QtWidgets.QPushButton(self.tab_inicioSesion)
        self.btn_pxView.setGeometry(QtCore.QRect(280, 290, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_pxView.setFont(font)
        self.btn_pxView.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_pxView.setObjectName("btn_pxView")
        self.nombre_ingresar = QtWidgets.QLineEdit(self.tab_inicioSesion)
        self.nombre_ingresar.setGeometry(QtCore.QRect(230, 130, 211, 21))
        self.nombre_ingresar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre_ingresar.setObjectName("nombre_ingresar")
        self.label_7 = QtWidgets.QLabel(self.tab_inicioSesion)
        self.label_7.setGeometry(QtCore.QRect(80, 130, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lbl_password = QtWidgets.QLineEdit(self.tab_inicioSesion)
        self.lbl_password.setGeometry(QtCore.QRect(230, 190, 211, 21))
        self.lbl_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_password.setObjectName("lbl_password")
        self.label_8 = QtWidgets.QLabel(self.tab_inicioSesion)
        self.label_8.setGeometry(QtCore.QRect(80, 190, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.tab_inicioSesion)
        self.label_14.setGeometry(QtCore.QRect(150, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.btn_regresar_2 = QtWidgets.QPushButton(self.tab_inicioSesion)
        self.btn_regresar_2.setGeometry(QtCore.QRect(30, 290, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_regresar_2.setFont(font)
        self.btn_regresar_2.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_regresar_2.setObjectName("btn_regresar_2")
        self.lbl_n_user = QtWidgets.QLabel(self.tab_inicioSesion)
        self.lbl_n_user.setGeometry(QtCore.QRect(70, 80, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_n_user.setFont(font)
        self.lbl_n_user.setStyleSheet("color:rgb(255, 0, 0)")
        self.lbl_n_user.setText("")
        self.lbl_n_user.setObjectName("lbl_n_user")
        self.tabWidget.addTab(self.tab_inicioSesion, "")
        self.tab_tabla_px = QtWidgets.QWidget()
        self.tab_tabla_px.setObjectName("tab_tabla_px")
        self.btn_back_inicio = QtWidgets.QPushButton(self.tab_tabla_px)
        self.btn_back_inicio.setGeometry(QtCore.QRect(300, 370, 176, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_back_inicio.setFont(font)
        self.btn_back_inicio.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_back_inicio.setObjectName("btn_back_inicio")
        self.btn_modificar = QtWidgets.QPushButton(self.tab_tabla_px)
        self.btn_modificar.setGeometry(QtCore.QRect(20, 370, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_modificar.setFont(font)
        self.btn_modificar.setStyleSheet("background-color: rgb(193, 226, 255);")
        self.btn_modificar.setObjectName("btn_modificar")
        self.tabla_medicamentos = QtWidgets.QTableWidget(self.tab_tabla_px)
        self.tabla_medicamentos.setGeometry(QtCore.QRect(50, 200, 391, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabla_medicamentos.setFont(font)
        self.tabla_medicamentos.setStyleSheet("background-color: rgb(167, 210, 255);")
        self.tabla_medicamentos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabla_medicamentos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tabla_medicamentos.setLineWidth(5)
        self.tabla_medicamentos.setAutoScrollMargin(15)
        self.tabla_medicamentos.setIconSize(QtCore.QSize(20, 20))
        self.tabla_medicamentos.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tabla_medicamentos.setShowGrid(True)
        self.tabla_medicamentos.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tabla_medicamentos.setWordWrap(True)
        self.tabla_medicamentos.setRowCount(5)
        self.tabla_medicamentos.setColumnCount(1)
        self.tabla_medicamentos.setObjectName("tabla_medicamentos")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_medicamentos.setHorizontalHeaderItem(0, item)
        self.tabla_medicamentos.horizontalHeader().setDefaultSectionSize(350)
        self.tabla_medicamentos.horizontalHeader().setMinimumSectionSize(50)
        self.tabla_medicamentos.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_medicamentos.verticalHeader().setDefaultSectionSize(40)
        self.groupBox = QtWidgets.QGroupBox(self.tab_tabla_px)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 441, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lbl_NoSocial = QtWidgets.QLabel(self.groupBox)
        self.lbl_NoSocial.setGeometry(QtCore.QRect(210, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_NoSocial.setFont(font)
        self.lbl_NoSocial.setText("")
        self.lbl_NoSocial.setObjectName("lbl_NoSocial")
        self.lbl_Dx = QtWidgets.QLabel(self.groupBox)
        self.lbl_Dx.setGeometry(QtCore.QRect(10, 80, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_Dx.setFont(font)
        self.lbl_Dx.setObjectName("lbl_Dx")
        self.lbl_edad = QtWidgets.QLabel(self.groupBox)
        self.lbl_edad.setGeometry(QtCore.QRect(10, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_edad.setFont(font)
        self.lbl_edad.setObjectName("lbl_edad")
        self.lbl_nombre = QtWidgets.QLabel(self.groupBox)
        self.lbl_nombre.setGeometry(QtCore.QRect(10, 30, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_social = QtWidgets.QLabel(self.groupBox)
        self.lbl_social.setGeometry(QtCore.QRect(10, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_social.setFont(font)
        self.lbl_social.setObjectName("lbl_social")
        self.label_10 = QtWidgets.QLabel(self.tab_tabla_px)
        self.label_10.setGeometry(QtCore.QRect(190, 10, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_tabla_px, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionInformacion = QtWidgets.QAction(MainWindow)
        self.actionInformacion.setObjectName("actionInformacion")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pastillero"))
        self.label.setText(_translate("MainWindow", "    Bienvenido a su pastillero digital"))
        self.btn_registrarce.setText(_translate("MainWindow", "Registrarce"))
        self.btn_busqueda.setText(_translate("MainWindow", "Iniciar Sesion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inicio), _translate("MainWindow", "Inicio"))
        self.label_2.setText(_translate("MainWindow", "Registro datos del Paciente"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Edad"))
        self.label_5.setText(_translate("MainWindow", "Padecimiento"))
        self.label_6.setText(_translate("MainWindow", "No. Seguro Social"))
        self.btn_registrar_px.setText(_translate("MainWindow", "Registrar"))
        self.label_13.setText(_translate("MainWindow", "Contraseña"))
        self.label_24.setText(_translate("MainWindow", "Usuario"))
        self.btn_regresar_main.setText(_translate("MainWindow", "Regresar a menu principal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registro_px), _translate("MainWindow", "Datos del paciente"))
        self.label_11.setText(_translate("MainWindow", "Medicamento"))
        self.label_15.setText(_translate("MainWindow", "Ingrese los medicamentos, uno por uno"))
        self.btn_add_med.setText(_translate("MainWindow", "Agregar medicamento"))
        self.btn_end_med.setText(_translate("MainWindow", "Concluir registro"))
        self.btn_record_med.setText(_translate("MainWindow", "Registrar nuevo medicamento"))
        self.label_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">kl</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Medicamentos seleccionados: 0"))
        self.btn_updateBox.setText(_translate("MainWindow", "Actualizar lista"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registro_medicamento), _translate("MainWindow", "Registro de medicamentos"))
        self.btn_pxView.setText(_translate("MainWindow", "Iniciar sesion"))
        self.label_7.setText(_translate("MainWindow", "Usuario"))
        self.label_8.setText(_translate("MainWindow", "Contraseña"))
        self.label_14.setText(_translate("MainWindow", "Ingrese los datos"))
        self.btn_regresar_2.setText(_translate("MainWindow", "Regresar a menu principal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inicioSesion), _translate("MainWindow", "Inicio Sesion"))
        self.btn_back_inicio.setText(_translate("MainWindow", "Cerrar Sesion"))
        self.btn_modificar.setText(_translate("MainWindow", "Modificar"))
        self.tabla_medicamentos.setSortingEnabled(False)
        item = self.tabla_medicamentos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lista de medicamentos"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos del paciente."))
        self.lbl_Dx.setText(_translate("MainWindow", "Padecimiento:"))
        self.lbl_edad.setText(_translate("MainWindow", "Edad:"))
        self.lbl_nombre.setText(_translate("MainWindow", "Nombre:"))
        self.lbl_social.setText(_translate("MainWindow", "No. Seguridad Social:"))
        self.label_10.setText(_translate("MainWindow", "Pastillero"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tabla_px), _translate("MainWindow", "Pacientes"))
        self.actionInformacion.setText(_translate("MainWindow", "Informacion "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
