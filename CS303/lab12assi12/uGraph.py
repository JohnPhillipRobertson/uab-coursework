from queue import Queue
from math import inf

"""
Meanings of the variable names from the pseudocode:
s, u, v are Node objects
Node requires color, key, predecessor, depth
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.flag = []
        self.d = 0
        self.pi = None
        self.neighbors = set()
        self.neighborNames = set()
        self.f = 0

    def __eq__(self, other):
        if self and other:
            if isinstance(other, Node):
                return self.name == other.name
        else: return False

    def add(self, neighbor, dg=False):
        if not dg:
            for i in neighbor:
                self.neighbors.add(i)
                self.neighborNames.add(i.name)
                i.neighbors.add(self)
                i.neighborNames.add(self.name)
        else:
            for i in neighbor:
                self.neighbors.add(i)
                self.neighborNames.add(i.name)

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return id(self)


class Ugraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.topoList = []

    def bfs(self, s):
        for u in (set(self.nodes) - {s}):
            u.color = "WHITE"
            u.d = inf
            u.pi = None
        s.color = "GRAY"
        s.d = 0
        s.pi = None
        Q = Queue()
        Q.put(s)
        while not Q.empty():
            u = Q.get()
            for v in u.neighbors:
                if v.color == "WHITE":
                    v.color = "GRAY"
                    v.d = u.d + 1
                    v.pi = u
                    Q.put(v)
            u.color = "BLACK"

    def dfs(self):
        for u in self.nodes:
            u.color = "WHITE"
            u.pi = None
        time = 0
        for u in self.nodes:
            if u.color == "WHITE":
                self.dfs_visit(u, time)

    def dfs_visit(self, u, time):
        tim = time + 1
        u.d = tim
        u.color = "GRAY"
        for v in u.neighbors:
            if v.color == "WHITE":
                v.pi = u
                self.dfs_visit(v, tim)
        u.color = "BLACK"
        tim += 1
        u.f = tim
        self.topoList.insert(0, u)

    def topological_sort(self):
        self.dfs()
        return self.topoList


    def print_path(self, s, v):
        if v == s:
            print(s, end="--")
        elif v.pi == None:
            pass
            #print("NO PATH FROM {} TO {} EXISTS".format(s, v))
        else:
            self.print_path(s, v.pi)
            print(v, end="--")

    #The following function is the help of TA Seoeui Hong
    def printGraph(self):
        for i in self.nodes:
            print(str(i) + ":", end="")
            for j in i.neighbors:
                print(str(j) + " ", end="")
            print()
        print()

def main():
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node0.add([node2, node3], True)
    node1.add([node3, node4], True)
    node2.add([node5], True)
    #nothing for 3
    #or 4
    node5.add([node4], True)

    nodes = [node0, node1, node2, node3, node4, node5]

    for n in nodes:
        print("Neighbors", end=": ")
        for i in n.neighbors:
            print(str(i), end=", ")
        print()
    print("Over")

    graph = Ugraph(nodes)
    x = graph.topological_sort()
    for i in x:
        print(str(i), end=" ")


if __name__ == "__main__":
    main()
