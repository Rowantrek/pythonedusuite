# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import edugui, edufunctions
import sip, sys

class Ui_guif_main(object):
    def setupUi(self, guif_main):
        guif_main.setObjectName("guif_main")
        guif_main.resize(792, 543)
        guif_main.setWindowOpacity(1.0)
        self.guif_maingrid = QtWidgets.QWidget(guif_main)
        self.guif_maingrid.setObjectName("guif_maingrid")
        self.gridLayout = QtWidgets.QGridLayout(self.guif_maingrid)
        self.gridLayout.setObjectName("gridLayout")
        self.guif_mm_main = QtWidgets.QFrame(self.guif_maingrid)
        self.guif_mm_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guif_mm_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guif_mm_main.setObjectName("guif_mm_main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.guif_mm_main)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.guif_mm_grid_secondary = QtWidgets.QGridLayout()
        self.guif_mm_grid_secondary.setObjectName("guif_mm_grid_secondary")
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_mm_grid_secondary.addItem(spacerItem1, 1, 0, 1, 1)
        self.guif_mm_title = QtWidgets.QLabel(self.guif_mm_main)
        self.guif_mm_title.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guif_mm_title.setFont(font)
        self.guif_mm_title.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_mm_title.setObjectName("guif_mm_title")
        self.guif_mm_grid_secondary.addWidget(self.guif_mm_title, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.guif_mm_btn_login = QtWidgets.QPushButton(self.guif_mm_main)
        self.guif_mm_btn_login.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.guif_mm_btn_login.setFont(font)
        self.guif_mm_btn_login.setObjectName("guif_mm_btn_login")
        # EVENT HANDLER LOGIN
        self.guif_mm_btn_login.clicked.connect(self.login_btn)
        self.horizontalLayout.addWidget(self.guif_mm_btn_login)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.guif_mm_btn_reg = QtWidgets.QPushButton(self.guif_mm_main)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.guif_mm_btn_reg.setFont(font)
        self.guif_mm_btn_reg.setObjectName("guif_mm_btn_reg")
        # EVENT HANDLER REGISTER
        self.guif_mm_btn_reg.clicked.connect(self.reg_btn)
        self.horizontalLayout.addWidget(self.guif_mm_btn_reg)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.guif_mm_grid_secondary.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.guif_mm_grid_secondary, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.guif_mm_main, 0, 0, 1, 1)
        guif_main.setCentralWidget(self.guif_maingrid)
        self.statusbar = QtWidgets.QStatusBar(guif_main)
        self.statusbar.setObjectName("statusbar")
        guif_main.setStatusBar(self.statusbar)

        self.retranslateUi(guif_main)
        QtCore.QMetaObject.connectSlotsByName(guif_main)

    def retranslateUi(self, guif_main):
        _translate = QtCore.QCoreApplication.translate
        self.guif_mm_title.setText(_translate("guif_main", "EduSuite"))
        self.guif_mm_btn_login.setText(_translate("guif_main", "  Login  "))
        self.guif_mm_btn_reg.setText(_translate("guif_main", "Register"))
        
    def login_btn(self):
        edugui.MenuHandler.LoginMenu()
        
    def reg_btn(self):
        edugui.MenuHanlder.RegisterMenu()
        
class MainGUI(object):
       def init():
        app = QtWidgets.QApplication(sys.argv)
        guif_main = QtWidgets.QMainWindow()
        
        guif_main.setObjectName("guif_main")
        guif_main.resize(792, 543)
        guif_main.setWindowOpacity(1.0)
        
        guif_main.showMaximized()
        
        _translate = QtCore.QCoreApplication.translate
        guif_main.setWindowTitle(_translate("guif_main", "EduSuite"))
        
        edugui.MenuHandler.MainMenu()
        return (guif_main)
        
        sys.exit(app.exec_())
        

        
        



