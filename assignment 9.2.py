# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Robert Ecker
# Creation Date: 10/27/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')

def chooseCave():
	#while cave != '1' and cave != '2':
    caveLoop = True #added loop and input validation check
    while caveLoop == True:
        cave = input('Which cave will you go into? (1 or 2): ')
        if cave == '1' or cave == '2':
            caveLoop = False
            return cave #corrected variable return
        else:
            print ('There are only 2 caves.')

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!') #added print function

displayIntro()
caveNumber = chooseCave()
checkCave(caveNumber)

playAgainLoop = True
while playAgainLoop == True:
	playAgain = input ('Do you want to play again? (yes or no): ')
	if playAgain == 'yes' or playAgain == 'y': #added extra validation check incase user enters 'yes'
		displayIntro()
		caveNumber = chooseCave() #fixed capitiliazation in 'choosecave'
		checkCave(caveNumber)
	elif playAgain == "no" or playAgain == 'n':
		print("Thanks for playing") #added print function
		playAgainLoop = False
	else:
		print ('Not a valid command')