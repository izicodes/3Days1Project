import questions
from colorama import Fore, Style

print(" ⠀⠀⠀⢠⡾⠲⠶⣤⣀⣠⣤⣤⣤⡿⠛⠿⡴⠾⠛⢻⡆⠀⠀⠀")
print(" ⠀⠀⠀⣼⠁⠀⠀⠀⠉⠁⠀⢀⣿⠐⡿⣿⠿⣶⣤⣤⣷⡀⠀⠀   Welcome to the")
print(" ⠀⠀⠀⢹⡶⠀⠀⠀⠀⠀⠀⠈⢯⣡⣿⣿⣀⣰⣿⣦⢂⡏⠀⠀  Hello Kitty Quiz")
print("⠀⠀ ⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠹⣍⣭⣾⠁⠀⠀")
print("⠀ ⣀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣧⣤⡀    By @xiacodes")
print(" ⠈⠉⠹⣏⡁⠀⢸⣿⠀⠀⠀⢀⡀⠀⠀⠀⣿⠆⠀⢀⣸⣇⣀⠀")
print("⠀ ⠐⠋⢻⣅⡄⢀⣀⣀⡀⠀⠯⠽⠂⢀⣀⣀⡀⠀⣤⣿⠀⠉⠀")
print(" ⠀⠀⠴⠛⠙⣳⠋⠉⠉⠙⣆⠀⠀⢰⡟⠉⠈⠙⢷⠟⠈⠙⠂⠀")
print(" ⠀⠀⠀⠀⠀⢻⣄⣠⣤⣴⠟⠛⠛⠛⢧⣤⣤⣀⡾⠀⠀⠀")

print("\n •───────────────────•°•❀•°•───────────────────•\n")

print(
 " You will have to answer 10 Hello Kitty related \n questions!Try your best! Good luck!\n"
)

print(Fore.RED + ' Warning: As of right now, you will have to type\n your answer out entirely.' + Style.RESET_ALL)


print("\n •───────────────────•°•❀•°•───────────────────•\n")

score = 0
q_and_a = questions.questions_and_answers
ans = questions.answers
wrongAns = []

for x in range(1, 11):
	question_number = 'q' + str(x)
	question = str(x) + ") " + q_and_a[question_number][0]
	print(question + "\n")

	if isinstance(q_and_a[question_number][1], list):
		answers = q_and_a[question_number][1]
		for i in range(len(answers)):
			answer = "   " + answers[i]
			print(answer)
	else:
		answer = "   " + q_and_a[question_number][1]
		print(answer)
	print()

	userAnswer = input(Fore.MAGENTA + 'Your answer: ' + Style.RESET_ALL)

	if (userAnswer == ans['q' + str(x) + 'answer']):
		score += 1
	else:
		wrongAns.append(q_and_a[question_number][0])
	print()

print(" •───────────────────•°•❀•°•───────────────────•\n")
print("That's the end of the Hello Kitty quiz! ")

if (score == 10):
	print("My goodness! You scored 10/10! Well done! ❀")
else:
	print("You scored " + str(score) + "! Here are the questions you got wrong:\n")
	for x in wrongAns:
		print("> " + x)

	print("\nBetter luck next time!")

print("\n •───────────────────•°•❀•°•───────────────────•\n")