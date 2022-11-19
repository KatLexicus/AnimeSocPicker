import random

# import mal
import pandas as pd
# from mal import *

with open('suggestions.csv', 'r', encoding="utf-8") as csvfile:
    fileinput = pd.read_csv('suggestions.csv')

    print('Incumbent Anime is Megalo box ' + '\n' +
          'Thursday Session Anime Suggestions:' + '\n' 'Ran by @Lexi.f'
          + '\n \n' + 'These are the choices for Thursday this week: ')
    fileinput.pop("Suggested by:")
    fileinput = fileinput.to_string().splitlines()
#
# for line in input:
#     lineOut = AnimeSearch(line).results[0]
#     print(line + " " + lineOut.title + " " + lineOut.url)


for i in range(8):
    randomLine = random.choice(fileinput)
    print(randomLine)

print('\n' + "One alternate suggestion can be entered into the Anime Suggestions forum with it being "
          "voted on in the same way but this has to be done with discord for fairness :nerd:")
