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
	'''
	USER MANAGEMENT VARIABLES
	'''
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
	'''
	QUIZ RELATED VARIABLES
	'''
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
	global score
	score = 0
	global questnum
	questnum = 0
	global totalanswered
	totalanswered = 0
	'''
	INFORMATION VARIABLES
	'''
	global activeinfo
	activeinfo = {"maths1": 0, "maths2":0, "maths3":0, "maths4":0, "maths5":0, "maths6":0, "compute1":0,"compute2":0,"compute3":0,"compute4":0,"compute5":0,"compute6":0,"hist1":0,"hist2":0,"hist3":0,"hist4":0,"hist5":0,"hist6":0}
	global infoimg
	infoimg = {}
	global info_content
	info_content = {'version':'version'}
	global infotype
	infotype = {}
	'''
	QUIZ QUERY
	'''
	global quizactive
	quizactive = {}
	

	'''
	SYNC INIT
	'''