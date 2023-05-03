from addMe import Ui_Dialog
from PyQt5 import  QtWidgets
class dialo(Ui_Dialog, QtWidgets.QDialog, QtWidgets.QLineEdit):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        # Configuramos la interfaz gráfica
        self.setupUi(self)
        self.btn_aggMedicament.clicked.connect(self.addMedDB)
    
    def addMedDB(self):
        a = self.lEdit_Medicamento.text()
        b = self.lineEdit.text()
        print(a, b)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Creamos una instancia de nuestro widget
    widget = dialo()
    widget.show()

    sys.exit(app.exec_())
