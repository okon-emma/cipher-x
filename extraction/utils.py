##This file contains the functions

def result(score):
    ##home_wins
    if score == '1-0' or score == '2-1' or score == '2-0' or score == '3-1' or score == '3-0' or score == '3-2':
        return('3')
    if score == '4-0' or score == '4-1' or score == '5-0' or score == '4-2' or score == '6-0' or score == '5-1':
        return('3')
    ##home_lose
    if score == '1-2' or score == '0-1' or score == '1-3' or score == '0-2' or score == '2-3' or score == '0-3':
        return('0')
    if score == '1-4' or score == '0-4' or score == '2-4' or score == '0-5' or score == '1-5' or score == '0-6':
        return('0')
    ##match_drawn
    if score == '0-0' or score == '1-1' or score == '2-2' or score == '3-3':
        return('1')

def home_score(score):
    return(score[0])

def away_score(score):
    return(score[2])

def goal_goal(score):
    if score == '1-0' or score == '2-0' or score == '3-0' or score == '4-0' or score == '5-0' or score == '6-0' or score == '0-0':
        return('0')
    if score == '0-1' or score == '0-2' or score == '0-3' or score == '0-4' or score == '0-5' or score == '0-6':
        return('0')
    if score == '2-1' or score == '3-1' or score == '3-2' or score == '4-1' or score == '4-2' or score == '5-1':
        return('1')
    if score == '1-2' or score == '1-3' or score == '2-3' or score == '1-4' or score == '2-4' or score == '1-5':
        return('1')
    if score == '1-1' or score == '2-2' or score == '3-3':
        return('1')

def over_1(score):
    if score == '0-0' or score == '0-1' or score == '1-0':
        return('0')
    else:
        return('1')

def over_2(score):
    if score == '0-0' or score == '0-1' or score == '1-0' or score == '1-1' or score == '2-0' or score == '0-2':
        return('0')
    else:
        return('1')

def over_3(score):
    if score == '0-0' or score == '0-1' or score == '1-0' or score == '1-1' or score == '2-0' or score == '0-2':
        return('0')
    elif score == '3-0' or score == '0-3' or score == '2-1' or score == '1-2':
        return('0')
    else:
        return('1')

def over_4(score):
    if score == '0-0' or score == '0-1' or score == '1-0' or score == '1-1' or score == '2-0' or score == '0-2':
        return('0')
    elif score == '3-0' or score == '0-3' or score == '2-1' or score == '1-2' or score == '2-2':
        return('0')
    elif score == '4-0' or score == '0-4' or score == '3-1' or score == '1-3':
        return('0')
    else:
        return('1')

def hodd(h,a):
    f = open('odd2.csv', 'r')
    for line in f:
        row = line.split(',')
        if h in row[0] and a in row[0]:
            h_ = str(row[1])
            return(h_)
    f.close()

def dodd(h,a):
    f = open('odd2.csv', 'r')
    for line in f:
        row = line.split(',')
        if h in row[0] and a in row[0]:
            d_ = str(row[2])
            return(d_)
    f.close()

def aodd(h,a):
    f = open('odd2.csv', 'r')
    for line in f:
        row = line.split(',')
        if h in row[0] and a in row[0]:
            a_ = str(row[3])
            return(a_)
    f.close()

def res(score):
    ##home_wins
    if score == '1-0' or score == '2-1' or score == '2-0' or score == '3-1' or score == '3-0' or score == '3-2':
        return('2')
    if score == '4-0' or score == '4-1' or score == '5-0' or score == '4-2' or score == '6-0' or score == '5-1':
        return('2')
    ##home_lose
    if score == '1-2' or score == '0-1' or score == '1-3' or score == '0-2' or score == '2-3' or score == '0-3':
        return('0')
    if score == '1-4' or score == '0-4' or score == '2-4' or score == '0-5' or score == '1-5' or score == '0-6':
        return('0')
    ##match_drawn
    if score == '0-0' or score == '1-1' or score == '2-2' or score == '3-3':
        return('1')
