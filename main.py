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

if __name__ == "__main__":
	edugui.MenuHandler.InitGUI()
	edugui.MenuHandler.MainMenu()
