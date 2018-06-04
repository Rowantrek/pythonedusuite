'''
	Name: main.py
	Author: Rowan Macdonald
	Description: Main python file for EduSuite Application
'''
#IMPORT STANDARD LIBRARY
import sys, os, random, math, time
#IMPORT PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
#IMPORT EduSuite Functions
import edufunctions
#IMPORT GUI CONTROLLER
import edugui
#IMPORT MAIN SETTINGS
import settings

if __name__ == "__main__":
	settings.init()
	edugui.UI_MAIN.InitWindow()
