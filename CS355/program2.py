"""
Simulate a pond with algae AND FISH and growth therein
John Phillip Robertson
04//2020
"""

from random import random, choice, randint, shuffle

# Event chances for algae activities
alg_die = 0.1
alg_reproduce = 0.2 + alg_die
alg_survive = 0.1 + alg_reproduce
# alg_migrate = None  # it is implicitly > alg_survive and < 1.0


class Algae():
    def __init__(self):
        self.alga = 2
        self.fish = []

    """
    Migration logic is contained in the Lake class instead.
    Death is simple: decrement alga.
    Reproduction is increment.
    """

    def step(self):
        chance = random()
        salga = self.alga
        if salga <= 3:
            if chance < alg_die:
                salga -= 1
                if salga >= 5:
                    salga = 4
            elif alg_die < chance < alg_reproduce:
                salga += 1
            # elif alg_reproduce < chance < alg_survive:
            #    pass
            elif alg_survive < chance:
                salga -= 1  # This will be incremented no matter what: either +1 for an adjacent cell, or -1 + 1 for the same cell
                return "move"


class Fish():
    def __init__(self):
        self.hp = 2

    def cycle(self, alga):
        self.hp -= 1
        if self.hp < 5:  # feeding logic
            if random() > .5:
                alga.alga -= 1
                self.hp += 3
                if self.hp > 5:  # satiety logic
                    self.hp = 5
        return self


class Lake():
    """
    The Lake class primarily consists of a 100^3 array of Algae plus a count of the fish.
    The Algae, more fittingly called "cells", contain a count of algae within
    as well as a list of Fish.
    """

    def __init__(self):
        self.fish_count = 100000  # Alternate 1000000
        self.lake = [[[Algae() for i in range(100)]
                      for j in range(100)] for k in range(100)]
        for i in range(self.fish_count):
            self.lake[randint(0, 99)][randint(
                0, 99)][randint(0, 99)].fish.append(Fish())
        # Above populates random Algae cells with fish.

    def valid_migration(self, i, j, k):
        try:
            return self.lake[i][j][k]
        except IndexError:
            # Kludge, but what can you do? If something returns, it will be truthy anyway.
            return False

    def cycle(self, steps):
        # I reset these after every iteration and count afresh.
        # The indices correspond precisely to which number is being counted.
        count = [0, 0, 0, 0, 0]
        for step in range(steps):
            for i in self.lake:
                for j in i:
                    for k in j:
                        result = k.step()
                        kalga = k.alga
                        if result == "move":
                            # a random surrounding cell is chosen, but only if it is valid
                            alGet = self.valid_migration(
                                self.lake.index(i) + choice((1, 0, -1)),
                                i.index(j) + choice((1, 0, -1)),
                                j.index(k) + choice((1, 0, -1))
                            )
                            if alGet:
                                alAl = alGet.alga
                                alAl += 1
                                if alAl >= 5:
                                    alAl = 4
                            else:
                                kalga += 1
                                if kalga >= 5:
                                    kalga = 4
                        # Every single bit of this is kludge but it's more efficient than counting post-facto
                        if kalga == 0:
                            count[0] += 1
                        elif kalga == 1:
                            count[1] += 1
                        elif kalga == 2:
                            count[2] += 1
                        elif kalga == 3:
                            count[3] += 1
                        elif kalga == 4:
                            count[4] += 1
                        # End counting. Begin fish handling.
                        kish = k.fish
                        for f in kish:
                            f.cycle(k)
                            if f.hp <= 0:
                                kish.remove(f)
                                del f
                                self.fish_count -= 1
                                continue
                            fiGet = self.valid_migration(
                                self.lake.index(i) + choice((1, 0, -1)),
                                i.index(j) + choice((1, 0, -1)),
                                j.index(k) + choice((1, 0, -1))
                            )
                            if fiGet:
                                kish.remove(f)
                                fiGet.fish.append(f)
                        if len(kish) >= 2:
                            shuffle(kish)
                            f1 = kish[0]
                            f2 = kish[1]
                            f1.hp -= 1
                            f2.hp -= 1
                            kish.extend([f1, f2])
                            kish.append(Fish())
                            self.fish_count += 1

            print(
                f"Generation {step + 1}: {self.fish_count} Fish, {count[1] + count[2] + count[3] + count[4]} Algae ({count[0]} of 0, {count[1]} of 1, {count[2]} of 2, {count[3]} of 3, {count[4]} of 4)"
            )


if __name__ == "__main__":
    green_goodness = Lake()
    green_goodness.cycle(1000)
