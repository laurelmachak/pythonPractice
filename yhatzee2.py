from random import randint

def roll(hand):
    dice = []
    for i in range(5 - len(hand)):
        dice.append(randint(1,6))
    return dice
    
def choose_Hand(hand):
    if len(hand) == 0:
        memo = "\nIf you'd like to keep any dice from your roll, enter the numbers (1-6) seperated by spaces.\n If you don't want to keep any, enter '0':\n"
    else:
        memo = "\nEnter the dice you'd like to keep from both your hand and your roll (1-6) seperated by spaces. \n If you don't want to keep any, enter '0':\n"
    
    kept_dice = input(memo).split()
    if kept_dice[0] != "0":
        hand = []
        for item in (kept_dice):
            hand.append(int(item))
        
    return hand
        


hand = []

for i in range(3):
    first_roll = roll(hand)
    print("roll:", first_roll)
    hand = choose_Hand(hand)
    print("hand", hand)
