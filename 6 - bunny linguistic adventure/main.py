# Imports
from colorama import Fore, Style
import level1 

print("\n ══════════ ≪ °" + Fore.MAGENTA + " Bunny Linguistic Adventure " + Style.RESET_ALL + "° ≫ ══════════ \n")

print("   __     __")
print("  /_/|   |\_\  ")
print("   |U|___|U|")
print("   |       |             " + Fore.RED + "By @xiacodes ♡" + Style.RESET_ALL)
print("   | ,   , |")
print("  (  = Y =  )")
print("   |   `   |")
print("  /|       |\\")
print(" (_|_|___|_|_)")
print("    '"
      "'   '"
      "'")

print("""
Prepare to hop into a captivating journey through the
enchanting realm of words, where fluffy bunnies and 
linguistic wonders await you! 

As a curious linguist, you possess a keen ear for the
delicate nuances of bunny language and are eager to 
unravel the secrets hidden within their furry vocabulary!""")

startGame = input(Fore.GREEN + "\nAre you ready to hop into your Bunny Linguistic Adventure?\n"+ Style.RESET_ALL)

if startGame.lower() == "yes":
	level1.level1()
else:
	print(Fore.RED + "\n>> Oh, okay, have a nice rest of your day!\n" + Style.RESET_ALL)
