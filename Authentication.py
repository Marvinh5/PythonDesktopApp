import  sys, socket
from AuthFrm import Ui_Dialog as AuthFrm
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from uuid import getnode as get_mac
import Data, Config

__author__ = 'marvin'



class Authentication():

    AuthDialog = None

    def __init__(self):
        app = QApplication(sys.argv)
        window = QDialog()
        AuthDialog =  AuthFrm()
        AuthDialog.setupUi(window)
        self.AuthDialog = AuthDialog

        AuthDialog.pushButton.clicked.connect(self.ConnectDatabase)
        AuthDialog.lblMacAddress.setText(AuthDialog.lblMacAddress.text()+str(get_mac()))
        AuthDialog.lblMacAddress.setStyleSheet("QLabel {color:blue;}")

        AuthDialog.lblIp.setText("Host:"+str(socket.gethostname()))
        AuthDialog.lblIp.setStyleSheet("QLabel {color:green;}")

        window.show()
        sys.exit(app.exec_())

    def ConnectDatabase(self):
        try:
            if(self.AuthDialog.lineEdit.text()!='' and self.AuthDialog.lineEdit_2.text()!=''):
                database = Data.Database().connect()
                header, row, len = database.executeQuery("""
                EXEC [dbo].[login]
                        @usuario = N'{usuario}',
                        @password = N'{password}',
                        @MacAddress = N'{mac_address}',
                        @Aplicacion = N'{aplicacion}',
                        @version = N'{version}'
                """.format(usuario=self.AuthDialog.lineEdit.text(),
                      password = self.AuthDialog.lineEdit_2.text(),
                      mac_address = get_mac(),
                      aplicacion = Config.getProperty('applicationname'),
                      version=Config.getProperty('applicationversion')))
                if(len>0):
                    if(int(row[0][0]) == 1):
                        box = QMessageBox()
                        box.setWindowTitle("Alerta")
                        box.setText(str(row[0][1]))
                        box.exec_()
                    else:
                        box = QMessageBox()
                        box.setWindowTitle("Alerta")
                        box.setText(str(row[0][1]))
                        box.exec_()

                else:
                    box = QMessageBox()
                    box.setWindowTitle("Alerta")
                    box.setText("Conexion Erronea")
                    box.exec_()
            else:
                box = QMessageBox()
                box.setWindowTitle("Alerta")
                box.setText("Datos Incorrectos ")
                box.exec_()
        except ValueError:
                box = QMessageBox()
                box.setWindowTitle("Alerta")
                box.setText("Problema con la conexion" + str(ValueError))
                box.exec_()

if __name__ == '__main__':
    Authentication()



