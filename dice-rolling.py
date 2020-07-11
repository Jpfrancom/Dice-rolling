from random import randint
dice = []
def throw_dice(amount_dice):
    for c in range(0, amount_dice):
        dice_num = randint(0,6)
        dice.append(dice_num)
    for i, u in enumerate(dice):
        print(f'=> the {i+1}° was {u}')
throw_dice(int(input('How much dice will be played? ')))