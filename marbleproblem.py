import random

class Marble(object):
    colors = ['Green','Red', 'Blue']
    def __init__(self):
        self.color = random.choice(self.colors)

    def __repr__(self):
        return self.color

class Bag(object):
    def __init__(self):
        self.contents = []
        for i in range(20):
            self.contents.append(Marble())

    def choose_two(self):
        chosentwo = []
        chosentwo = random.choices(self.contents, k=2)
        return chosentwo

    def same_color_test(self, choose_two):
        # How many times did the same color get chosen in the bag?
        # both_same = []
        # if choose_two[0] == choose_two[1]:
        #     both_same += 1
        # return both_same
        return choose_two[0] == choose_two[1]

    def same_prob(self, n_trials):
        result = [self.same_color_test(self.choose_two()) for _ in range(n_trials)]
        print(result)
        # return result.count(True) / len(result)
        return sum(result) / len(result)


    def __repr__(self):
        return str(self.contents)

if __name__ == "__main__":
    mybag = Bag()

# So I need to wrap the above functions in some shit that makes it go
# like a thousand times. I also need to have a state that I'm tracking in each of those iterations
'''
import random

def coin_flipper(n):
   return [random.random() > 0.5 for _ in range(n)]

def head_test(n_heads, n_flips):
   # with some number of flips, do you get at least n heads
   flips = coin_flipper(n_flips)
   return sum(flips) > n_heads

def heads_prob(n_trials, n_heads, n_flips):
   blah = [head_test(n_heads, n_flips) for _ in range(n_trials)]
   return sum(blah) / len(blah)
here's one i made for simulating a coin

head_test flips a coin n_flips # of times
and returns whether you got at least that many heads
heads_prob is a wrapper that for some number of trials
'''

