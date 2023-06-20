
import colours as c
import generate as gen
import os
from time import sleep

def init():
	intro = c.rt + """
████████╗██████╗░██╗░██████╗░██╗░░░██╗███╗░░██╗
╚══██╔══╝██╔══██╗██║██╔════╝░██║░░░██║████╗░██║
░░░██║░░░██████╔╝██║██║░░██╗░██║░░░██║██╔██╗██║
░░░██║░░░██╔══██╗██║██║░░╚██╗██║░░░██║██║╚████║
░░░██║░░░██║░░██║██║╚██████╔╝╚██████╔╝██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚══╝
""" + c.rs

	intro = intro + c.bs + "\nHello and welcome to the Trigun Quote Generator! \n" + c.rs
	intro = intro + """\nI had finished the anime TV series 'Trigun (1998)
and thought why not share some amazing quotes
from the show!"""

	print(intro)

	print("\n»» ———————————————————　★　——————————————————— «« \n")

	print("""Pick from one of the four main characters or pick
'any' to get a random quote!\n""")

	characters = ['Vash The Stampede', 'Nicholas D. Wolfwood', 'Meryl Stryfe', 'Millie Thompson', 'Any']

	for i, char in enumerate(characters, start=1):
		print("	" + c.bs + str(i) + ") " + c.rs + char + "\n")
	
	userAns = input(c.rt + "Chosen option number: " + c.rs)
	userAns = int(userAns)

	if userAns <= 5:
		sleep(1)
		gen.ansToChar(userAns, characters)
	else:
		print(c.ct + "That number is not part of the option list. Try again." + c.rs)
		sleep(1)
		os.system('clear')
		init()
	
	print("\n»» ———————————————————　★　——————————————————— «« \n")

	playAgain = input(c.rt + "Would you want another quote? " + c.rs).lower()

	if playAgain == "yes":
		sleep(1)
		os.system('clear')
		init()
	elif playAgain == "no":
		print("\nHave a nice rest of our day then! And remember:\n\n>> Love and Peace! <<")
	else:
		print("\nI'll assume no then... Have a nice rest of our day then! And remember:\n\n>> Love and Peace! <<")

	

init()

print("\n»» ———————————————————　★　——————————————————— «« \n")