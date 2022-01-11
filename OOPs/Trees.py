
# creating a binary tree using classes in python


class BinaryTree():
# A binary tree has three things to consider root, left, right

    def __init__(self, *data): 
    
        if(len(data) == 1):

            # inserting data into the root of binary tree
            self.data = data[0]
        
            # creating left and right branches for binary tree
            self.left = BinaryTree()
            self.right = BinaryTree()

    def insert_left(self,data):
        self.left.data = data
    
    def insert_right(self, data):
        self.right.data = data


tree1 = BinaryTree(100)
tree1.insert_left(200)
tree1.insert_right(300)
