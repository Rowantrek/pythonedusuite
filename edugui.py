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

class MenuHandler(object):
	def InitGUI():
		MainGUI.init()
	def MainMenu():
		pass
	def LoginMenu():
		pass
	def RegisterMenu():
		pass

		

