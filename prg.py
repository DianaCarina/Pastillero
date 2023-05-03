import sys
from PyQt5.QtWidgets import QApplication, QWidget
from mywidget import Ui_Form

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Creamos una instancia de Ui_Form
        self.ui = Ui_Form()

        # Configuramos la interfaz gráfica
        self.ui.setupUi(self)
        self.pushButton = self.ui.pushButton

        self.ui.pushButton.clicked.connect(self.cli)
    
    def cli(self):
        print("Hello")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Creamos una instancia de nuestro widget
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
