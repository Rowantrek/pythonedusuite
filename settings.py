'''
	Name: settings.py
	Author: Rowan Macdonald
	Description: The Handler of global variables throughout the program
'''
#IMPORT STANDARD LIBRARY
import sys, os, random, math, time
#IMPORT PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
#IMPORT EduSuite Functions
import edufunctions
#IMPORT GUI CONTROLLER
import edugui

def init():
	global user
	user = "Guest"
	global email
	email = "Email"
	global dob
	dob = "00-00-0000"
	global maths_access
	maths_access = 0
	global comput_access
	comput_access = 0
	global hist_access
	hist_access = 0
	global maths_scores
	maths_scores = list([0,0,0,0,0,0])
	global compute_scores
	compute_scores = list([0,0,0,0,0,0])
	global hist_scores
	hist_scores = list([0,0,0,0,0,0])
	global admin_level
	admin_level = 0
	global synctime
	synctime = 120
	''' QUESTIONS '''
	global quizid
	quizid = ""
	global quiztype
	quiztype = ""
	global totalquest
	totalquest = 0
	global quizquestions
	quizquestions = []
	global quizanswers
	quizanswers = []
	global quizname
	quizname = ""
	global questionremain
	questionremain = 10
	'''
	INFO INIT
	'''
	global info_content
	info_content = {'version':'version'}
	
	info_vars = ["additsub", "multdiv", "primecomp"]
	for _i in info_vars:
		edufunctions.RDB.QueryInfoContent(_i)
	'''
	SYNC INIT
	'''