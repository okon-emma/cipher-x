##This file contains the functions

def outcome(score):
    ##home_wins
    if score == '1-0' or score == '2-1' or score == '2-0' or score == '3-1' or score == '3-0' or score == '3-2':
        return('win')
    if score == '4-0' or score == '4-1' or score == '5-0' or score == '4-2' or score == '6-0' or score == '5-1':
        return('win')
    ##home_lose
    if score == '1-2' or score == '0-1' or score == '1-3' or score == '0-2' or score == '2-3' or score == '0-3':
        return('lose')
    if score == '1-4' or score == '0-4' or score == '2-4' or score == '0-5' or score == '1-5' or score == '0-6':
        return('lose')
    ##match_drawn
    if score == '0-0' or score == '1-1' or score == '2-2' or score == '3-3':
        return('draw')
