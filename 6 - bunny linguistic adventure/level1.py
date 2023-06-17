from colorama import Fore, Style
import colours as col
import level2 as lvl2

# --------------------------------------- #
	
fullPuzzle = """R E H A F
E G A H T
R H N E S
A E R A T
H T R U T
"""

def puzzle():
	print(fullPuzzle)

	userAns = input(Fore.GREEN + "What is the hidden word?" + Fore.RED + " Type 'help' if you need a hint!\n" + Style.RESET_ALL)

	testAnswer(userAns)

def testAnswer(userAns):
	if (userAns.upper() == "HARE"):
		print("\nCorrect! The hidden word is " + Fore.GREEN + userAns.upper() + Style.RESET_ALL)
		lvl2.init()
	elif userAns.lower() == "help":
		col.red("\n> Ooo, a hint! Okay, it begins with a 'h'! Good luck!\n")
		puzzle()
	else:
		col.red("\nOops, that's not the hidden word! Tricky, I know! Try again!\n")
		puzzle()

# --------------------------------------- #

def level1():
	print("\n\n ══════ ≪ °" + Fore.MAGENTA + " Level 1: Bunny Uppercase Challenge " + Style.RESET_ALL + "° ≫ ══════ \n")

	print("""Prepare to test your linguistic skills by uppercasing the 
hidden bunny word. Bunnies love to hop around and catch
our attention, so let's give this word the recognition it 
deserves!\n""")

	puzzle()

	




