from random import randint
# import math

# random_num=random.random()
# random_num=random.randint(0,1)

def tossIt():
	heads = 0
	tails = 0
	print 'Starting the program...'
	for i in range(1,5001):
		z=randint(0,1)
		if z < 0.5:
			y_rounded=round(z)
			z = 0
			# global tails
			tails+=1
			print "Attempt #",i,": Throwing a coin... It's a tail! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
		else:
			# global heads
			heads+=1
			print "Attempt #", i,": Throwing a coin... It's a head! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
	
	print "Ending the program, thank you!"

tossIt()

'''
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!

'''