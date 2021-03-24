"""
Simulate a pond with algae and growth therein
John Phillip Robertson
01/29/2020
"""

from random import random, choice

# Event chances for less than 3, for the second set of probabilities
l3die = 0.1 #0.2
l3reproduce = 0.3 + l3die #0.3
l3survive = 0.6 + l3reproduce #0.5
# Event chances for greater than 4, for the second set of probabilities
g4die = 0.3 #0.1
g4survive = 0.3 + g4die #0.4
g4migrate = 0.4 + g4survive #0.5

"""
An Algae data type is actually a cell within the lake (and I should have called it "Cell" in hindsight).
The Algae class contains the number of algae within it (called "alga" to avoid confusion).
The instructions to increase and decrease the amount of alga in an Algae object are within the class itself to take responsibility from the Lake class.
"""


class Algae():
    def __init__(self):
        self.alga = 2

    """
    This is to be invoked in the two situations where an Algae can have more than 4 alga after a cycle.
    """
    def kill(self):
        if self.alga >= 5:
            self.alga = 4

    """
    This is the main event of every cycle.
    Migration logic is contained in the Lake class instead.
    Death is simple: decrement alga.
    Reproduction is increment.
    Mere survival is a no-op put there so I wouldn't get nervous.

    """
    def step(self):
        chance = random()
        if self.alga <= 3:
            if chance < l3die:
                self.alga -= 1
            elif l3die < chance < l3reproduce:
                self.alga += 1
            elif l3reproduce < chance < l3survive:
                pass
        elif self.alga >= 4:
            if chance < g4die:
                self.alga -= 1
                self.kill()
            elif g4die < chance < g4survive:
                pass
            elif g4survive < chance < g4migrate:
                self.alga -= 1 #This will be incremented no matter what: either +1 for an adjacent cell, or -1 + 1 for the same cell
                return "move"


class Lake():
    """
    The Lake class primarily consists of a 100^3 array of Algae
    """

    def __init__(self):
        self.lake_size = 100
        self.lake = [[[Algae() for i in range(self.lake_size)]
                      for j in range(self.lake_size)] for k in range(self.lake_size)]
        #The above list comprehension builds a 3-d array, each with a fresh Algae object.

    def count(self):
        total = 0
        none = 0
        one = 0
        two = 0
        three = 0
        four = 0
        for i in self.lake:
            for j in i:
                for k in j:
                    total += k.alga
                    if k.alga == 0:
                        none += 1
                    elif k.alga == 1:
                        one += 1
                    elif k.alga == 2:
                        two += 1
                    elif k.alga == 3:
                        three += 1
                    elif k.alga == 4:
                        four += 1
        return (total, none, one, two, three, four)

    def valid_migration(self, i, j, k):
        try:
            return self.lake[i][j][k]
        except IndexError:
            return False #Kludge, but what can you do? If something returns, it will be truthy anyway.

    def cycle(self, steps):
        moves = (1, 0, -1)
        horizontal = []
        for step in range(steps):
            for i in self.lake:
                for j in i:
                    for k in j:
                        result = k.step()
                        if result == "move":  # aside from None, this is the only thing it can return
                            # a random surrounding alga is chosen, but only if it is valid
                            get = self.valid_migration(
                                self.lake.index(i) + choice(moves), i.index(j) + choice(moves), j.index(k) + choice(moves))
                            if get:
                                get.alga += 1
                                get.kill()
                            else:
                                k.alga += 1
                                k.kill()
                            #Both of the above "kill"s ensure that alga won't rise above 4.

            print(self.count())

#This is the "main."
green_goodness = Lake()
green_goodness.cycle(75)
