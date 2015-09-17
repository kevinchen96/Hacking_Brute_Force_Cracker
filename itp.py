#Kevin Chen
#Brute Force Password Cracking
#Run the script with the imports hashlib and time, and the included text file test.txt in the same directory
#Extra Credit Attempt: Faster Cracked times

import hashlib
import time

#Crack Password by calling Recurse function
#Updates max size of password by 1 if Recurse function on size doesn't work
#For ex, Recurse size 1 is all characters, size 2 is all permutations of length 2, etc.
def crackPassword(size, mhash, stime):
	check = False
	while(check == False):
		check = recurse(size, 0, mhash, "", stime)
		size += 1

#Recurse recursively checks through all options by changing a single letter at a time for a given length
def recurse(size, position, mhash, answer, stime):
	for index in range(33, 127):
		if position < size - 1:
			check = recurse(size, position + 1, mhash, answer + chr(index), stime)  
			if check == True:
				return True
		elif hashlib.md5(answer + chr(index)).hexdigest() == mhash:
			print "Password is: " + answer + chr(index)
			print "Cracked in " + str(time.time() - start_time) + " seconds"
			return True
	return False

#Main program
#Reads in file and calls on crackPassword
f = open("test.txt", "r" )
temp = f.read().splitlines()
for line in temp:
	answer = ""
	print "Trying to crack " + line
	start_time = time.time()
	crackPassword(1, line, start_time)
	print ""
