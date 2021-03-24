class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.p = None
    def __str__(self):
        return str(self.key) + "|" + str(self.val)

class Tree:

    def __init__(self):
        self.root = None

    def tree_insert(self, z_key, z_val):
        z = Node(z_key, z_val)
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder_tree_walk(self):
        l = []
        def itw(x, y):
            if x != None:
                itw(x.left, y)
                y.append(str(x))
                itw(x.right, y)
        itw(self.root, l)
        for i in l:
            print("\t" + i)

    def tree_search(self, k):
        def _tree_search(k, x):
            if x == None:
                return Node(-1, "Not Found")
            elif k == x.key:
                return x
            if k < x.key:
                return _tree_search(k, x.left)
            else:
                return _tree_search(k, x.right)
        return _tree_search(k, self.root)

# test code

def main():
    from random import randrange, choice
    groot = Tree()
    print("Test on no elements")
    groot.inorder_tree_walk()
    print("Nothing was printed")
    x = [randrange(512) for i in range(12)]
    print("List form: " + str(x))
    for i in x:
        groot.tree_insert(i, i)
    print("Tree form: ")
    groot.inorder_tree_walk()
    del groot
    groot = Tree()
    print("Sorted list")
    x = [i for i in range(12)]
    print(x)
    for i in x:
        groot.tree_insert(i, i)
    print("As a tree: ")
    groot.inorder_tree_walk()
    x.sort(reverse=True)
    print("Reverse-sorted list")
    print(x)
    print("As a tree: ")
    del groot
    groot = Tree()
    for i in x:
        groot.tree_insert(i, i)
    groot.inorder_tree_walk()
    s = choice(x)
    print("Finding something: ")
    print(groot.tree_search(s).val)
    print("Finding something that isn't there: ")
    print(groot.tree_search(-1).val)

if __name__ == "__main__":
    main()
