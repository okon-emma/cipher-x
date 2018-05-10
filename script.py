from bs4 import BeautifulSoup
from utils import outcome
import datetime

count = 0
now = str(datetime.datetime.now())
soup = BeautifulSoup(open('vfl.html'), 'html.parser')
weeks = soup.findAll('td', {'style':'width: 33%; text-align:center; background-color: #E1E3E6; padding: 7px'})

f = open("data.csv", "w")
f.write("home, score, away, outcome \n")

for week in weeks:
    weekn = week.findAll('tr')
    count = count +1
    print("Week " + str(count) + " Ported")

    for match in weekn:
        match1 = match.findAll('td')
        if len(match1) == 3:
            home = match1[0].text
            score = match1[1].text
            away = match1[2].text
            f.write(home + "," + score + "," + away + "," + outcome(score) + "\n")

f.close()
print("Data Ported to CSV format")
