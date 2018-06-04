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
		sql = "SELECT * FROM USERS WHERE `USERNAME`=%s"
		cursor.execute(sql, (username))
		results = cursor.fetchall()
		for row in results:
			userid = row[0]
			user = row[1]
			passw = row[2]
		if (username.lower() == user.lower() and password == passw):
			settings.name = user
			return True
		else:
			return False