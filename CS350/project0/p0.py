#/usr/bin/python3
#
# Project 0 is a set of small functions to warm up with python3 and discrete math.
# [[[[1#]]]]


#[[[[0#]]]]
# I *John Robertson* have written all of this project myself, without any
# unauthorized assistance, and have followed the academic honor code.
#[[[[1#]]]]



import re

### Modify code below.
#[[[[0#]]]]



def phonenumber(s):
    """Converts formatted 10-digit phone numbers like '(123) 456-7890' to integers like 1234567890 or returns None when malformed"""
    r = re.compile("^\(\d{3}\) \d{3}-\d{4}$")
    x = r.findall(s)
    if x:
        subject = x[0]
        retString = ""
        for i in subject:
            if i not in '() -':
                retString += i
        return retString
    else:
        return None

def is_leapday(s):
    """Decides if a date/time like 'Mar 23, 2002 4:12:55am' is during a leap day
       Returns None when the date is invalid, True when it is a leap day, False otherwise"""
    r = re.compile(r"^\w{3} \d{1,2}, \d{4} \d{1,2}:\d{2}:\d{2}am|pm$")
    x = r.findall(s)
    if r:
        re.purge()
        newR = re.compile("\d{4}")
        yr = newR.findall(s)
        year = int(yr[0])
        if "Feb 29" in s and year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            return True
        return False
    else:
        return None

def evalsum(s):
    """Returns a string encoding a sum expression as a value."""
    expr = re.compile("\d*\.?\d+|\+|-|\s")
    nums = expr.findall(s)
    for i in nums:
        if i.isalpha() or not i.isdecimal() and i not in "+.- " and "." not in i:
            return None
    if s[-1] in ".+-" or ".+" in s or ".-" in s:
        return None
    sum = 0.0
    for i in nums:
        if nums.index(i) == 0:
            sum += float(i)
        if i not in "+- ":
            if nums.index(i) < len(nums):
                if nums[nums.index(i)-1] == "+":
                    sum += float(i)
                elif nums[nums.index(i)-1] == "-":
                    sum = sum - float(i)
    return sum

def cuberoot(n):
    """Computes the cube root of float n by fixpoint iteration"""
    from math import isclose, sqrt
    def iterToFix(fun, x):
        v = fun(x)
        if v == x or isclose(v, x, abs_tol=0.000000001):
            return x
        return iterToFix(fun, v)
    def curt(guess):
        return (n/(2*guess))/guess + guess/2
    return round(iterToFix(curt, 1), 8)

def powerset(st):
    """computes the power set of an input set st"""
    sot = st.copy()
    if len(sot) == 0:
        return frozenset({frozenset({})})
    for i in st:
        sat = set(sot.copy())
        sat.pop()
        sut = powerset(sat)
        for j in sut:
            sot = sot | frozenset({j})
        sot = frozenset(sot | frozenset({i}) | frozenset({j for j in sut}))
    return sot
#print(powerset({1,2}))

def cartesianproduct(lst):
    """Takes a list of sets/frozensets and computes their Cartesian product"""
    if len(lst) == 0:
        return set(lst)
    elif len(lst) == 1:
        x = lst[:]
        x[0] = tuple(x[0])
        return set(x)
    else:
        x = lst[:]

    def collater(num, *args):
        pass

def transitiveclosure(g):
    """computes the transitive closure of a graph/relation encoded as as a set of 2-tuples"""
    gCl = set(g.copy())
    nodes = []
    for i in g:
        nodes.append(i[0])
        nodes.append(i[1])
    nodes = list(set(nodes))
    exes = [x[0] for x in g]
    wyes = [y[1] for y in g]
    end = max(wyes)
    for i in exes:
        for j in range(i, end):
            gCl.add((i, j + 1))
    wyes.remove(end)
    for i in wyes:
        for j in range(i, end):
            gCl.add((i, j + 1))
    return frozenset(gCl)
