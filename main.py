import MySQLdb
import sys
import inspect
from student import student
from student import teacher
from student import stu_group


def insert(input_obj):
	if isinstance(input_obj, student):
		input_sql = "INSERT INTO Student(name, score, class_id) VALUES ('{}', {}, {});".format(input_obj.name, input_obj.score, input_obj.class_id)
		print(input_obj.name, "is now added into list.")
	elif isinstance(input_obj, teacher):
		input_sql = "INSERT INTO Teacher(name, age, class_id) VALUES ('{}', {}, {});".format(input_obj.name, input_obj.age, input_obj.class_id)
		print(input_obj.name, "is now added into list.")
	elif isinstance(input_obj, stu_group):
		input_sql = "INSERT INTO Class(name, grade) VALUES ('{}', '{}');".format(input_obj.name, input_obj.grade)
		print(input_obj.name, "is now added into list.")
	cursor.execute(input_sql)

def delete(table, name):
	if (table == 'student'):
		sql = "SELECT name FROM Student"
	elif (table == 'teacher'):
		sql = "SELECT name FROM Teacher"
	elif (table == 'class'):
		sql = "SELECT name FROM Class"
	cursor.execute(sql)
	name_list = [row[0] for row in cursor.fetchall()]  #fetchall() format: ((student1-col1,col2,...), (student2-col1,col2,...), ....)
	if name in name_list:
		if (table == 'student'):
			sql = "DELETE FROM Student WHERE name = '{}'".format(name)
		elif (table == 'teacher'):
			sql = "DELETE FROM Teacher WHERE name = '{}'".format(name)
		elif (table == 'class'):
			sql = "DELETE FROM Class WHERE name = '{}'".format(name)

		cursor.execute(sql)
		print(name, "is now deleted from", table)
	else:
		print(name, "doesn't exist in", table)

def list(table):
	if (table == 'student'):
		sql = "SELECT name FROM Student"
	elif (table == 'teacher'):
		sql = "SELECT name FROM Teacher"
	elif (table == 'class'):
		sql = "SELECT name FROM Class"
	cursor.execute(sql)
	name_list = [row[0] for row in cursor.fetchall()]  #fetchall() format: ((student1-col1,col2,...), (student2-col1,col2,...), ....)
	name_list.sort()
	print(name_list)

def list_contains(table, contain_component):
	if (table == 'student'):
		sql = "SELECT name FROM Student"
	elif (table == 'teacher'):
		sql = "SELECT name FROM Teacher"
	elif (table == 'class'):
		sql = "SELECT name FROM Class"
	cursor.execute(sql)
	name_list = [row[0] for row in cursor.fetchall()]  #fetchall() format: ((student1-col1,col2,...), (student2-col1,col2,...), ....)
	name_list.sort()
	match = [_ for _ in name_list if contain_component in _]
	print(match)



if __name__ == '__main__':

	db = MySQLdb.connect(host="localhost", user="Patina", passwd="1234", db="MyClass")
	cursor = db.cursor()

	argv = sys.argv
	table = argv[1]
	command = argv[2]

	if (command == 'insert'):
		if(table == 'student' and len(argv) == 6):
			input_obj = student(argv[3], argv[4], argv[5])
			insert(input_obj)
		elif(table == 'teacher' and len(argv) == 6):
			input_obj = teacher(argv[3], argv[4], argv[5])
			insert(input_obj)
		elif(table == 'class' and len(argv) == 5):
			input_obj = stu_group(argv[3], argv[4])
			insert(input_obj)
		elif(((table == 'student' or table == 'teacher') and len(argv) < 6) or (table == 'class' and len(argv) < 5)):
			print("Some parameter required might be missing, please check.")
		else:
			print("There might be redundant parameter, please check.")

	elif (command == 'delete'):
		if(len(argv) == 4):
			name = argv[3]
			delete(table, name)
		elif(len(argv) < 4):
			print("Some parameter required might be missing, please check.")
		else:
			print("There might be redundant parameter, please check.")

	elif (command == 'list'):
		if (len(argv) == 3):
			list(table)
		elif (len(argv) == 4):
			contain_component = argv[3]
			list_contains(table, contain_component)
		elif(len(argv) < 3):
			print("Some parameter required might be missing, please check.")
		elif(len(argv) > 4):
			print("There might be redundant parameter, please check.")


	db.commit()
