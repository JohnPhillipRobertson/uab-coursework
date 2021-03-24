"""
This is Monty Hall in diguise.
"""
from random import choice

coinOne = (1, 1)  # all heads
coinTwo = (0, 0)  # all tails
coinThree = (0, 1)  # all tails
coinTypes = [coinOne, coinTwo, coinThree]


def trial():
    pick = choice(coinTypes)
    if pick == coinThree:
        return 1
    else:
        return 0


count = 0
trials = 1000000
for i in range(trials):
    count += trial()
print(count/trials)
