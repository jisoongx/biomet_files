# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Downloads\biomet_files\loginnew.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtCore import QTimer


class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(910, 610)
                self.ctuBG = QtWidgets.QLabel(Form)
                self.ctuBG.setGeometry(QtCore.QRect(0, 0, 910, 610))
                self.ctuBG.setStyleSheet("background-image: url(D:/Downloads/biomet_files/images/ctu-bg.jpg);\n"
        "background-blend-mode: overlay;\n"
        "background-color: rgba(218, 212, 181, 0.4);\n"
        "")
                self.ctuBG.setText("")
                self.ctuBG.setObjectName("ctuBG")
                self.seethroughBlackBG = QtWidgets.QLabel(Form)
                self.seethroughBlackBG.setGeometry(QtCore.QRect(90, 80, 731, 431))
                self.seethroughBlackBG.setStyleSheet("background-color: rgb(0, 0, 0,190);\n"
        "border-radius: 15px;\n"
        "")
                self.seethroughBlackBG.setText("")
                self.seethroughBlackBG.setObjectName("seethroughBlackBG")
                self.ctuBG_2 = QtWidgets.QLabel(Form)
                self.ctuBG_2.setGeometry(QtCore.QRect(0, 0, 910, 610))
                self.ctuBG_2.setStyleSheet("background-color: rgb(218, 212, 181,130);")
                self.ctuBG_2.setText("")
                self.ctuBG_2.setObjectName("ctuBG_2")
                self.welcomeLabel = QtWidgets.QLabel(Form)
                self.welcomeLabel.setGeometry(QtCore.QRect(340, 130, 241, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.welcomeLabel.setFont(font)
                self.welcomeLabel.setStyleSheet("color: rgb(255, 255, 255);")
                self.welcomeLabel.setScaledContents(False)
                self.welcomeLabel.setWordWrap(False)
                self.welcomeLabel.setObjectName("welcomeLabel")

                self.startBtn = QtWidgets.QPushButton(Form)
                self.startBtn.setGeometry(QtCore.QRect(390, 420, 141, 35))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.startBtn.setFont(font)
                self.startBtn.setStyleSheet("background-color: rgb(153, 51, 51);\n"
        "border: 0;\n"
        "border-radius: 4px;\n"
        "color: rgb(255, 255, 255);")
                self.startBtn.setObjectName("startBtn")

                self.startBtn.clicked.connect(self.changeToGif)

                self.whiteBG = QtWidgets.QLabel(Form)
                self.whiteBG.setGeometry(QtCore.QRect(370, 200, 181, 181))
                self.whiteBG.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 10px;")
                self.whiteBG.setText("")
                self.whiteBG.setObjectName("whiteBG")
                self.scanFingerprint = QtWidgets.QLabel(Form)
                self.scanFingerprint.setGeometry(QtCore.QRect(380, 210, 160, 160))
                self.scanFingerprint.setStyleSheet("image: url(D:/Downloads/biomet_files/images/login-fingerprint.gif);")
                self.scanFingerprint.setText("")
                self.scanFingerprint.setObjectName("scanFingerprint")

                self.ctuBG.raise_()
                self.ctuBG_2.raise_()
                self.seethroughBlackBG.raise_()
                self.welcomeLabel.raise_()
                self.startBtn.raise_()
                self.whiteBG.raise_()
                self.scanFingerprint.raise_()

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.welcomeLabel.setText(_translate("Form", "Welcome Technologist!"))
                self.startBtn.setText(_translate("Form", "Sart Scanning"))

        def changeToGif(self):
                self.startBtn.setEnabled(False)
                self.startBtn.setGeometry(QtCore.QRect(338, 420, 250, 35))
                self.startBtn.setText("Place your finger on the scanner.")
                
                new_movie = QMovie("D:/Downloads/biomet_files/images/login-fingerprint.gif")
                self.scanFingerprint.setMovie(new_movie)
                self.scanFingerprint.setGeometry(QtCore.QRect(380, 210, 160, 160)) 
                new_movie.setScaledSize(self.scanFingerprint.size())
                QTimer.singleShot(2100, lambda: new_movie.start())
                
                QTimer.singleShot(2100, lambda: self.startBtn.setText("Scanning..."))
                self.startBtn.setStyleSheet("background-color: transparent;\n"
                                        "color: white;\n"
                                        "font-weight: bold;"
                                        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowFlags(Form.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    Form.show()
    sys.exit(app.exec_())
