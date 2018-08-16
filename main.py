import MySQLdb
import sys
import student


def insert(student):
		input_sql = "INSERT INTO Student(name, email, score) VALUES ('{}', '{}', {});".format(student.name, student.email, student.score)
		print(student.name, "is now added into Student.")
		cursor.execute(input_sql)

def delete(name):
	cursor.execute("SELECT name FROM Student")
	students = [row[0] for row in cursor.fetchall()]  #fetchall() format: ((student1-col1,col2,...), (student2-col1,col2,...), ....)
	if name in students:
		input_sql = "DELETE FROM Student WHERE name = '{}'".format(name)
		cursor.execute(input_sql)
		print(name, "is now deleted from Student.")
	else:
		print("Student", name, "doesn't exist.")

def list():
	cursor.execute("SELECT name FROM Student")
	students = [row[0] for row in cursor.fetchall()]  #fetchall() format: ((student1-col1,col2,...), (student2-col1,col2,...), ....)
	students.sort()
	print(students)

def list_contains(name):
	cursor.execute("SELECT name FROM Student")
	students = [row[0] for row in cursor.fetchall()]  #fetchall() format: ((student1-col1,col2,...), (student2-col1,col2,...), ....)
	students.sort()
	match = [stu for stu in students if contain_component in stu]
	print(match)



if __name__ == '__main__':

	db = MySQLdb.connect(host="localhost", user="Patina", passwd="1234", db="MyClass")
	cursor = db.cursor()

	argv = sys.argv
	command = argv[1]

	if (command == 'insert'):
		if(len(argv) == 5):
			student_obj = student.student(argv[2], argv[3], argv[4])
			insert(student_obj)
		elif(len(argv) < 5):
			print("Some parameter required might be missing, please check.")
		else:
			print("There might be redundant parameter, please check.")

	elif (command == 'delete'):
		if(len(argv) == 3):
			name = argv[2]
			delete(name)
		elif(len(argv) < 3):
			print("Some parameter required might be missing, please check.")
		else:
			print("There might be redundant parameter, please check.")

	elif (command == 'list'):
		if (len(argv) == 2):
			list()
		elif (len(argv) == 3):
			name = argv[2]
			list_contains()
		elif(len(argv) < 2):
			print("Some parameter required might be missing, please check.")
		elif(len(argv) > 3):
			print("There might be redundant parameter, please check.")


	db.commit()
