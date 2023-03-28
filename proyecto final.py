from pastillero import *
import sqlite3


class windows (Ui_MainWindow, QtWidgets.QMainWindow, QtWidgets.QLineEdit, QtWidgets.QTableWidget):
    def __init__ (self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)  
        # Default values      
        self.tabWidget.setCurrentIndex(0)
        self.inicio.setEnabled(True)
        self.ingresar.setEnabled(False)
        self.tab.setEnabled(False)
        self.preguntas.setEnabled(False)
        self.tabla.setEnabled(False)
        self.c = 0
        self.lista = []
        self.siguiente.clicked.connect(self.registro)
        self.finalizar.clicked.connect(self.fin)
        self.pushButton_2.clicked.connect(self.old)
        self.pushButton.clicked.connect(self.nuevo)
        self.pushButton_3.clicked.connect(self.adelante)
        self.agregar.clicked.connect(self.agg_pastilla) # Boton agg pastilla
        self.inicio_2.clicked.connect(self.regresar)
        self.pushButton_4.clicked.connect(self.mod)

    def mod (self):
        self.tabla.setEnabled(False)
        self.ingresar.setEnabled(True)
        self.tabWidget.setCurrentIndex(2)
        self.lineEdit.setText(self.idea)
        self.lineEdit_2.setText(self.o[1])
        self.lineEdit_3.setText(self.o[2])
        self.lineEdit_4.setText(self.o[3])

    def nuevo (self):
        self.inicio.setEnabled(False)
        self.ingresar.setEnabled(True)
        self.tabWidget.setCurrentIndex(2)

    def old (self):
        self.tab.setEnabled(True)
        self.inicio.setEnabled(False)
        self.tabWidget.setCurrentIndex(1)

    def adelante(self):
        self.tab.setEnabled(False)

        self.idea = self.lineEdit_9.text().upper()
        f = open (" " + str(self.idea) + ".txt",'r+')
        self.b = f.read()
        self.o = self.b.split(",")

        nomed = self.o[3]
        no_med = nomed[2]

        self.label_4.setText(self.idea)
        self.label_5.setText(self.o[1])
        self.label_6.setText(self.o[2].upper())
        self.label_9.setText(no_med)

        self.be = 0
        self.fin = int(no_med)
        
        self.uno = 4
        self.dos = 5
        self.tres = 6
        self.diana = 7

        while (self.be<self.fin):
            self.tableWidget.verticalHeaderItem(self.be).setText(self.o[self.uno].upper())
            self.tableWidget.item(self.be, 2).setText(self.o[self.dos])
            self.tableWidget.item (self.be, 0).setText(self.o[self.tres].upper())
            self.tableWidget.item (self.be, 1).setText(self.o[self.diana])

            self.be += 1
            self.uno += 4
            self.dos += 4
            self.tres += 4
            self.diana += 4

        while(self.fin<6):
            self.tableWidget.verticalHeaderItem(self.be).setText(" ")
            self.tableWidget.item(self.be, 2).setText(" ")
            self.tableWidget.item (self.be, 0).setText(" ")
            self.tableWidget.item (self.be, 1).setText(" ")

            self.fin += 1
            self.be += 1

        self.tabla.setEnabled(True)
        self.tabWidget.setCurrentIndex(4)
        self.lineEdit_9.clear()

    def agg_pastilla(self):
        self.miConexion = sqlite3.connect("Pastillero")
        self.miCursor = self.miConexion.cursor()

        self.registro_Px = [
            (self.lineEdit.text(), int(self.lineEdit_2.text()), self.lineEdit_3.text(), int(self.lineEdit_4.text()))]
        
        self.miCursor.executemany("INSERT INTO PASTILLERO VALUES (NULL,?,?,?,?)", self.registro_Px)

        self.miConexion.commit()
        self.miConexion.close()

        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        
        if (self.c > 5):
            self.agregar.setEnabled(False)
    
    def fin (self):
        self.preguntas.setEnabled(False)
        self.tabla.setEnabled(True)
        
        self.fi = int (self.lineEdit_4.text())
        
        while(self.fi<6):
            self.tableWidget.verticalHeaderItem(self.fi).setText(" ")
            self.tableWidget.item(self.fi, 2).setText(" ")
            self.tableWidget.item (self.fi, 0).setText(" ")
            self.tableWidget.item (self.fi, 1).setText(" ")

            self.fi += 1
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        
        self.tabWidget.setCurrentIndex(4)
        
    def registro(self):
    
        self.label_4.setText(self.lineEdit.text())
        self.label_5.setText(self.lineEdit_2.text())
        self.label_6.setText(self.lineEdit_3.text())
        self.label_9.setText(self.lineEdit_4.text())

        self.n = self.lineEdit.text()

        self.lista.append (self.lineEdit.text())
        self.lista.append (self.lineEdit_2.text())
        self.lista.append (self.lineEdit_3.text())
        self.lista.append (self.lineEdit_4.text())

        self.ingresar.setEnabled(False)
        self.tabla.setEnabled(False)
        self.inicio.setEnabled(False)
        self.preguntas.setEnabled(True)
        
        self.tabWidget.setCurrentIndex(3)

    def regresar(self):
        
        self.label_4.setText(" ")
        self.label_5.setText(" ")
        self.label_6.setText(" ")
        self.label_7.setText(" ")
        
        giu = 0
        
        while(giu<6):
            self.tableWidget.verticalHeaderItem(giu).setText(" ")
            self.tableWidget.item(giu, 2).setText(" ")
            self.tableWidget.item (giu, 0).setText(" ")
            self.tableWidget.item (giu, 1).setText(" ")

            giu += 1

        self.inicio.setEnabled(True)
        self.tabla.setEnabled(False)
        
        self.tabWidget.setCurrentIndex(0)
        
        
if __name__=="__main__":
    app=QtWidgets.QApplication([])
    ventana=windows()
    ventana.show()
    app.exec_()
