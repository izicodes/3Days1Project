from colorama import Fore, Style
import colours as col
import level3 as lvl3

# --------------------------------------- #

words = ["Cottontail", "Thump", "Fluffy"]

# --------------------------------------- #

def puzzle():
    wordPlace = 0 
	
    while wordPlace < len(words):
        word = words[wordPlace]
        print("	≪ " + word + " ≫")
        
        userAns = input(Fore.GREEN + "\nCan you count the characters?\n" + Style.RESET_ALL)
        
        if testAnswer(userAns, word):
            wordPlace += 1  
        else:
            col.red("\nOops, that's not the correct number! Tricky, I know! Try again!\n")

def testAnswer(userAns, word):
    numberOfChars = len(word)
    userAns = int(userAns)
    
    if userAns == numberOfChars:
        print("\nCorrect! " + word + " has " + str(numberOfChars) + " letters!\n")
        return True
    else:
        return False

# --------------------------------------- #

def init():
	print("\n\n ═════ ≪ °" + Fore.MAGENTA + " Level 2: Bunny Character Count Quest " + Style.RESET_ALL + "° ≫ ═════ \n")

	print("""In this challenge, you will need to determine the number 
of characters in the mystery bunny words. Bunnies come in all shapes 
and sizes, and so do words!\n""")

	puzzle()

	lvl3.init()
	