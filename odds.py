from bs4 import BeautifulSoup

count = 0
soup = BeautifulSoup(open("data/vfl.html"), 'html.parser')
odds = soup.findAll('td', {'style':'width:19%; text-align:center'})

count = 0
for odd in odds:
    count = count +1
    #print(str(count) + " ...")
    ftcount = [0,1,2,3,4,5,6,7,8,9]
    for ftc in ftcount:
        fth = odd.findAll('label', {'for':'Match_Result_' + str(ftc) + '_Home'})
        for ft0 in fth:
            print(ft0.text)

        ftd = odd.findAll('label', {'for':'Match_Result_' + str(ftc) + '_Draw'})
        for ft2 in ftd:
            print(ft2.text)
        fta = odd.findAll('label', {'for':'Match_Result_' + str(ftc) + '_Away'})
        for ft1 in fta:
            print(ft1.text)
            print("")
