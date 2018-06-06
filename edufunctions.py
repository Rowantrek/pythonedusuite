'''
	Name: edufunctions.py
	Author: Rowan Macdonald
	Description: The master function handler for the application.
'''
import pymysql, sys, random, math, time, PyQt5
import settings

class DB():
	def __init__(self):
		global connection
		global cursor
		connection = pymysql.connect(host='localhost',user='root',password='root',db='sdd',charset='utf8mb4')
		cursor = connection.cursor()
		
class LoginCheck():
	def init(username,password):
		DB()
		#INIT VARIALBES DEFAULTs
		userid = 0
		user = ""
		passw = ""
		email = ""
		dob = ""
		mathsaccess = 0
		comput_access = 0
		hist_acccess = 0
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
		if (username.lower() == user.lower() and password == passw):
			settings.user = user
			settings.email = email
			settings.dob = dob
			settings.maths_access = maths_access
			settings.comput_access = comput_access
			settings.hist_access = hist_access
			return True
		else:
			return False
		connection.close()
		
class RegisterCheck():
	def init(username,password,email,dob):
		#CALLING DB CONNECT
		DB()
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
		
class DBUpdate():
	def Username(oldusername,username):
		#CALL DB
		DB()
		updateRequest = "UPDATE users SET username=%s WHERE username=%s"
		cursor.execute(updateRequest, (username, oldusername))
		connection.commit()
		return True
		connection.close()
		
	def Password(oldpass, newpass):
		DB()
		username = settings.user
		query = "SELECT * FROM USERS WHERE `USERNAME`=%s"
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
		
	def Email(newemail):
		DB()
		username = settings.user
		updateRequest = "UPDATE users SET email=%s WHERE username=%s"
		cursor.execute(updateRequest, (newemail, username))
		connection.commit()
		connection.close()
		settings.email = newemail
		return True
	
	def DOB(newdob):
		DB()
		username = settings.user
		updateRequest = "UPDATE users set dob=%s WHERE username=%s"
		cursor.execute(updateRequest, (newdob, username))
		connection.commit()
		connection.close()
		settings.dob = newdob
		return True
		

	