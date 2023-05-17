from pastillero import *
from advertencia_id import *
from addMe import Ui_Dialog
import query as query

class ProgramaPrincipal(Ui_MainWindow, QtWidgets.QMainWindow, QtWidgets.QLineEdit):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        # Iniciar el programa en la primera pestaña
        self.tabWidget.setCurrentIndex(0)
        self.tab_inicio.setEnabled(True)
        self.tab_inicioSesion.setEnabled(False)
        self.tab_registro_medicamento.setEnabled(False)
        self.tab_registro_px.setEnabled(False)
        self.tab_tabla_px.setEnabled(False)
        # Eventos con sus slots 
        self.btn_busqueda.clicked.connect(self.busquedaTab)
        self.btn_registrarce.clicked.connect(self.registroPxTab)
        self.btn_registrar_px.clicked.connect(self.regMedTab)
        self.btn_end_med.clicked.connect(self.busquedaTab)
        self.btn_pxView.clicked.connect(self.pastilleroView)
        self.btn_back_inicio.clicked.connect(self.regresarMenuPrincipal)
        self.btn_add_med.clicked.connect(self.addMedicamento)
        self.btn_modificar.clicked.connect(self.modificar)
        self.btn_record_med.clicked.connect(self.addNewMEd)
        self.btn_updateBox.clicked.connect(self.rellenarCBox)
        self.btn_regresar_main.clicked.connect(self.regresarMenuPrincipal)
        self.btn_regresar_2.clicked.connect(self.regresarMenuPrincipal)

    def registroPxTab(self):
        # Cambio a pestaña de registro PX
        self.tabWidget.setCurrentIndex(1)
        self.tab_registro_px.setEnabled(True)
        self.tab_inicio.setEnabled(False)
        self.tab_tabla_px.setEnabled(False)
    
    def regresarMenuPrincipal(self):
        self.tabWidget.setCurrentIndex(0)
        self.tab_inicio.setEnabled(True)
        self.tab_registro_px.setEnabled(False)
        self.tab_inicioSesion.setEnabled(False)
        self.tab_tabla_px.setEnabled(False)

    def addMedicamento(self):
        # Aqui se seleccionas los medicamentos del combobox y 
        # los guarda en la base de datos de los medicamentos que toma el paciente
        self.tab_registro_medicamento.setEnabled(True)
        self.NombreMedicamento = self.comboBox.currentText()
        print(self.NombreMedicamento)

    def modificar(self):
        self.tabWidget.setCurrentIndex(2)

    def busquedaTab(self):
        # Cambio de pestaña para el usuario y contraseña
        self.tabWidget.setCurrentIndex(3)
        self.tab_inicioSesion.setEnabled(True)
        self.tab_inicio.setEnabled(False)

    
    def addNewMEd(self):
        # Cuando se quiere agregar un medicamento que no esta en la lisa
        # se abre una nueva pestaña para agregarlo
        nuevoMeciamentoWidget.show()

    def regMedTab(self):
        # Captura de los datos del px de los line edit
        self.edad = 0
        self.NoSS = 0
        try:
            self.edad = int(self.lEdit_edad_reg.text())
            self.NoSS = int(self.lEdit_NoSS.text())
        except:
            self.lbl_corregir.setText("La edad y el No. Seguro social deben ser con numero")
        
        self.nombrePx = self.lEdit_nombre_reg.text()
        self.padecimiento = self.lEdit_Dx.text()
        self.user = self.lEdit_User.text()
        self.password = self.lEdit_Password.text()

        try:
            # Insertat los datos en la base de datos
            self.RegistroPaciente = query.Paciente(self.nombrePx, self.padecimiento, self.edad, self.NoSS, self.user, self.password)
            self.RegistroPaciente.registroPX()
            # Cambio a pestaña info medicameto
            self.tabWidget.setCurrentIndex(2)
            self.tab_registro_medicamento.setEnabled(True)
            self.tab_registro_px.setEnabled(False)
            # Limpiar lineedit
        except(ValueError):
            self.lbl_corregir.setText("Ingrese valores corretos")

        finally:
            # Rellenar la combobox con los medicamentos existentes en la BD
            self.rellenarCBox()
                
    def pastilleroView(self):
        # Cambio a la pestaña de visualizar los medicamentos
        self.tabWidget.setCurrentIndex(4)
        self.tab_tabla_px.setEnabled(True)
        self.tab_inicioSesion.setEnabled(False)
    
    def rellenarCBox(self):
        self.rellenar = query.Medicamento(5, "medicamento")
        self.records = self.rellenar.medQuery()
        # Por cada registro rellenamos la combobox
        for registro in self.records:
            self.busqueda = self.comboBox.findText(registro[1])
            # Nos aseguramos que no exista el medicamento ya registrado en la combobox
            if self.busqueda == -1:
                self.comboBox.addItem(registro[1])
            # Si ya existe dejamos pasar
            else:
                print(self.busqueda)

class Ui_Form(Ui_Form, QtWidgets.QMainWindow):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 

class AgregarMedicamento(Ui_Dialog, QtWidgets.QDialog, QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.btn_aggMedicament.clicked.connect(self.addMedDB)

    def addMedDB(self):
        # Aqui se guarda el nuevo medicamento a la base de datos desde el Qdialog
        self.medicamento = self.lEdit_Medicamento.text()
        self.id_med = self.medicamento[1:4].upper() + "1"
        self.agregar = query.Medicamento(self.id_med, self.medicamento)
        self.lbl__resultado.setText(self.agregar.registroMedicamento())

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication([])
    # Creamos una instancia del programa principal
    ventana = ProgramaPrincipal()
    ventana.show()

    advertencia = Ui_Form()
    # Creamos una instancia para el dialogo donde se agregamos medicamentos
    nuevoMeciamentoWidget = AgregarMedicamento()

    sys.exit(app.exec_())
