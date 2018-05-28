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
from ui.gui import Ui_guif_main
gui = ""

class MenuHandler(object):
	def InitGUI():
		global mm_main
		app = QtWidgets.QApplication(sys.argv)
		mm_main = QtWidgets.QMainWindow()
		ui = Ui_guif_main()
		ui.setupUi(mm_main)
		mm_main.showMaximized()
		sys.exit(app.exec_())
	def LoginMenu():
		pass
	def RegisterMenu():
		pass

		

