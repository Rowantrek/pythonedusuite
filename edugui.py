'''
	Name: edugui.py
	Author: Rowan Macdonald
	Description: The Master GUI Handler for the application
'''
#IMPORT STANDARD LIBRARY
import sys, os, random, math, time
#IMPORT PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#IMPORT EduSuite Functions
import edufunctions
#IMPORT MAIN GUI
from ui.gui import Ui_guif_main, MainGUI

class InitWindow():
	def __init__(self):
		global guif_main
		global guif_maingrid
		global app
		app = QtWidgets.QApplication(sys.argv)
		#WINDOW INIT
		guif_main = QtWidgets.QMainWindow()
		guif_main.setObjectName("guif_main")
		guif_main.resize(900, 700)
		guif_main.setWindowOpacity(1.0)
		_translate = QtCore.QCoreApplication.translate
		guif_main.setWindowTitle(_translate("guif_main", "EduSuite"))
		#MAINGRID INIT
		guif_maingrid = QtWidgets.QWidget(guif_main)
		guif_maingrid.setObjectName("guif_maingrid")
		
		guif_main.setCentralWidget(guif_maingrid)
		

		
class WidgetTele():
	def MainMenu():
		Ui_MainMenu()
		guif_main.showMaximized()
		sys.exit(app.exec_())

	
class Ui_MainMenu():
	def __init__(self):
		self.guif_mm_place = QtWidgets.QWidget()
		self.guif_mm_place.setObjectName("guif_mm_place")
		
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("guif_mm_layout")
		#MAIN WIDGET CONTAINER
		self.guif_mm_main = QtWidgets.QWidget(self.guif_mm_place)
		self.guif_mm_main.setObjectName("guif_mm_main")
		#GRID CONTAINER 3
		self.gridLayout_3 = QtWidgets.QGridLayout(self.guif_mm_main)
		self.gridLayout_3.setObjectName("guif_mm_layout3")
		self.gridLayout_3.setContentsMargins(0,0,0,0)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
		#SECONDARY GRID [CONTAINS LOGO AND BUTTONS]
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
		self.guif_mm_Hlayout_btn = QtWidgets.QHBoxLayout()
		self.guif_mm_Hlayout_btn.setObjectName("guif_mm_Hlayout_btn")
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.guif_mm_Hlayout_btn.addItem(spacerItem2)
		self.guif_mm_btn_login = QtWidgets.QPushButton(self.guif_mm_main)
		self.guif_mm_btn_login.setEnabled(True)
		font = QtGui.QFont()
		font.setPointSize(20)
		self.guif_mm_btn_login.setFont(font)
		self.guif_mm_btn_login.setObjectName("guif_mm_btn_login")
		self.guif_mm_Hlayout_btn.addWidget(self.guif_mm_btn_login)
		spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		self.guif_mm_Hlayout_btn.addItem(spacerItem3)
		self.guif_mm_btn_reg = QtWidgets.QPushButton(self.guif_mm_main)
		font = QtGui.QFont()
		font.setPointSize(20)
		self.guif_mm_btn_reg.setFont(font)
		self.guif_mm_btn_reg.setObjectName("guif_mm_btn_reg")
		self.guif_mm_Hlayout_btn.addWidget(self.guif_mm_btn_reg)
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.guif_mm_Hlayout_btn.addItem(spacerItem4)
		#ADDS LAYOUTS TO MAIN LAYERS
		self.guif_mm_grid_secondary.addLayout(self.guif_mm_Hlayout_btn, 2, 0, 1, 1)
		self.gridLayout_3.addLayout(self.guif_mm_grid_secondary, 1, 0, 1, 1)
		spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
		_translate = QtCore.QCoreApplication.translate
		self.guif_mm_title.setText(_translate("guif_main", "EduSuite"))
		self.guif_mm_btn_login.setText(_translate("guif_main", "  Login  "))
		self.guif_mm_btn_reg.setText(_translate("guif_main", "Register"))
		guif_maingrid.addWidget(self.guif_mm_place, 0, 0, 1, 1)
