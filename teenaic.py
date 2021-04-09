def pointsystem():
    points = 0
    cycle = 0
    items = input(" There are items scattered on the beach. You see plastic bottles, glass and paper. Pick up 20 points worth of thrash. ",
                  "",
                  " You can only pick up 5 items' ",
                  " Which one do you want to pick up? ",
                  "a) Plastic bottles ", " b) Glass ", " or ", " c) Paper ")
    while points < 20 and cycle < 5:
        if items == a:
            points = points + 5
        elif items == b:
            points = points + 3
        elif items == c:
            points = points + 1

return points

def redeemable():
    if points >= 50:
        print(" You have more than enough to redeem a BruToken ")
        print(" You have redeemed the token ")
    elif points < 50:
        print(" You do not have enough points to claim a toke. Please do more mission or activities to earn enough points ")


def main():
    points = pointsystem()
    print(" You have a total of: ", points)
    boolean = input(" Do you wish to redeem it? (yes/no) ")
    if boolean = yes:
        redeemable()
    elif:
        print(" Thank you for playing the game ")
    
    /// hahha tested here :) 
