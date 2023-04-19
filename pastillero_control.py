from pastillero import *
from advertencia_id import *
import query as query

class Ui_MainWindow(Ui_MainWindow, QtWidgets.QMainWindow, QtWidgets.QLineEdit):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        self.tabWidget.setCurrentIndex(0)
        self.btn_busqueda.clicked.connect(self.busquedaTab)
        self.btn_registrarce.clicked.connect(self.registroPxTab)
        self.btn_registrar_px.clicked.connect(self.regMedTab)
        self.btn_end_med.clicked.connect(self.busquedaTab)
        self.btn_pxView.clicked.connect(self.pastilleroView)
        self.btn_back_inicio.clicked.connect(self.cerrarSesion)
        self.btn_add_med.clicked.connect(self.addMedicamento)
        self.btn_modificar.clicked.connect(self.modificar)

    def modificar(self):
        self.tabWidget.setCurrentIndex(2)

    def addMedicamento(self):
        # En este metodo se guarda el nombre del medicamento en la base de datos
        self.NombreMedicamento = self.linEdit_Medicamento.text()
        self.aviso = query.Medicamento(self.NombreMedicamento)
    
    def cerrarSesion(self):
        self.tabWidget.setCurrentIndex(0)

    def busquedaTab(self):
        self.tabWidget.setCurrentIndex(3)

    def registroPxTab(self):
        # En este metodo guardamos la info del px en la base de datos
        self.tabWidget.setCurrentIndex(1)
    
    def regMedTab(self):
        # Cambio a pestaña info medicameto
        self.tabWidget.setCurrentIndex(2)
        # Captura de los datos en los line edit
        self.nombrePx = self.lEdit_nombre_reg.text()
        self.edad = int(self.lEdit_edad_reg.text())
        self.padecimiento = self.lEdit_Dx.text()
        self.NoSS = int(self.lEdit_NoSS.text())
        self.user = self.lEdit_User.text()
        self.password = self.lEdit_Password.text()
        # Insertat los datos en la base de datos
        self.RegistroPAciente = query.Paciente(self.nombrePx, self.padecimiento, self.edad, self.NoSS, self.user, self.password)
        self.RegistroPAciente.registro()
    
    def pastilleroView(self):
        self.tabWidget.setCurrentIndex(4)
    

class Ui_Form(Ui_Form, QtWidgets.QMainWindow):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication([])
    ventana = Ui_MainWindow()
    advertencia = Ui_Form()
    ventana.show()
    sys.exit(app.exec_())
