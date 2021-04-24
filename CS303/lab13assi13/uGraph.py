from math import inf


class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.flag = []
        self.d = 0
        self.pi = None
        self.neighbors = set()
        self.neighborNames = set()
        self.key = None
        self.keys = {}

    def __eq__(self, other):
        if self and other:
            if isinstance(other, Node):
                return self.name == other.name
        else:
            return False

    def add(self, neighbor, weight=inf):
        self.neighbors.add(neighbor)
        self.neighborNames.add(neighbor.name)
        self.keys[neighbor] = weight

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return id(self) + self.name

class Ugraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.span = []

    # https://realpython.com/iterate-through-dictionary-python/#iterating-through-items
    def extract_min(self, q):
        l = []
        for i in q.neighbors:
            try:
                l.append(q.keys[i])
            except KeyError:
                pass
        minimum = "guarantee"
        try:
            minimum = min(l)
        except ValueError:
            pass
        ret = None
        for i, j in q.keys.items():
            if j == minimum:
                ret = i
        return ret

    def mst_prim(self, r):
        for u in self.nodes:
            u.key = inf
            u.pi = None
        r.key = 0
        #https://stackoverflow.com/questions/59003032/how-do-you-iterate-through-a-queue-in-python-without-emptying-it?noredirect=1#comment104256465_59003032
        Q = self.nodes.copy()
        while Q:
            u = self.extract_min(Q.pop())
            self.span.append(u)
            if u != None:
                for v in u.neighbors:
                    if v in Q and u.keys[v] < v.key:
                        self.span.append(v)
                        v.pi = u
                        v.key = u.keys[v]

    # The following function is the help of TA Seoeui Hong

    def printGraph(self):
        for i in self.nodes:
            print(str(i) + "...", end="")
            for j in i.neighbors:
                print("to " + str(j) + " is " + str(i.keys[j]), end="; ")
            print()
        print()

    def spanTree(self):
        for i in self.span:
            if i.key != inf:
                print(i, end=", ")
                print(i.key)


def main():
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node0.add(node2, 0.26)
    node0.add(node7, 0.16)
    node0.add(node4, 0.38)
    node0.add(node6, 0.58)
    node1.add(node5, 0.32)
    node1.add(node7, 0.19)
    node1.add(node2, 0.36)
    node1.add(node3, 0.29)
    node2.add(node0, 0.26)
    node2.add(node1, 0.36)
    node2.add(node3, 0.17)
    node2.add(node6, 0.4)
    node2.add(node7, 0.34)
    node3.add(node1, 0.29)
    node3.add(node2, 0.17)
    node3.add(node6, 0.52)
    node4.add(node0, 0.38)
    node4.add(node5, 0.35)
    node4.add(node7, 0.37)
    node5.add(node1, 0.32)
    node5.add(node4, 0.35)
    node5.add(node7, 0.28)
    node6.add(node0, 0.58)
    node6.add(node2, 0.4)
    node6.add(node3, 0.52)
    node7.add(node0, 0.16)
    node7.add(node1, 0.19)
    node7.add(node2, 0.34)
    node7.add(node4, 0.37)
    node7.add(node5, 0.28)

    nodes = [node0, node1, node2, node3, node4, node5, node6, node7]

    graph = Ugraph(nodes)

    graph.mst_prim(node0)

    graph.printGraph()

    graph.spanTree()


if __name__ == "__main__":
    main()
