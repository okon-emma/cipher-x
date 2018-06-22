import numpy as np
import pandas as pd
import os
from utils import hodd, aodd

f = open("train.csv", "w")
f.write("r3,r2,r1,odd,class\n")

directory = os.fsencode("snippets")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    df = pd.read_csv("snippets/" + filename)
    result = df['result']
    home_col = df['home']
    away_col = df['away']
    arg = filename[12:15]
    print(".." + filename)

    for r in range(3,38):
        r1 = r - 1
        r2 = r - 2
        r3 = r - 3
        sr3 = result[r3]
        sr2 = result[r2]
        sr1 = result[r1]
        sr = result[r]
        home = home_col[r]
        away = away_col[r]


        if home == 'LEI':
            s_home = 'lei'
        if home == 'WBA':
            s_home = 'wba'
        if home == 'WHU':
            s_home = 'whu'
        if home == 'MNU':
            s_home = 'mnu'
        if home == 'STC':
            s_home = 'stc'

        if home == 'CHE':
            s_home = 'che'
        if home == 'WAT':
            s_home = 'wat'
        if home == 'BRI':
            s_home = 'bri'
        if home == 'NWC':
            s_home = 'nwc'
        if home == 'BOU':
            s_home = 'bou'

        if home == 'SWA':
            s_home = 'swa'
        if home == 'BUR':
            s_home = 'bur'
        if home == 'ARS':
            s_home = 'ars'
        if home == 'TOT':
            s_home = 'tot'
        if home == 'EVE':
            s_home = 'eve'

        if home == 'HUD':
            s_home = 'hud'
        if home == 'LIV':
            s_home = 'liv'
        if home == 'CRY':
            s_home = 'cry'
        if home == 'SOU':
            s_home = 'sou'
        if home == 'MNC':
            s_home = 'mnc'

################################################################
################################################################

        if away == 'LEI':
            s_away = 'lei'
        if away == 'WBA':
            s_away = 'wba'
        if away == 'WHU':
            s_away = 'whu'
        if away == 'MNU':
            s_away = 'mnu'
        if away == 'STC':
            s_away = 'stc'

        if away == 'CHE':
            s_away = 'che'
        if away == 'WAT':
            s_away = 'wat'
        if away == 'BRI':
            s_away = 'bri'
        if away == 'NWC':
            s_away = 'nwc'
        if away == 'BOU':
            s_away = 'bou'

        if away == 'SWA':
            s_away = 'swa'
        if away == 'BUR':
            s_away = 'bur'
        if away == 'ARS':
            s_away = 'ars'
        if away == 'TOT':
            s_away = 'tot'
        if away == 'EVE':
            s_away = 'eve'

        if away == 'HUD':
            s_away = 'hud'
        if away == 'LIV':
            s_away = 'liv'
        if away == 'CRY':
            s_away = 'cry'
        if away == 'SOU':
            s_away = 'sou'
        if away == 'MNC':
            s_away = 'mnc'



        if sr3 == 0:
            s3 = '0'
        if sr3 == 1:
            s3 = '1'
        if sr3 == 3:
            s3 = '3'

        if sr2 == 0:
            s2 = '0'
        if sr2 == 1:
            s2 = '1'
        if sr2 == 3:
            s2 = '3'

        if sr1 == 0:
            s1 = '0'
        if sr1 == 1:
            s1 = '1'
        if sr1 == 3:
            s1 = '3'

        if sr == 0:
            s = '0'
        if sr == 1:
            s = '1'
        if sr == 3:
            s = '3'

        #f.write(s3 + "," + s2 + "," + s1 + "," + hodd(s_home, s_away) + "," + s + "\n")

        if arg == home:
            f.write(s3 + "," + s2 + "," + s1 + "," + hodd(s_home, s_away) + "," + s + "\n")
        if arg == away:
            f.write(s3 + "," + s2 + "," + s1 + "," + aodd(s_home, s_away) + "," + s + "\n")

f.close()
