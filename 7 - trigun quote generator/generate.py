import pandas as pd
import random as ran
import colours as c

def ansToChar(userAns, character_list):
    userAns = userAns - 1

    if userAns <= 3:
        chosenChar = character_list[userAns]
        getRandomQuote(chosenChar)
    elif userAns == 4:
        random_number = ran.randint(0, 4)
        character_list.remove("Any")
        chosenChar = character_list[random_number]
        getRandomQuote(chosenChar)

data = pd.read_excel('trigun.xlsx')

def getRandomQuote(char):
    filtered_data = data[data['Character'] == char]

    if filtered_data.empty:
        print('No quotes found for {}'.format(char))
    else:
        random_number = ran.randint(1, 10)
        random_quote = filtered_data.iloc[random_number - 1]['Quote']
        print("\n"+ random_quote + c.bs + "\n	- " + char + c.rs)

