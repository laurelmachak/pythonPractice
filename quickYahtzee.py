from random import randint

game = True
dice = []
next_roll = 5
hand = []

#keep.split()


while game == True: 
    for x in range(3):
        for i in range(next_roll):
            dice.append(randint(1,6))
        print("your roll:", dice)
        
        keep = input("\nenter the dice you'd like to keep from both your hand and your roll (1-6), seperated by spaces (if none, press '0'): ").split()
        print(keep)
        if len(keep)>0:
            hand = [keep]
        next_roll = 5 - len(keep)
        dice = []
        print("your hand:", hand)
            #for d in range(next_roll):
                #dice.append(0)
                
            
            
        print("\n")
            
    response = input("\ncontinue? y/n: ")
    if response == "n":
        break
        
        
def roll(hand):
    dice = []
    for i in range(5 - len(hand)):
        dice.append(randint(1,6))
    return dice
    
def choose_Hand(hand):
    if len(hand) == 0:
        memo = "\nIf you'd like to keep any dice from your roll, enter the numbers (1-6) seperated by spaces.\n If you don't want to keep any, enter '0':\n".split()
    else:
        memo = "\nEnter the dice you'd like to keep from both your hand and your roll (1-6) seperated by spaces. \n If you don't want to keep any, enter '0':\n".split()
    
    kept_dice = input(memo)
    if kept_dice[0] != "0":
        hand = []
        for kept_dice:
        hand.append(int(kept_dice))
        
    return hand
        
        
    
        
        



    