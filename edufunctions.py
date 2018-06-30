'''
	Name: edufunctions.py
	Author: Rowan Macdonald
	Description: The master function handler for the application.
'''
import pymysql, sys, random, math, time
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtWebKitWidgets
import settings

''' TODO: MERGE ALL DB INTO ONE SINGLE CLASS '''

''' RDB - Rowan's Database Interface - Deals with any communication between the app & MySQL'''
class RDB():
	def Connect():
		global connection
		global cursor
		connection = pymysql.connect(host='localhost',user='root',password='root',db='sdd',charset='utf8mb4')
		cursor = connection.cursor()
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
		sql = "SELECT * FROM USERS WHERE `USERNAME`=%s"
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
		connection.close()
	def Register(username,password,email,dob):
		#CALLING DB CONNECT
		RDB.Connect()
		insertRequest = "INSERT INTO `users` (`username`, `password`, `email`, `dob`) VALUES (%s, %s, %s, %s)"
		cursor.execute(insertRequest, (username, password, email, dob))
		connection.commit()
		sql = "SELECT * FROM USERS WHERE `USERNAME`=%s"
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
		connection.close()
	def UpdateUser(oldusername,username):
		#CALL DB
		RDB.Connect()
		updateRequest = "UPDATE users SET username=%s WHERE username=%s"
		cursor.execute(updateRequest, (username, oldusername))
		connection.commit()
		return True
		connection.close()
		settings.user = username
		
	def UpdatePassword(oldpass, newpass):
		RDB.Connect()
		username = settings.user
		passw = ""
		query = "SELECT * FROM USERS WHERE USERNAME=%s"
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
		connection.close()
		
	def UpdateEmail(newemail):
		RDB.Connect()
		username = settings.user
		updateRequest = "UPDATE users SET email=%s WHERE username=%s"
		cursor.execute(updateRequest, (newemail, username))
		connection.commit()
		connection.close()
		settings.email = newemail
		return True
	
	def UpdateDOB(newdob):
		RDB.Connect()
		username = settings.user
		updateRequest = "UPDATE users set dob=%s WHERE username=%s"
		cursor.execute(updateRequest, (newdob, username))
		connection.commit()
		connection.close()
		settings.dob = newdob
		return True
	def QueryInfoContent(content_id):
		RDB.Connect()
		#Define variables to ensure error is not given if DB does not find anything
		info_name = ""
		info_content = ""
		contentQuery = "SELECT * FROM INFO WHERE info_name = %s"
		cursor.execute(contentQuery, (content_id))
		results = cursor.fetchall()
		for row in results:
			info_name = row[1]
			info_content = row[2]
		settings.info_content[info_name] = info_content
		connection.close()
		
	def QueryScores():
		RDB.Connect()
		username = settings.user
		maths_scores = settings.maths_scores
		compute_scores = settings.compute_scores
		hist_scores = settings.hist_scores
		scoreQuery = "SELECT * FROM USERS WHERE username = %s"
		cursor.execute(scoreQuery, (username))
		results = cursor.fetchall()
		for row in results:
			settings.maths_scores = row[8]
			settings.compute_scores = row[9]
			settings.hist_scores = row[10]
		connection.close()
	
	def UpdateScores():
		math = settings.maths_scores
		compute = settings.compute_scores
		hist = settings.hist_scores
		RDB.Connect()
		
		connection.close()
	
	def GetQuestions(quiz):
		que = 1
		ans = 1
		RDB.Connect()
		quizQuery = "SELECT * FROM QUIZ WHERE quizid = %s"
		cursor.execute(quizQuery, (quiz))
		results = cursor.fetchall()
		for row in results:
			settings.quizid = row[0]
			settings.quiztype = row[1]
			settings.totalquest = row[2]
			
		if (settings.quiztype == "normal"):
			for row in results:
				questions = row[3]
				answers = row[4]
				quizname = row[5]
			settings.quizquestions = questions.split(",")
			settings.quizanswers = answers.split(",")
			settings.quizname = quizname
		if (settings.quiztype == "multi"):
			pass
	
	def Sync():
		RDB.Connect()
		
	