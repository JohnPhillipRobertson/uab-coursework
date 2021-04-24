from HashEntry import *


class HashMap:

    def __init__(self, size=100):
        self.TABLE_SIZE = size
        # https://www.programiz.com/python-programming/anonymous-function
        self.loc = lambda k: k % self.TABLE_SIZE
        # https: // stackoverflow.com/questions/21581085/how-to-allocate-array-size-in-python/21581165
        # Array of HashEntrys
        self.table = [None for i in range(self.TABLE_SIZE)]

    def get(self, key, get_type="lin"):
        elem = self.loc(key)
        i = 0
        if get_type == "lin":
            while self.table[elem] != None and self.table[elem].key == key:
                i += 1
                elem = self.loc(key + i)
            return self.table[elem]
        elif get_type == "quad":
            while self.table[elem] != None and self.table[elem].key == key:
                elem = self.loc(key + (i**2))
                i += 1
            return self.table[elem]
        elif get_type == "cust":
            if self.table[elem] != None and self.table[elem].key == key:
                return self.table[elem]
            else:
                return self.get(self.loc(7 * key + 1))
        else:
            return "HashMap is empty"

    def linear_probe(self, key, value):
        brown = HashEntry(key, value)
        k = self.loc(key)
        i = 0
        while self.table[k] != None:
            k = self.loc(key + i)
            i += 1
        self.table[k] = brown

    def quadratic_probe(self, key, value):
        brown = HashEntry(key, value)
        i = 0
        k = self.loc(key)
        while self.table[k] != None:
            k = self.loc(key + (i**2))
            i += 1
        self.table[k] = brown

    def custom_probe(self, key, value):
        brown = HashEntry(key, value)
        k = self.loc(key)
        while self.table[k] != None:
            k = self.loc(7*k + 1)
        self.table[k] = brown

    def put(self, key, value, probe_type="lin"):
        brown = HashEntry(key, value)
        if self.table[self.loc(key)] == None:
            self.table[self.loc(key)] = brown
        elif self.table[self.loc(key)] != None:
            if probe_type == "lin":
                self.linear_probe(key, value)
            elif probe_type == "quad":
                self.quadratic_probe(key, value)
            elif probe_type == "cust":
                self.custom_probe(key, value)

# Testing:


def main():
    mesa = HashMap()
    print("Test on no elements")
    print(mesa.get(1))
    print("That's the error value.")

    x = [177, 360, 411, 46, 41, 462, 61, 474, 274, 300, 504]

    # Linear put
    print("Linear put: " + str(x))
    for i in x:
        mesa.put(i, str(i))
    for i in x:
        print(mesa.get(i))
    print()
    del mesa

    # Quadratic put
    mesa = HashMap()
    print("Quadratic put: " + str(x))
    for i in x:
        mesa.put(i, str(i), "quad")
    for i in x:
        print(mesa.get(i))
    print()
    del mesa

    # Custom put
    mesa = HashMap()
    print("Custom put: " + str(x))
    for i in x:
        mesa.put(i, str(i), "cust")
    for i in x:
        print(mesa.get(i))
    print()
    del mesa
    del x

    # Manual:
    mesa = HashMap()
    tupni = input(
        "Now for your input. Type in as many integers as you want, separated by spaces:\n")
    y = tupni.split()
    x = [int(i) for i in y]
    print(x)
    for i in x:
        mesa.put(i, str(i) + "val")
    loop = True
    while loop:
        tupni = input(
            "Now you may get. Enter one number you entered to print it, or press 'c' to stop the input loop.")
        if tupni == 'c':
            loop = False
        else:
            print(mesa.get(int(tupni)))


if __name__ == "__main__":
    main()
