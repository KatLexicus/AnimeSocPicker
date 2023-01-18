import random

from mal import Anime
import pandas as pd
import re

# from mal import *

with open('suggestions.csv', 'r', encoding="utf-8") as csvfile:
    fileinput = pd.read_csv('suggestions.csv')

    print('Incumbent Anime is Megalo box ' + '\n' +
          'Thursday Session Anime Suggestions:' + '\n' 'Ran by @Lexi.f'
          + '\n \n' + 'These are the choices for Thursday this week: ')

for line in fileinput:
    lineOut = AnimeSearch(line).results[0]
    print(line + " " + lineOut.title + " " + lineOut.url)


fileinput = fileinput.to_string(index=False, justify="left").splitlines()
for line in range(8):
    line = random.choice(fileinput)
    line = re.sub(' +', ' ', line)
    print(line)
