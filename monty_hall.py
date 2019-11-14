'''
We need 3 doors(maybe more). One door has a new car behind it. The other two have loathsome goats. 
    1. Generate doors and prizes
    2. Player choice
    3. Monty removes a wrong door
    4. Player Choice
    5. The big reveal! 
        a. The unchosen door is revealed first
        b. The chosen door is revealed after
'''
import random
prizes = []
choice = []

# Randomizes the elements of the prizes list
def assign_prizes():
    prizes = random.shuffle([0,0,1])

# Chooses a door at random
def door_choice(lst):
    print(lst)
    choice = lst.pop(lst[0])
    return choice
    
# Removes one of the wrong doors
def remove_door(prizes):
    for door in prizes:
        if prizes[door] == False:
            prizes.remove(prizes[door])
            break

# def clean_up(choices):
#     if door_choice != 1 or 2 or 3:
#         return
#     elif door_choice == 1:
#         remove_door(prizes[1],prizes[2])
#     elif door_choice == 2:
#         remove_door(prizes[0],prizes[2])
#     elif door_choice == 3:
#         remove_door(prizes[0],prizes[1])

def reveal():
    pass

# main sequence
# while True:
#     assign_prizes()
#     choice()
#     remove_door()
#     choice()
#     reveal()
