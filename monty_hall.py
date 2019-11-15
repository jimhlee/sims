'''
We need 3 doors(maybe more). One door has a new car behind it. The other two have loathsome goats. 
    1. Generate doors and prizes
    2. Player choice
    3. Monty removes a wrong door
    4. Player Choice
    5. The big reveal! 
        a. The unchosen door is revealed first
'''
import random

# Randomizes the elements of the prizes list
def assign_prizes():
    prizes = [0,0,1]
    random.shuffle(prizes)
    return prizes

# Chooses a door at random
def door_choice(lst):
    popped = lst.pop(0)
    remove_door(lst)
    lst.insert(0,popped)
    return lst

# Removes one of the wrong doors
def remove_door(lst):
    for i in lst:
        if i == False:
            lst.remove(i)
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

# main sequence
def start(switch = False):
    blah = door_choice(assign_prizes())
    # won = blah[1 if switch else 0]
    won = blah[int(switch)]
    if won:
        print('You win a new car!')
        return True
    else:
        print('You won a smelly goat')
        return False

    #     if blah[0]:
    #         print('You win a new car!')
    #         return True
    #     else:
    #         print('You won a smelly goat')
    #         return False
    # else:
    #     if blah[1]:
    #         print('You win a new car!')
    #         return True
    #     else:
    #         print('You won a smelly goat')
    #         return False      

def win_rate(n_trials, foo = False):
    # if  switch == False:
    result = [start(foo) for _ in range(n_trials)]
    return sum(result) / len(result)
       
    # def same_prob(self, n_trials):
    #     result = [self.same_color_test(self.choose_two()) for _ in range(n_trials)]
    #     print(result)
    #     # return result.count(True) / len(result)
    #     return sum(result) / len(result)