from bst import *


class RBNode(Node):
    def __init__(self, key=None, val=None):
        Node.__init__(self, key, val)
        self.color = "RED"

    def __str__(self):
        return "{}|{}|{}".format(self.key, self.val, self.color)


class RBT(Tree):
    def __init__(self):
        # https://stackoverflow.com/q/576169/9295513
        Tree.__init__(self)
        self.nil = None

    def leftRotate(self, x):
        T = self
        y = x.right
        x.right = y.left
        if y.left != T.nil:
            y.left.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        T = self
        y = x.left
        x.left = y.right
        if y.right != T.nil:
            y.right.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def RBinsertFixup(self, z):
        T = self
        while z is not T.root and z.p and z.p.p and z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y and y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z = z.p.p
                else:
                    if z and z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    if z.p:
                        z.p.color = "BLACK"
                    if z.p.p:
                        z.p.p.color = "RED"
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y and y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z = z.p.p
                else:
                    if z and z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    if z.p:
                        z.p.color = "BLACK"
                    if z.p.p:
                        z.p.p.color = "RED"
                    self.leftRotate(z.p.p)
        T.root.color = "BLACK"

    def _RBinsert(self, z):
        T = self
        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == T.nil:
            T.root = z
            z.color = "BLACK"
            # https://stackoverflow.com/q/15300550/9295513
            return None
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = "RED"
        self.RBinsertFixup(z)

    def RBinsert(self, key, val):
        self._RBinsert(RBNode(key, val))


def main():
    from random import randrange, choice
    groot = RBT()
    print("Test on no elements")
    groot.inorder_tree_walk()
    print("Nothing was printed")
    x = [randrange(512) for i in range(12)]
    print("List form: " + str(x))
    for i in x:
        print("Inserting ", end="")
        groot.RBinsert(i, i)
        print(i)
    print("Tree form: ")
    groot.inorder_tree_walk()
    del groot

    groot = RBT()
    print("Sorted list")
    x = [i for i in range(12)]
    print(x)
    for i in x:
        groot.RBinsert(i, i)
    print("As a tree: ")
    groot.inorder_tree_walk()
    x.sort(reverse=True)
    print("Reverse-sorted list")
    print(x)
    print("As a tree: ")
    del groot

    groot = RBT()
    for i in x:
        groot.RBinsert(i, i)
    groot.inorder_tree_walk()
    s = choice(x)
    print("Finding something: ")
    print(groot.tree_search(s).val)
    print("Finding something that isn't there: ")
    print(groot.tree_search(-1).val)
    del groot

    print("\nTests that show that the rotations work:")
    x = [5, 1, 6, 8, 9]
    y = [8, 4, 9, 2, 1]
    z = [10, 15, 5, 3, 1]
    # Values courtesy of Logan Creel
    print(x)
    print(y)
    print(z)
    rightTree = RBT()
    leftTree = RBT()
    finalTree = RBT()
    print("\nTree that works on first array")
    for i in x:
        rightTree.RBinsert(i, i)
    print("The root is {}".format(rightTree.root))
    rightTree.inorder_tree_walk()
    print("\nTree that works on second array")
    for i in y:
        leftTree.RBinsert(i, i)
    print("The root is {}".format(leftTree.root))
    leftTree.inorder_tree_walk()
    print("\nTree that works on third array (and the order they're inserted in)")
    for i in z:
        print(i)
        finalTree.RBinsert(i, i)
    print("The root is {}".format(finalTree.root))
    finalTree.inorder_tree_walk()

    print("One last demo: relations")
    a, b, c = RBNode(30, 30), RBNode(10, 10), RBNode(20, 20)
    family = [a, b, c]
    mesa = RBT()
    for i in family:
        mesa.RBinsert(i.key, i.key)
    print("Root is {}".format(mesa.root))
    print("Its left and right children are {} and {}".format(
        mesa.root.left, mesa.root.right))


if __name__ == "__main__":
    main()
