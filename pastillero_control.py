from Pastillero import *
from advertencia_id import *
from addMe import Ui_Dialog
import query as query

class ProgramaPrincipal(Ui_MainWindow, QtWidgets.QMainWindow, QtWidgets.QLineEdit):
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
        self.btn_record_med.clicked.connect(self.addNewMEd)

    def modificar(self):
        self.tabWidget.setCurrentIndex(2)

    def addMedicamento(self):
        # En este metodo se guarda el nombre del medicamento en la base de datos
        self.NombreMedicamento = self.linEdit_Medicamento.text()
        self.aviso = query.Medicamento(self.NombreMedicamento)
    
    def cerrarSesion(self):
        # Cambio de pestaña al inico del programa
        self.tabWidget.setCurrentIndex(0)

    def busquedaTab(self):
        # Cambio de pestaña para el usuario y contraseña
        self.tabWidget.setCurrentIndex(3)

    def registroPxTab(self):
        # Cambio a pestaña de registro PX
        self.tabWidget.setCurrentIndex(1)
    
    def addNewMEd(self):
        pass
     #   Dialog.show()

    def regMedTab(self):
        # En este metodo guardamos la info del px en la base de datos
        # Captura de los datos en los line edit
        self.lbl_corregir.setText("")
        try:
            self.nombrePx = self.lEdit_nombre_reg.text()
            self.edad = int(self.lEdit_edad_reg.text())
            self.padecimiento = self.lEdit_Dx.text()
            self.NoSS = int(self.lEdit_NoSS.text())
            self.user = self.lEdit_User.text()
            self.password = self.lEdit_Password.text()
            # Insertat los datos en la base de datos
            self.RegistroPAciente = query.Paciente(self.nombrePx, self.padecimiento, self.edad, self.NoSS, self.user, self.password)
            self.RegistroPAciente.registroPX()
            # Cambio a pestaña info medicameto
            self.tabWidget.setCurrentIndex(2)
            self.comboBox.addItem("Buenas")
        except(ValueError):
            self.lbl_corregir.setText("Ingrese valores corretos")
            print("Corrija el numero")
                
    def pastilleroView(self):
        # Cambio a la pestaña de visualizar los medicamentos
        self.tabWidget.setCurrentIndex(4)
    
    def rellenarCBox(self):
        pass

class Ui_Form(Ui_Form, QtWidgets.QMainWindow):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 

class AgregarMedicamento(Ui_Dialog, QtWidgets.QDialog, QtWidgets.QLineEdit):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.btn_aggMedicament.click()
        self.btn_aggMedicament.clicked.connect(self.addMedDB)
        print("Si se ejecuta")

    def addMedDB(self):
        self.medicamento = self.lEdit_Medicamento.text()
        print(self.medicamento)
        self.id_med = self.medicamento[1:4].upper() + "1"
        self.agregar = query.Medicamento(self.id_med, self.medicamento)
        self.agregar.registroMedicamento()

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication([])
    ventana = ProgramaPrincipal()
    ventana.show()
    advertencia = Ui_Form()
    widget = AgregarMedicamento()
    widget.show()

    sys.exit(app.exec_())
