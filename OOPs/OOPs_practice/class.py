
# basic class in python contains
# 1) data members
# 2) methods of the class

Root = None


class Tree():

    # Data members of the tree
    size = 5
    left_recursion, right_recursion = 0, 0
    # we also have a concept class constructor in python

    def __init__(self, value):

        global Root

        self.value = value
        traverser = Root

        if (Root == None):
            Root = self
            traverser = Root

        # These are the left and right nodes of the root
        self.left = None
        self.right = None

    # Methods of the tree are
    def insert_element(self, value):

        global Root
        t1 = Tree(value)
        traverser = Root

        print(traverser.value)
        print(traverser != None)
        print(traverser.value and traverser != None)

        while (traverser.value > t1.value and traverser.left != None):
            traverser = traverser.left
        while (traverser.value < t1.value and traverser.right != None):
            traverser = traverser.right

        if (traverser.value > t1.value):
            traverser.left = t1
        else:
            traverser.right = t1

    def preorder_traversal(self, t1):

        # preorder traversal of the tree is done in the following way
        # root, left, right

        # first note down root of the tree
        treversal = self

        # creating a traversal which traverses till the end of the tree
        # then go to the left of the tree and note down its value as it is the root of the sub tree
        # repeat
        print(self.value)
        if (treversal.left != None):
            self.left.preorder_traversal(t1)

        # after the root and left part of the tree gets finished
        # fetch the right element of the tree [This can be done by using recursion]
        if (self.right != None):
            self.right.preorder_traversal(t1)

    def delete_element(self, value):
        print(value)
        pass

    def search(self, value):
        print(value)
        pass


t1 = Tree(10)
t1.insert_element(20)
t1.insert_element(30)
t1.insert_element(40)
t1.insert_element(50)
t1.insert_element(25)
t1.insert_element(15)
t1.insert_element(7)
t1.insert_element(5)

print('---------------------------------------------------------------------------------')
t1.preorder_traversal(t1)

print('---------------------------------------------------------------------------------')
print(t1.left_recursion)
print(t1.right_recursion)
