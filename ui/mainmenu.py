# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mm_main(object):
	def loginCheck(self):
		LoginMenuCall()
    def setupUi(self, mm_main):
        mm_main.setObjectName("mm_main")
        mm_main.resize(800, 600)
        mm_main.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(mm_main)
        self.centralwidget.setObjectName("centralwidget")
        self.mm_title = QtWidgets.QLabel(self.centralwidget)
        self.mm_title.setGeometry(QtCore.QRect(260, 50, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.mm_title.setFont(font)
        self.mm_title.setObjectName("mm_title")
        self.mm_logininput = QtWidgets.QTextEdit(self.centralwidget)
        self.mm_logininput.setGeometry(QtCore.QRect(270, 180, 231, 31))
        self.mm_logininput.setObjectName("mm_logininput")
        self.mm_logintitle = QtWidgets.QLabel(self.centralwidget)
        self.mm_logintitle.setGeometry(QtCore.QRect(200, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mm_logintitle.setFont(font)
        self.mm_logintitle.setObjectName("mm_logintitle")
        self.mm_passwordtitle = QtWidgets.QLabel(self.centralwidget)
        self.mm_passwordtitle.setGeometry(QtCore.QRect(160, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mm_passwordtitle.setFont(font)
        self.mm_passwordtitle.setObjectName("mm_passwordtitle")
        self.mm_passinput = QtWidgets.QTextEdit(self.centralwidget)
        self.mm_passinput.setGeometry(QtCore.QRect(270, 230, 231, 31))
        self.mm_passinput.setObjectName("mm_passinput")
        self.mm_loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.mm_loginbutton.setGeometry(QtCore.QRect(270, 290, 101, 41))
        self.mm_loginbutton.setObjectName("mm_loginbutton")
		################## LOGIN BUTTON EVENT ###################
		self.mm_loginbutton.clicked.connect(self.loginCheck)
		##########################################################
        self.mm_forgotbutton = QtWidgets.QPushButton(self.centralwidget)
        self.mm_forgotbutton.setGeometry(QtCore.QRect(400, 290, 101, 41))
        self.mm_forgotbutton.setDefault(False)
        self.mm_forgotbutton.setFlat(False)
        self.mm_forgotbutton.setObjectName("mm_forgotbutton")
        mm_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mm_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mm_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mm_main)
        self.statusbar.setObjectName("statusbar")
        mm_main.setStatusBar(self.statusbar)

        self.retranslateUi(mm_main)
        QtCore.QMetaObject.connectSlotsByName(mm_main)

    def retranslateUi(self, mm_main):
        _translate = QtCore.QCoreApplication.translate
        mm_main.setWindowTitle(_translate("mm_main", "EduSuite"))
        self.mm_title.setText(_translate("mm_main", "EduSuite"))
        self.mm_logininput.setHtml(_translate("mm_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mm_logintitle.setText(_translate("mm_main", "Login:"))
        self.mm_passwordtitle.setText(_translate("mm_main", "Password:"))
        self.mm_passinput.setHtml(_translate("mm_main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mm_loginbutton.setText(_translate("mm_main", "Login"))
        self.mm_forgotbutton.setText(_translate("mm_main", "Forgot Password"))