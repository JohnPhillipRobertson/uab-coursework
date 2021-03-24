from random import choice


def trial(n):
    four = (0, 1, 2, 3)
    output = []
    for i in range(n):
        output.append(choice(four))
    return output


for i in [1000, 10000, 100000]:
    print(round(trial(i).count(0)/i, 4), end="\t|")
    print(round(trial(i).count(1)/i, 4), end="\t|")
    print(round(trial(i).count(2)/i, 4), end="\t|")
    print(round(trial(i).count(3)/i, 4))
    print("-"*31)
