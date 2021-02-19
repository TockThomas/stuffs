import zipfile
import itertools
import string
from threading import Thread
import traceback

print('Cracking...')

def crack(zip, pwd):
	try:
		zip.extractall(pwd=str.encode(pwd))
		print('Success: Password is: ' + pwd)
	except:
		pass

zipFile = zipfile.ZipFile("\crack2.zip")
myLetters = string.ascii_letters + string.digits + string.punctuation
for i in range(3,10):
	for j in map(''.join, itertools.product(myLetters, repeat=i)):
		t = Thread(target=crack, args=(zipFile, j))
		t.start()
