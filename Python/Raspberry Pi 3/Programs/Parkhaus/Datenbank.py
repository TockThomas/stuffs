import sqlite3

connection = sqlite3.connect("Test.db")
try:
	cursor = connection.cursor()
	cursor.execute("""CREATE TABLE test (
		AutoID INTEGER, Eingangszeit INTEGER, Ausgangszeit INTEGER)""")
	cursor.execute("""INSERTINTO test VALUES (
		'1', '14:10', '15:00')""")
except:
	print("Ein Problem trat auf -> Rollback")
	connection.rollback()