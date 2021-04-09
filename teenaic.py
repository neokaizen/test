def option():
    score = 10
    Error = False


    for x in range(1, 6):
Expand
Climate_action.txt
2 KB
﻿
def option():
    score = 10
    Error = False


    for x in range(1, 6):
        
        item = input(" There are items scattered on the beach. You see plastic bottles, glass and paper. Pick up 20 points worth of thrash. You can only pick up 5 items. Which one do you want to pick up? "
                      " a) Plastic bottles "
                      " b) Glass "
                      " c) Paper: ")
        while Error == True:
            if item == b:
                score = score + 3
            elif item == c:
                score = score + 1
            elif item == a:
                score = score + 5
            else:
                print(" Error ")
                Error = True


    return score


def redeemable(score):

    if score >= 50:
        print(" You have more than enough to redeem a BruToken ")
        print(" You have redeemed the token ")
    elif score < 50:
        print(" You do not have enough points to claim a token. Please do more mission or activities to earn enough points ")
        
    

def main():
    score = 10
    Player = input(" What is your name? ")
    print(" Hello, ", Player, " welcome to BruGreen, let's get started" )
    print("")
    Answer = option()
    print(" You have a total points of: ", Answer)
    Final = redeemable(score)
    
    
    
Climate_action.txt
2 KB
