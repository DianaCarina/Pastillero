from pastillero import *
from advertencia_id import *
from addMe import Ui_Dialog
import query as query


class ProgramaPrincipal(Ui_MainWindow, QtWidgets.QMainWindow, QtWidgets.QLineEdit, QtWidgets.QTableWidgetItem):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        # Iniciar el programa en la primera pestaña
        self.tabWidget.setCurrentIndex(0)
        self.tab_inicio.setEnabled(True)
      #  self.tab_inicioSesion.setEnabled(False)
      #  self.tab_registro_medicamento.setEnabled(False)
        self.tab_registro_px.setEnabled(False)
        self.tab_tabla_px.setEnabled(False)
        # Eventos con sus slots 
        self.btn_busqueda.clicked.connect(self.busquedaTab)
        self.btn_registrarce.clicked.connect(self.registroPxTab)
        self.btn_registrar_px.clicked.connect(self.regMedTab)
        self.btn_end_med.clicked.connect(self.pastilleroView)
        self.btn_pxView.clicked.connect(self.inicioSesion)
        self.btn_back_inicio.clicked.connect(self.regresarMenuPrincipal)
        self.btn_add_med.clicked.connect(self.addMedicamento)
        self.btn_modificar.clicked.connect(self.modificar)
        self.btn_record_med.clicked.connect(self.addNewMEd)
        self.btn_updateBox.clicked.connect(self.rellenarCBox)
        self.btn_regresar_main.clicked.connect(self.regresarMenuPrincipal)
        self.btn_regresar_2.clicked.connect(self.regresarMenuPrincipal)
        self.lEdit_nombre_reg.textChanged.connect(self.limpiaLineEdit)
        self.lEdit_Dx.textChanged.connect(self.limpiaLineEdit)
        self.lEdit_User.textChanged.connect(self.limpiaLineEdit)
        self.lEdit_Password.textChanged.connect(self.limpiaLineEdit)
        self.lEdit_edad_reg.textChanged.connect(self.limpiaLineEdit)
        self.lEdit_NoSS.textChanged.connect(self.limpiaLineEdit)
        self.rellenarCBox()
        self.lista_medicamentos = []

    def inicioSesion(self):
        self.nombre_usuario = self.nombre_ingresar.text()
        self.contra_user = self.lbl_password.text()
        self.consulta_inicio = query.Paciente(User = self.nombre_usuario, password=self.contra_user)
        self.verificacion = self.consulta_inicio.consultaInicioSesion()
        print(self.verificacion)
        if self.verificacion is None:
            self.lbl_n_user.setText("Usuario o contraseña no validos")
        else:
            self.lbl_n_user.clear()
            self.TablaTab(self.verificacion[0])
        
    def limpiaLineEdit(self):
        self.lbl_corregir.setText("")

    def registroPxTab(self):
    # Cambio a pestaña de registro de datos del PX
        self.tabWidget.setCurrentIndex(1)
        self.tab_registro_px.setEnabled(True)
        self.tab_inicio.setEnabled(False)
        self.tab_tabla_px.setEnabled(False)
    
    def regresarMenuPrincipal(self):
    # Se regresa a la pestaña principal
        self.tabWidget.setCurrentIndex(0)
        self.tab_inicio.setEnabled(True)
        self.tab_registro_px.setEnabled(False)
        self.tab_inicioSesion.setEnabled(False)
        self.tab_tabla_px.setEnabled(False)

    def addMedicamento(self):
    # Aqui se seleccionas los medicamentos del combobox y 
    # los guarda en la base de datos de los medicamentos que toma el paciente
        self.len_med = len(self.lista_medicamentos)
        if self.len_med < 5:
            self.NombreMedicamento = self.comboBox.currentText()
            self.queryMed = query.Medicamento(self.NombreMedicamento)
            self.IDMed = self.queryMed.medQuery2()
            if self.lista_medicamentos.count(self.IDMed) > 0:
                self.label_9.setText(f"Medicamentos seleccionados: {str(len(self.lista_medicamentos))}\nNo se puede agregar un medicamento dos veces")
            else:
                self.lista_medicamentos.append(self.IDMed)
                print(self.lista_medicamentos)
                self.label_9.setText(f"Medicamentos seleccionados: {str(len(self.lista_medicamentos))}")
        else:
            self.label_9.setText(f"Medicamentos seleccionados: {str(len(self.lista_medicamentos))} \nYa no es posible agregar mas medicamentos")


    def modificar(self):
    # Aqui se modificaran los componentes de la tabla
        self.tabWidget.setCurrentIndex(1)
        self.label_2.setText("Modificar datos del paciente")
        self.queryDatos = query.Paciente(self.lbl_NoSocial.text())
        self.data_px = self.queryDatos.consultaIdPX2()
        print(self.data_px)

    def busquedaTab(self):
    # Cambio de pestaña para el usuario y contraseña
        self.tabWidget.setCurrentIndex(3)
        self.tab_inicioSesion.setEnabled(True)
        self.tab_inicio.setEnabled(False)
        
    def TablaTab(self, parametro1):
    # Cambio a la Tabla para ver los medicamentos registrados
        self.tabWidget.setCurrentIndex(4)
        self.tab_tabla_px.setEnabled(True)
        self.tab_inicioSesion.setEnabled(False)
        self.tab_registro_medicamento.setEnabled(False)
        self.nombre_ingresar.clear()
        self.lbl_password.clear()

        self.tratamiento_ = query.Tratamiento(id_usuario=parametro1)
        self.tratamiento1 = self.tratamiento_.consultaTratamiento()
        print("tratamiento: ", self.tratamiento1)

        self.consulta_datos_px = query.Paciente(id=parametro1)
        self.datosPX = self.consulta_datos_px.consultaIdPX2()
        print("datos del paciente: ", self.datosPX)

        self.lbl_nombre.setText("Nombre: " +self.datosPX[1])
        self.lbl_edad.setText("Edad: " + str(self.datosPX[3]) + " años")
        self.lbl_Dx.setText("Padecimento: " + self.datosPX[2])
        self.lbl_NoSocial.setText(str(self.datosPX[4]))
        for i in range(5):
            self.nombre_item = QtWidgets.QTableWidgetItem(self.tratamiento1[i])
            self.tabla_medicamentos.setItem(0, i, self.nombre_item)


    def addNewMEd(self):
    # Se abre una nueva pestaña para agregar un medicamento que no esta en la BD
        nuevoMeciamentoWidget.show()

    def regMedTab(self):
    # Captura de los datos del px de los line edit
        line_edits = [self.lEdit_nombre_reg, self.lEdit_Dx, self.lEdit_User, self.lEdit_Password, self.lEdit_edad_reg, self.lEdit_NoSS]
        if all(line_edit.text() for line_edit in line_edits):
            self.nombrePx = self.lEdit_nombre_reg.text()
            self.padecimiento = self.lEdit_Dx.text()
            self.user = self.lEdit_User.text()
            self.password = self.lEdit_Password.text()
            try:
                self.edad = int(self.lEdit_edad_reg.text())
                self.NoSS = int(self.lEdit_NoSS.text())
            except:
                self.lbl_corregir.setText("*Ingrese la edad  y el numero de servicio social en numero*")
            else:
                try:
                    # Insertar los datos en la base de datos
                    self.RegistroPaciente = query.Paciente(self.nombrePx, self.padecimiento, self.edad, self.NoSS, self.user, self.password)
                    self.RegistroPaciente.registroPX()
                    # Cambio a pestaña info medicameto
                    self.tabWidget.setCurrentIndex(2)                    
                    self.tab_registro_medicamento.setEnabled(True)
                    self.tab_registro_px.setEnabled(False)
                    # Limpiar lineedit
                    for line in line_edits:
                        line.clear()
                except:
                    self.lbl_corregir.setText("Error en la insersion de datos")
        else:
            self.lbl_corregir.setText("*Agregar correctamente los campos*")
                
    def pastilleroView(self):
    # Funcion para agregar el TRATAMIENTO
        # Si se seleccionaron menos de 5 medicamentos, se rellenan los espacios
        self.faltantes = 5 - len(self.lista_medicamentos) # verificar cuantos elementos tiene la lista
        if self.faltantes > 0:
            for n in range(5-self.faltantes, 5): # verificar de que indice empezar
                self.lista_medicamentos.append("1")
        # print("Lista de medicamentos", self.lista_medicamentos)

        # Se busca el id del usuario 
        self.id2 = self.busqueda_id_usuario()
        
        # Insertar los medicmamentos en la tabla tratamiento
        self.queryTratamiento = query.Tratamiento(self.lista_medicamentos, self.id2)
        self.queryTratamiento.insertTrat()
        # Cambio pestañas
        self.TablaTab(self.id2)

    def busqueda_id_usuario(self):
    # Busqueda del id del paciente
        self.queryID = query.Paciente(User=self.user)
        self.queryID_PX = self.queryID.consultaIdPX()
        self.queryID_PX = self.queryID_PX[0]
        return self.queryID_PX

    def rellenarCBox(self):
    # Funcion para agregar medicamentos a la combobox
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
                pass

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
        self.agregar = query.Medicamento(id_medicamento = self.id_med, medicamento = self.medicamento)
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
