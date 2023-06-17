from colorama import Fore, Style
import colours as col

# --------------------------------------- #

words = ["Floppy", "Whiskers", "Bunny"]

# --------------------------------------- #

def puzzle():
    wordPlace = 0 
	
    while wordPlace < len(words):
        word = words[wordPlace]
        print("	≪ " + word + " ≫")
        
        userAns = input(Fore.GREEN + "\nCan you put this word in reverse?\n" + Style.RESET_ALL)
        
        if testAnswer(userAns, word):
            wordPlace += 1  
        else:
            col.red("\nOops, that's not in reverse order! Do try again!\n")

def testAnswer(userAns, word):
    reverseWord = word[::-1]
    
    if userAns.lower() == reverseWord.lower():
        print("\nCorrect! " + word + " reversed is " + reverseWord + " letters!\n")
        return True
    else:
        return False

def endGame():
	print("\n ═════════════════ ≪ °" + Fore.MAGENTA + " End of Game " + Style.RESET_ALL + "° ≫ ═════════════════ \n")
	col.cyan("Congratulations, Linguistic Bunny Adventurer!\n")

	print("""You have successfully completed all the levels of Bunny 
Linguistic Adventure, and it's time to say goodbye and 
have a lovely rest of your day! 

Hope you had fun!\n""")
	
# --------------------------------------- #

def init():
	print("\n\n ═════ ≪ °" + Fore.MAGENTA + " Level 3: Bunny Word Reversal Riddle " + Style.RESET_ALL + "° ≫ ═════ \n")

	print("""In this puzzling challenge, your task is to decipher the 
bunny word in reverse order. \n""")

	puzzle()

	endGame()


