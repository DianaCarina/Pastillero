# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Medica(object):
    def setupUi(self, Medica):
        Medica.setObjectName("Medica")
        Medica.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Medica)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Medica)
        self.pushButton.setGeometry(QtCore.QRect(120, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Medica)
        QtCore.QMetaObject.connectSlotsByName(Medica)

    def retranslateUi(self, Medica):
        _translate = QtCore.QCoreApplication.translate
        Medica.setWindowTitle(_translate("Medica", "Form"))
        self.pushButton.setText(_translate("Medica", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Medica = QtWidgets.QWidget()
    ui = Ui_Medica()
    ui.setupUi(Medica)
    Medica.show()
    sys.exit(app.exec_())
