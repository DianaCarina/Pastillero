from uu import Ui_Medica

class Medica(Ui_Medica):
    def __init__ (self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.kk)

    def kk(self):
        print("lmj")
        print(self.lineEdit.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Medica = QtWidgets.QWidget()
    ui = Ui_Medica()
    ui.setupUi(Medica)
    Medica.show()
    sys.exit(app.exec_())

