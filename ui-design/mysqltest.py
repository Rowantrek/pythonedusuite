import pymysql, sys, random, math, time, PyQt5


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
			user = user
			email = email
			dob = dob
			maths_access = maths_access
			comput_access = comput_access
			hist_access = hist_access
			maths_scores = maths_scores
			compute_scores = compute_scores
			hist_scores = hist_scores
			admin_level = int(admin_level)
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
		user = username
		
	def UpdatePassword(oldpass, newpass):
		RDB.Connect()
		username = user
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
		username = user
		updateRequest = "UPDATE users SET email=%s WHERE username=%s"
		cursor.execute(updateRequest, (newemail, username))
		connection.commit()
		connection.close()
		email = newemail
		return True
	
	def UpdateDOB(newdob):
		RDB.Connect()
		username = user
		updateRequest = "UPDATE users set dob=%s WHERE username=%s"
		cursor.execute(updateRequest, (newdob, username))
		connection.commit()
		connection.close()
		dob = newdob
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
		info_content[info_name] = info_content
		connection.close()
		
	def QueryScores():
		RDB.Connect()
		username = user
		maths_scores = maths_scores
		compute_scores = compute_scores
		hist_scores = hist_scores
		scoreQuery = "SELECT * FROM USERS WHERE username = %s"
		cursor.execute(scoreQuery, (username))
		results = cursor.fetchall()
		for row in results:
			maths_scores = row[8]
			compute_scores = row[9]
			hist_scores = row[10]
		connection.close()
	
	def UpdateScores():
		math = maths_scores
		compute = compute_scores
		hist = hist_scores
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
			quizid = row[0]
			quiztype = row[1]
			totalquest = row[2]
			
		if (quiztype == "normal"):
			for row in results:
				questions = list(row[3])
				answers = row[4]
				print(questions)
			for _i in questions:
				quizquestions[que] = _i
				que += 1
			for _i in answers:
				quizanswers[ans] = _i
				ans += 1
		if (quiztype == "multi"):
			for row in results:
				questions = row[3]
				answers = row[4]
				options = list(row[5])
			for _i in questions:
				quizquestion[que] = _i
				que += 1
	
	def Sync():
		RDB.Connect()
		
quizquestions = {}
quizanswers = {}

quiz1 = "maths1_1"
RDB.GetQuestions(quiz1)

myq = [1,2,3,4,5,6,7,8,9,10]

q = random.sample(myq, 1)

print(quizquestions)
myqs = ["HJELLO","HELLO2","QUESTION3","QUESTION4"]
quizid2 = "maths1_1"

RDB.Connect()
sql = "UPDATE quiz SET questions=%s WHERE quizid=%s"
cursor.execute(sql, (myqs, quizid2))
connection.commit()


