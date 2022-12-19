import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.LoginController import LoginController
from Views.principal import Ui_Principal
from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.Registrarse import Ui_Ventana_registro

class Ui_LogIn(object):

    def __init__(self):
        self.login_controller = LoginController(self)
        self.registrar = Ui_Ventana_registro()


    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(860, 673)
        LogIn.setMaximumSize(QtCore.QSize(860, 673))
        LogIn.setMouseTracking(True)
        LogIn.setStyleSheet("background-color: rgb(136, 106, 255);")
        self.input_user = QtWidgets.QLineEdit(LogIn)
        self.input_user.setGeometry(QtCore.QRect(300, 250, 181, 31))
        self.input_user.setTabletTracking(False)
        self.input_user.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.input_user.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.input_user.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_user.setAutoFillBackground(False)
        self.input_user.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(220, 222, 255);\n"
"border-radius:15px;\n"
"")
        self.input_user.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_user.setMaxLength(32770)
        self.input_user.setFrame(True)
        self.input_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_user.setCursorPosition(31)
        self.input_user.setDragEnabled(True)
        self.input_user.setReadOnly(False)
        self.input_user.setPlaceholderText("")
        self.input_user.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.input_user.setClearButtonEnabled(False)
        self.input_user.setObjectName("input_user")
        self.bienvenido = QtWidgets.QLabel(LogIn)
        self.bienvenido.setGeometry(QtCore.QRect(200, 110, 381, 91))
        font = QtGui.QFont()
        font.setFamily("BERNIER Distressed")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.bienvenido.setFont(font)
        self.bienvenido.setMouseTracking(False)
        self.bienvenido.setTabletTracking(False)
        self.bienvenido.setObjectName("bienvenido")
        self.input_password = QtWidgets.QLineEdit(LogIn)
        self.input_password.setGeometry(QtCore.QRect(300, 290, 181, 31))
        self.input_password.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(220, 222, 255);\n"
"border-radius:15px;\n"
"")
        self.input_password.setMaxLength(32775)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_password.setCursorPosition(31)
        self.input_password.setDragEnabled(False)
        self.input_password.setClearButtonEnabled(False)
        self.input_password.setObjectName("input_password")
        self.btn_login = QtWidgets.QPushButton(LogIn)
        self.btn_login.setGeometry(QtCore.QRect(350, 340, 91, 21))
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setMouseTracking(False)
        self.btn_login.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_login.setToolTipDuration(1)
        self.btn_login.setAutoFillBackground(False)
        self.btn_login.setStyleSheet("")
        self.btn_login.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btn_login.setCheckable(False)
        self.btn_login.setAutoRepeat(False)
        self.btn_login.setAutoExclusive(True)
        self.btn_login.setAutoDefault(True)
        self.btn_login.setDefault(False)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")
        self.Boto_Registrarse = QtWidgets.QCommandLinkButton(LogIn)
        self.Boto_Registrarse.setGeometry(QtCore.QRect(320, 391, 161, 41))
        self.Boto_Registrarse.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Boto_Registrarse.setObjectName("Boto_Registrarse")

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

        self.x = self.btn_login.clicked.connect(lambda:self.login_controller.logIn(self.input_user.text(),self.input_password.text(),Ui_Principal,LogIn))

        self.Boto_Registrarse.clicked.connect(self.IrRegistro)

    def IrRegistro(self):
        self.regi = QtWidgets.QMainWindow()
        self.ui = Ui_Ventana_registro()
        self.ui.setupUi(self.regi)
        self.regi.show()



    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "MainWindows"))
        self.input_user.setText(_translate("LogIn", "                Ingrese usuario"))
        self.bienvenido.setText(_translate("LogIn", "Bienvenido"))
        self.input_password.setText(_translate("LogIn", "             Ingrese Contraseña"))
        self.btn_login.setText(_translate("LogIn", "INICIAR SESION"))
        self.Boto_Registrarse.setText(_translate("LogIn", "Registrarse aqui"))
        self.Boto_Registrarse.setShortcut(_translate("LogIn", "|"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
