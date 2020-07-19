# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 843)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, -10, 301, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 281, 211))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("venv/Include/exchange.png"))
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 320, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 410, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 500, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 590, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 710, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CURRENCY CONVERTER"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
