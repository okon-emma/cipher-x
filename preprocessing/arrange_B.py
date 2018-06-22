import numpy as np
import pandas as pd
import os
from utils import hodd, aodd


groups = [
'SOU','WAT','SWA','BRI','WBA',
'BOU','EVE','MNC','ARS','MNU',
'CRY','CHE','LEI','NWC','STC',
'LIV','WHU','BUR','HUD','TOT'
]


directory = os.fsencode("outputs")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    df = pd.read_csv("outputs/" + filename)
    home_col = df['home']
    score_col= df['score']
    away_col = df['away']
    result_col = df['result']
    print(filename + " >>>")

    for g in groups:
        f = open("snippets/" + filename + g + ".csv", "w")
        f.write("home,score,away,result\n")
        for r in range(0,380):
            ###FOCUS - HOME GAMES
            if home_col[r] == g:
                if result_col[r] == 0:
                    result = "0"
                if result_col[r] == 1:
                    result = "1"
                if result_col[r] == 3:
                    result = "3"

                f.write(home_col[r] + "," + score_col[r] + "," + away_col[r] + "," + result + "\n")
                #print(home_col[r], score_col[r], away_col[r], result_col[r])
            if away_col[r] == g:
                if result_col[r] == 0:
                    result = "3"
                if result_col[r] == 1:
                    result = "1"
                if result_col[r] == 3:
                    result = "0"
                f.write(home_col[r] + "," + score_col[r] + "," + away_col[r] + "," + result + "\n")
                #print(home_col[r], score_col[r], away_col[r], result_col[r])
        f.close()
