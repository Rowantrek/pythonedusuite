'''
	Name: edufunctions.py
	Author: Rowan Macdonald
	Description: The master function handler for the application.
'''
import pymysql, sys, random, math, time
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtWebKitWidgets
import settings
import threading

''' TODO: MERGE ALL DB INTO ONE SINGLE CLASS '''

''' RDB - Rowan's Database Interface - Deals with any communication between the app & MySQL'''
class RDB():
	def Connect():
		global connection
		global cursor
		connection = pymysql.connect(host='45.76.121.220',user='software',password='software',db='sdd',charset='utf8mb4')
		cursor = connection.cursor()
	def CloseConn():
		connection.close()
	def Login(username,password):
		RDB.Connect()
		#INIT VARIALBES DEFAULTs
		userid = 0
		user = ""
		passw = ""
		email = ""
		dob = ""
		mathsaccess = 0
		comput_access = 0
		hist_acccess = 0
		maths_scores = [0,0,0,0,0,0]
		compute_scores = [0,0,0,0,0,0]
		hist_scores = [0,0,0,0,0,0]
		admin_level = 0
		sql = "SELECT * FROM users WHERE `username`=%s"
		cursor.execute(sql, (username))
		results = cursor.fetchall()
		for row in results:
			userid = row[0]
			user = row[1]
			passw = row[2]
			email = row[3]
			dob = row[4]
			maths_access = row[5]
			comput_access = row[6]
			hist_access = row[7]
			maths_scores = row[8]
			compute_scores = row[9]
			hist_scores = row [10]
			admin_level = row[11]
		if (username.lower() == user.lower() and password == passw):
			settings.user = user
			settings.email = email
			settings.dob = dob
			settings.maths_access = maths_access
			settings.comput_access = comput_access
			settings.hist_access = hist_access
			settings.maths_scores = maths_scores
			settings.compute_scores = compute_scores
			settings.hist_scores = hist_scores
			settings.admin_level = int(admin_level)
			return True
		else:
			return False
		
	def Register(username,password,email,dob):
		#CALLING DB CONNECT
		RDB.Connect()
		insertRequest = "INSERT INTO `users` (`username`, `password`, `email`, `dob`) VALUES (%s, %s, %s, %s)"
		cursor.execute(insertRequest, (username, password, email, dob))
		connection.commit()
		sql = "SELECT * FROM users WHERE `username`=%s"
		cursor.execute(sql, (username))
		results = cursor.fetchall()
		for row in results:
			userid = row[0]
			user = row[1]
			passw = row[2]
		if (username.lower() == user.lower()):
			return True
		else:
			return False
		
	def UpdateUser(oldusername,username):
		#CALL DB
		RDB.Connect()
		updateRequest = "UPDATE users SET username=%s WHERE username=%s"
		cursor.execute(updateRequest, (username, oldusername))
		connection.commit()
		return True
		
		settings.user = username
		
	def UpdatePassword(oldpass, newpass):
		RDB.Connect()
		username = settings.user
		passw = ""
		query = "SELECT * FROM users WHERE username=%s"
		cursor.execute(query, (username))
		results = cursor.fetchall()
		for row in results:
			user = row[1]
			passw = row[2]
		if (oldpass == passw):
			updateRequest = "UPDATE users SET password=%s WHERE username = %s"
			cursor.execute(updateRequest, (newpass, username))
			connection.commit()
			return True
		else:
			return False
		
		
	def UpdateEmail(newemail):
		RDB.Connect()
		username = settings.user
		updateRequest = "UPDATE users SET email=%s WHERE username=%s"
		cursor.execute(updateRequest, (newemail, username))
		connection.commit()
		
		settings.email = newemail
		return True
	
	def UpdateDOB(newdob):
		RDB.Connect()
		username = settings.user
		updateRequest = "UPDATE users set dob=%s WHERE username=%s"
		cursor.execute(updateRequest, (newdob, username))
		connection.commit()
		
		settings.dob = newdob
		return True
	
	def QueryInfoContent(content_id):
		RDB.Connect()
		#Define variables to ensure error is not given if DB does not find anything
		info_name = ""
		info_content = ""
		contentQuery = "SELECT * FROM info WHERE idinfo = %s"
		cursor.execute(contentQuery, (content_id))
		results = cursor.fetchall()
		for row in results:
			info_name = row[2]
			info_content = row[3]
			infotype = row[1]
		
		return info_name, info_content, infotype				
				
	def QuizImages(quiz):
		RDB.Connect()
		query = "SELECT * FROM quiz WHERE quizid = %s"
		cursor.execute(query, (quiz))
		results = cursor.fetchall()
		for row in results:
			ret = row[10]
		return ret
	
	def CatImages(menu):
		RDB.Connect()
		query = "SELECT * FROM info WHERE idinfo = %s"
		cursor.execute(query, (menu))
		results = cursor.fetchall()
		for row in results:
			image = row[4]
		return image

		
	
	def QueryScores():
		RDB.Connect()
		username = settings.user
		maths_scores = settings.maths_scores
		compute_scores = settings.compute_scores
		hist_scores = settings.hist_scores
		scoreQuery = "SELECT * FROM users WHERE username = %s"
		cursor.execute(scoreQuery, (username))
		results = cursor.fetchall()
		for row in results:
			settings.maths_scores = row[8]
			settings.compute_scores = row[9]
			settings.hist_scores = row[10]
		
		settings.maths_scores = settings.maths_scores.split(",")
		settings.compute_scores = settings.compute_scores.split(",")
		settings.hist_scores = settings.hist_scores.split(",")
	
	def UpdateScores():
		math = settings.maths_scores
		compute = settings.compute_scores
		hist = settings.hist_scores
		RDB.Connect()
		
		
	
	def GetQuestions(quiz):
		RDB.Connect()
		quizQuery = "SELECT * FROM quiz WHERE quizid = %s"
		cursor.execute(quizQuery, (quiz))
		results = cursor.fetchall()
		for row in results:
			settings.quizid = row[0]
			settings.quiztype = row[2]
			settings.totalquest = row[3]
			settings.quizname = row[1]
			
		if (settings.quiztype == "normal"):
			for row in results:
				questions = row[4]
				answers = row[9]
			settings.quizquestions = questions.split(",")
			settings.quizanswers = answers.split(",")
		elif (settings.quiztype == "choice"):
			for row in results:
				questions = row[4]
				answers = row[9]
				choicea = row[5]
				choiceb = row[6]
				choicec = row[7]
				choiced = row[8]

			settings.quizquestions = questions.split(",")
			settings.quizanswers = answers.split(",")
			settings.choices = {}
			settings.choices["A"] = choicea.split(",")
			settings.choices["B"] = choiceb.split(",")
			settings.choices["C"] = choicec.split(",")
			settings.choices["D"] = choiced.split(",")
	
	def Sync():
		RDB.Connect()
		
class QuizHandler():
	def InitQuiz(quizname):
		#CHECK WHAT quiz SO WE CAN LOAD THE STUFF
		quizname = quizname
		settings.quizid = ""
		settings.quiztype = ""
		settings.totalquest = 0
		settings.score = 0
		settings.quizquestions = []
		settings.quizanswers = []
		settings.totalanswered = 0
		settings.questnum = 0
		FirstQuestion = True
		RDB.GetQuestions(quizname)
		settings.questionremain = settings.totalquest
		#return FirstQuestion
		
	def GetFinish():
		finished = False
		if (settings.questionremain == 0):
			finished = True
		return finished
		
	def Question():
		finished = False
		question = ""
		#settings.questnum = random.randrange(-1, settings.questionremain)
		if (settings.quiztype == "normal"):
			quiztype = "normal"
			choice_a = ""
			choice_b = ""
			choice_c = ""
			choice_d = ""
			question = settings.quizquestions[settings.questnum]
		elif (settings.quiztype == "choice"):
			quiztype = "choice"
			question = settings.quizquestions[settings.questnum]
			choice_a = settings.choices["A"][settings.questnum]
			choice_b = settings.choices["B"][settings.questnum]
			choice_c = settings.choices["C"][settings.questnum]
			choice_d = settings.choices["D"][settings.questnum]
		return question, choice_a, choice_b, choice_c, choice_d
		
	def ShortAnswer(ansinput):
		correctanswer = settings.quizanswers[settings.questnum]
		ansinput = ansinput
		#CHECK TYPE OF quiz
		if (settings.quiztype == "normal"):
			if (str(ansinput) == str(correctanswer)):
				correct = True
				settings.score += 1
			else:
				correct = False
		else:
			correct = False
		
		settings.questionremain -= 1
		settings.totalanswered += 1
		settings.questnum = settings.questnum + 1
		return correct
	
	def MultiAnswer(multianswer):
		correctanswer = settings.quizanswers[settings.questnum]
		if (str(multianswer) == str(correctanswer)):
			correct = True
			settings.score +=1
		else:
			correct = False
			
		settings.questionremain -= 1
		settings.totalanswered += 1
		settings.questnum = settings.questnum + 1
		return correct

	def Finished():
		score = settings.score
		maxscore = settings.totalquest
		return score,maxscore
		

class gui():
	def subcatmenu(menu):
		info_name = ""
		info_content = ""
		infotype = ""
		#RETRIEVES DATA FROM THE DB
		info_name, info_content, infotype = RDB.QueryInfoContent(menu)
		#7 - GET IMAGES FOR THING, DEFINES IMAGES IN DICTIONARY
		quizimages = {"one":"","two":"","three":""}
		quizimages["one"] = RDB.QuizImages(menu + "_1")
		quizimages["two"] = RDB.QuizImages(menu + "_2")
		quizimages["three"] = RDB.QuizImages(menu + "_3")
		
		return info_name, info_content, infotype, quizimages
	
	def catmenu(menu):
		#CONTROL FLOW TO DETERMINE CAT_TITLE
		if (menu == "maths"):
			cat_title = "Mathematics"
		elif (menu == "compute"):
			cat_title = "Computing"
		elif (menu == "hist"):
			cat_title = "History"
		else:
			cat_title = "ERROR RETREIVING DATA"
		#PROCESS FOR GETTING info_IMAGES
		info_images = {"one":"","two":"","three":""}
		info_images["one"] = RDB.CatImages(menu + "1")
		info_images["two"] = RDB.CatImages(menu + "2")
		info_images["three"] = RDB.CatImages(menu + "3")
		
		return cat_title, info_images
		
		
	
		
		