#IMPORT STANDARD LIBRARY
import sys, os, random, math, time
#IMPORT PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#IMPORT EduSuite Functions
import edufunctions, edugui

class MainMenuCall():
	def __init__(self):
		from ui.mainmenu import Ui_mm_main
		super().__init__()
		app = QtWidgets.QApplication(sys.argv)
		mm_main = QtWidgets.QMainWindow()
		ui = Ui_mm_main()
		ui.setupUi(mm_main)
		mm_main.showMaximized()
		sys.exit(app.exec_())

class LoginMenuCall():
	def __init__(self):
		from ui.loginmenu import Ui_mm_login_menu
		super().__init__()
		app = QtWidgets.QApplication(sys.argv)
		mm_login_menu = QtWidgets.QMainWindow()
		ui = Ui_mm_login_menu
		ui.setupUi(mm_login_menu)
		mm_login_menu.showMaximized()
		sys.exit(app.exec_())