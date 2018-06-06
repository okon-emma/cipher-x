from bs4 import BeautifulSoup
from utils import result, home_score, away_score, hodd, dodd, aodd
from utils import goal_goal, over_1, over_2, over_3, over_4
import datetime
import os

directory = os.fsencode("database")

f = open("data.csv", "w")
f.write("home,score,away,result,home_score,away_score,goal_goal,over_1,over_2,over_3,over_4,home_odd,draw_odd,away_odd\n")


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print("database/" + filename)
    count = 0
    now = str(datetime.datetime.now())
    soup = BeautifulSoup(open("database/" + filename), 'html.parser')
    weeks = soup.findAll('td', {'style':'width: 33%; text-align:center; background-color: #E1E3E6; padding: 7px'})
    odds = soup.findAll('td', {'style':'width:19%; text-align:center'})

    for week in weeks:
        weekn = week.findAll('tr')
        count = count +1
        #print("Week " + str(count) + " ...")
        print(":", end="")

        for match in weekn:
            match1 = match.findAll('td')
            if len(match1) == 3:
                home = match1[0].text
                score = match1[1].text
                away = match1[2].text

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


                f.write(home + "," + score + "," + away + "," + result(score) + "," + home_score(score) + "," + away_score(score) + "," + goal_goal(score) + "," + over_1(score) + "," + over_2(score) + "," + over_3(score) + "," + over_4(score) + "," + hodd(s_home,s_away) + "," + dodd(s_home,s_away) + "," + aodd(s_home,s_away) + "\n")

    print(">>database/" + filename)

f.close()
print("Porting Successfully Finished")
