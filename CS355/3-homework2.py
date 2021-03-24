"""
Each of the k jars contain m white and n black balls. A ball is randomly chosen from jar 1 and transferred to jar 2, then a ball is randomly chosen from jar 2 and transferred to jar 3, etc. Finally, a ball is randomly chosen from jar k. Show that the probability that the last ball is white is the same as the probability that the first ball is white, i.e., it is m/(m+n).
"""
from random import choice
m = 10
n = 5
k = 5
def first():
    white = ["w" for i in range(m)]
    black = ["b" for i in range(n)]
    jar = white + black
    first = choice(jar)
    if first == "w":
        return 1
    return 0
def last():
    white = ["w" for i in range(m)]
    black = ["b" for i in range(n)]
    jar = white + black
    jark = jar[:]
    for i in range(k):
        jark.append(choice(jar))
        jar = jark[:]
        jark.pop()
    last = choice(jark)
    if last == "w":
        return 1
    return 0
trials = 2**15
firsts, lasts = 0, 0
for i in range(trials):
    firsts += first()
    lasts += last()
print(m/(m+n)) """the simple formula"""
print(firsts/trials) """for picking from a jar once"""
print(lasts/trials) """for transferring jars"""