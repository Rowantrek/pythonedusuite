# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Guif_lm_main(object):
    def setupUi(self, Guif_lm_main):
        Guif_lm_main.setObjectName("Guif_lm_main")
        Guif_lm_main.resize(419, 315)
        Guif_lm_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Guif_lm_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guif_lm_maingrid = QtWidgets.QGridLayout(Guif_lm_main)
        self.guif_lm_maingrid.setObjectName("guif_lm_maingrid")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_lm_maingrid.addItem(spacerItem, 5, 0, 1, 1)
        self.guif_lm_title = QtWidgets.QLabel(Guif_lm_main)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.guif_lm_title.setFont(font)
        self.guif_lm_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.guif_lm_title.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_lm_title.setObjectName("guif_lm_title")
        self.guif_lm_maingrid.addWidget(self.guif_lm_title, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_lm_maingrid.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.guif_lm_label_user = QtWidgets.QLabel(Guif_lm_main)
        self.guif_lm_label_user.setObjectName("guif_lm_label_user")
        self.horizontalLayout.addWidget(self.guif_lm_label_user)
        self.guif_lm_textEdit_user = QtWidgets.QLineEdit(Guif_lm_main)
        self.guif_lm_textEdit_user.setObjectName("guif_lm_textEdit_user")
        self.horizontalLayout.addWidget(self.guif_lm_textEdit_user)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.guif_lm_maingrid.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_lm_maingrid.addItem(spacerItem4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.guif_lm_label_pass = QtWidgets.QLabel(Guif_lm_main)
        self.guif_lm_label_pass.setObjectName("guif_lm_label_pass")
        self.horizontalLayout_2.addWidget(self.guif_lm_label_pass)
        self.guif_lm_textEdit_pass = QtWidgets.QLineEdit(Guif_lm_main)
        self.guif_lm_textEdit_pass.setObjectName("guif_lm_textEdit_pass")
        self.horizontalLayout_2.addWidget(self.guif_lm_textEdit_pass)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.guif_lm_maingrid.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.retranslateUi(Guif_lm_main)
        QtCore.QMetaObject.connectSlotsByName(Guif_lm_main)

    def retranslateUi(self, Guif_lm_main):
        _translate = QtCore.QCoreApplication.translate
        Guif_lm_main.setWindowTitle(_translate("Guif_lm_main", "Frame"))
        self.guif_lm_title.setText(_translate("Guif_lm_main", "EduSuite"))
        self.guif_lm_label_user.setText(_translate("Guif_lm_main", "Username:"))
        self.guif_lm_label_pass.setText(_translate("Guif_lm_main", "Password:"))
